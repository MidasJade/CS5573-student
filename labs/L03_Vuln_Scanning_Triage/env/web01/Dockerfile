# Small-office intranet web server.
#
# Built rather than using the stock nginx image directly, for one reason: the
# HTTP basic-auth password file is generated HERE, at build time, with the
# official htpasswd tool. Shipping a pre-computed hash in the repo would mean
# trusting a hash nobody can verify; generating it in the image means it is
# correct by construction on every machine.
FROM nginx:1.25.3

RUN apt-get update \
 && apt-get install -y --no-install-recommends apache2-utils \
 && htpasswd -bcB /etc/nginx/.htpasswd admin admin \
 && chmod 644 /etc/nginx/.htpasswd \
 && apt-get purge -y apache2-utils \
 && apt-get autoremove -y \
 && rm -rf /var/lib/apt/lists/*
