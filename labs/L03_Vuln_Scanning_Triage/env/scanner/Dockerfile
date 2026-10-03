# The student's scanning workstation.
#
# Everything the guide needs is installed here so students never install tools
# on their own OS. It listens on nothing. The tool versions here do not change
# what is true about the targets — every value this lab asks for comes from the
# targets' own configuration and responses, not from a scanner's rating.
FROM debian:12.5-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
      nikto \
      nmap \
      curl \
      ca-certificates \
      openssl \
      jq \
      less \
      vim-tiny \
      iputils-ping \
      dnsutils \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /work
