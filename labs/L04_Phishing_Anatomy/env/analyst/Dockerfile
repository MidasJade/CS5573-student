# L04 analyst workstation.
#
# Deliberately installs nothing. Everything this lab needs is either in Python's
# standard library (the email, base64 and hashlib modules) or in the base image's
# coreutils (sha256sum, cat, grep). No apt-get, so no package availability to go
# wrong on the night.
FROM python:3.12.3-slim

# The parser is baked into the image rather than bind-mounted, so it is present
# even if a host path misbehaves. The copy in env/analyst/ is the editable one.
COPY eml.py /opt/eml.py
RUN chmod 0755 /opt/eml.py

# A working directory students own, separate from the read-only /cases mount.
RUN mkdir -p /workbench
WORKDIR /workbench

# Convenience: `eml` on PATH, so the guide's commands stay short.
RUN printf '#!/bin/sh\nexec python3 /opt/eml.py "$@"\n' > /usr/local/bin/eml \
    && chmod 0755 /usr/local/bin/eml
