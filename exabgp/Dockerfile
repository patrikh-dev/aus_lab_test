FROM ubuntu:22.04

RUN apt update && \
    apt -y install python3-pip net-tools wget mrtparse vim && \
    rm -rf /var/lib/apt/lists/* && apt clean

RUN pip3 install --upgrade pip && \
    pip3 install exabgp==4.2.22

COPY exabgp.cfg /etc/exabgp/exabgp.cfg

COPY bgp.py /etc/exabgp/bgp.py

#ENTRYPOINT "exabgp -f /etc/exabgp/exabgp.cfg"
