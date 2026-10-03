# Legacy office file server, reachable over SSH (22/tcp).
# OpenSSH version is fixed by the pinned base image. Note that nmap's -sV
# strings for OpenSSH carry a distro suffix that varies between nmap builds,
# so treat any version it reports here as approximate.
FROM alpine:3.20.3

RUN apk add --no-cache openssh \
 && ssh-keygen -A \
 && adduser -D -g "" fileuser \
 && echo 'fileuser:marsh-lantern-oak-51' | chpasswd \
 && sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D", "-e"]
