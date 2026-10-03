# CS5573 L01 — the "workbench" container.
# A tiny, deterministic Linux workbench for the Week-1 environment gate and the
# CLI + hashing warmup. Base is pinned so every student gets identical tools.
#
# What you find in this lab depends only on the FILES copied in below, never on
# the image's tool versions — hashing is deterministic on file bytes, so results
# are identical on every machine as long as those files are byte-identical (see
# the .gitattributes in this folder, which forces no EOL translation on
# files/**).
FROM debian:12.5-slim

LABEL course="CS5573" lab="L01" \
      purpose="environment gate + CLI/hashing warmup"

# coreutils (sha256sum/md5sum), grep, findutils, bash are already in the base.
# openssl + file are the only extras (openssl gives students `openssl dgst`;
# file is used in the guide to show that an extension does not define a type).
RUN apt-get update \
 && apt-get install -y --no-install-recommends openssl file \
 && rm -rf /var/lib/apt/lists/*

# Student fixtures. COPY preserves bytes exactly (no EOL conversion at build).
COPY files/ /workbench/

# Environment self-check (the gate). It reports nothing you submit — it exists
# to prove your Docker toolchain works.
COPY verify_env.sh /usr/local/bin/verify_env.sh
RUN chmod +x /usr/local/bin/verify_env.sh

WORKDIR /workbench
CMD ["sleep", "infinity"]
