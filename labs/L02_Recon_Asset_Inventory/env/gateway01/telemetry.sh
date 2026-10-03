#!/bin/sh
# Simulated device traffic for this gateway's message broker.
#
# Publishes to the broker on LOOPBACK ONLY (127.0.0.1). It opens no listener,
# so it adds no host and no port to the segment — the scanned surface is
# unchanged. Values are derived from a counter, not randomness, so every
# student's traffic looks the same.
#
# Two kinds of messages:
#   retained  - device records, re-sent by the broker to each NEW subscriber the
#               moment it connects, so a subscriber sees something immediately
#               instead of waiting for the next reading.
#   periodic  - sensor readings and a heartbeat, every INTERVAL seconds.

BROKER=127.0.0.1
INTERVAL=5

# The broker starts in the foreground after this script is launched; retry
# until it is accepting connections.
until mosquitto_pub -h "$BROKER" -t gateway/boot -m started >/dev/null 2>&1; do
  sleep 1
done

# Retained device records. persistence is off in mosquitto.conf, so these are
# lost on a broker restart and re-published here on every container start.
mosquitto_pub -h "$BROKER" -r -t devices/thermostat-2f/status      -m 'online fw=1.4.2' || true
mosquitto_pub -h "$BROKER" -r -t devices/badge-reader-lobby/status -m 'online fw=2.1.7' || true
mosquitto_pub -h "$BROKER" -r -t devices/coldstore-01/status       -m 'online fw=3.0.1' || true
mosquitto_pub -h "$BROKER" -r -t devices/ups-rack-a/status         -m 'online fw=5.2.0' || true
mosquitto_pub -h "$BROKER" -r -t devices/printer-2f/status         -m 'online fw=1.0.9' || true

seq=0
while :; do
  seq=$((seq + 1))

  mosquitto_pub -h "$BROKER" -t sensors/floor2/thermostat/temp_c \
    -m "21.$((seq % 9))" >/dev/null 2>&1 || true
  mosquitto_pub -h "$BROKER" -t sensors/coldstore-01/temp_c \
    -m "-19.$((seq % 5))" >/dev/null 2>&1 || true
  mosquitto_pub -h "$BROKER" -t sensors/lobby/badge_reader/events \
    -m "scan door=lobby result=granted" >/dev/null 2>&1 || true
  mosquitto_pub -h "$BROKER" -t gateway/heartbeat \
    -m "seq=$seq uptime=$((seq * INTERVAL))s" >/dev/null 2>&1 || true

  # Occasional operational alert, so the stream is not perfectly uniform.
  if [ $((seq % 12)) -eq 0 ]; then
    mosquitto_pub -h "$BROKER" -t alerts/coldstore-01 \
      -m "temp_excursion threshold=-18.0" >/dev/null 2>&1 || true
  fi

  sleep "$INTERVAL"
done
