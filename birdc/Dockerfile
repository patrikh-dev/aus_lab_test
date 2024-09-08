FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# https://pkg.labs.nic.cz/doc/?project=bird

RUN apt update && \
    apt -y install apt-transport-https ca-certificates wget

RUN wget -O /usr/share/keyrings/cznic-labs-pkg.gpg https://pkg.labs.nic.cz/gpg && \
    echo "deb [signed-by=/usr/share/keyrings/cznic-labs-pkg.gpg] https://pkg.labs.nic.cz/bird2 bookworm main" > /etc/apt/sources.list.d/cznic-labs-bird2.list

RUN apt-get update && \
    apt install -y iproute2 && \
    apt -y install bird2=2.15.1-cznic.1~bookworm

RUN rm -rf /var/lib/apt/lists/*

#RUN sed -i 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/' /etc/sysctl.conf && sed -i 's/#net.ipv6.conf.all.forwarding=1/net.ipv6.conf.all.forwarding=1/' /etc/sysctl.conf && sysctl -p

COPY bird.conf /etc/bird/bird.conf
