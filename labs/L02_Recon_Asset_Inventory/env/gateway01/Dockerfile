# Office device / IoT gateway. Runs two listeners:
#   23/tcp    legacy cleartext management console (socat + login banner)
#   1883/tcp  MQTT message broker, anonymous access allowed
#
# A small publisher also runs here and sends simulated device telemetry to the
# broker over loopback, so the broker carries real traffic rather than sitting
# empty. It opens no listener and changes no scanned port.
#
# Nothing here self-labels as risky. Any conclusion about these services has to
# be INFERRED from the protocol (cleartext) and the configuration (anonymous).
FROM alpine:3.20.3

# mosquitto = the broker; mosquitto-clients = mosquitto_pub/mosquitto_sub,
# needed here so the gateway can publish its own device traffic.
RUN apk add --no-cache mosquitto mosquitto-clients socat
COPY mosquitto.conf /etc/mosquitto/mosquitto.conf
COPY entrypoint.sh /entrypoint.sh
COPY telemetry.sh /telemetry.sh
RUN chmod +x /entrypoint.sh /telemetry.sh

EXPOSE 23 1883
ENTRYPOINT ["/entrypoint.sh"]
