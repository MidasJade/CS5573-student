# The student's scanning workstation.
#
# Everything the guide needs is installed here so students never install tools
# on their own OS. It listens on nothing. The tool versions here do not change
# what is true about the targets — every value this lab asks for comes from the
# targets' own configuration and responses, not from a scanner's rating.
#
# TOOL NOTE: whatweb and nmap are both in Debian main. (nikto is in non-free,
# which debian:*-slim does not enable, so it cannot be installed here without
# editing sources.list — see L03_Solve_Record.md R2.) The pairing is deliberate:
# whatweb fingerprints from banners and nmap -sV fingerprints from probes, and
# on one of the targets they agree with each other and are both wrong. That is
# the lab.
FROM debian:12.5-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
      whatweb \
      nmap \
      dirb \
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
