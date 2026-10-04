# Internal application front end.
#
# A Python http.server serving a small static app. The Server: response header
# is set from SERVER_BANNER (see docker-compose.yml) rather than reporting the
# real runtime — a configuration the operators copied from an older runbook and
# never revisited. Nothing here is labeled; any conclusion about what this host
# runs has to come from evidence other than the banner.
FROM python:3.12.3-slim

COPY server.py /srv/server.py
COPY www /srv/www

EXPOSE 8080
CMD ["python3", "/srv/server.py"]
