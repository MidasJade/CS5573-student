# Developer utility box.
#
# Serves a small status/metrics directory over HTTP on port 9090. No
# authentication is configured on it. Python's http.server is used because it
# is what someone would reach for to "just expose this quickly."
FROM python:3.12.3-slim

COPY www /srv/www
WORKDIR /srv/www

EXPOSE 9090
CMD ["python3", "-m", "http.server", "9090", "--bind", "0.0.0.0", "--directory", "/srv/www"]
