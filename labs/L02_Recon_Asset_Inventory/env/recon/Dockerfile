# The student's recon workstation. Everything the guide needs is here so
# students never install tools on their own OS. The tool versions here do not
# affect what you can find on the segment.
FROM debian:12.5-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
      nmap \
      netcat-openbsd \
      curl \
      iputils-ping \
      dnsutils \
      telnet \
      mosquitto-clients \
      ca-certificates \
 && rm -rf /var/lib/apt/lists/*

CMD ["sleep", "infinity"]
