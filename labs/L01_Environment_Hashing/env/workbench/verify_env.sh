#!/bin/sh
# CS5573 L01 environment self-check. This is the GATE: if you can run this and
# see "ENVIRONMENT OK" at the bottom, your Docker toolchain works and you are
# ready for the rest of the course. It reports nothing you submit — it proves
# your setup works.
echo "CS5573 L01 — environment check"
echo "--------------------------------"
echo "container hostname : $(hostname)"
echo "sha256sum          : $(command -v sha256sum || echo MISSING)"
echo "md5sum             : $(command -v md5sum || echo MISSING)"
echo "openssl            : $(openssl version 2>/dev/null || echo MISSING)"
echo "grep               : $(command -v grep || echo MISSING)"
echo "find               : $(command -v find || echo MISSING)"
echo "workbench folders  :"
ls -1 /workbench | sed 's/^/                     /'
echo "--------------------------------"
echo "ENVIRONMENT OK — if you can read this line inside the container,"
echo "your Docker environment is working. You are ready for Week 2."
