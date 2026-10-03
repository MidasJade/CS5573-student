#!/bin/sh
# Start the telnet console listener and the device-telemetry publisher in the
# background, then run the MQTT broker in the foreground as PID 1.
#
# socat holds tcp/23 open with a login-style banner; nmap maps tcp/23 ->
# "telnet" by port number regardless of the banner.
#
# telemetry.sh publishes over loopback only. It waits for the broker to come up
# on its own, so ordering here does not matter, and it opens no listener — the
# segment's scanned surface is exactly tcp/23 and tcp/1883.
set -e

socat TCP-LISTEN:23,fork,reuseaddr,crlf SYSTEM:"printf 'Device Gateway Console\r\nlogin: '" &

/telemetry.sh &

exec mosquitto -c /etc/mosquitto/mosquitto.conf
