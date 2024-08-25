FROM python:3-alpine

LABEL BASEDON="https://git.dartmouth.edu/d41259m/exabgplab"
LABEL AUTHOR="@patrikh"

RUN pip install --upgrade pip
RUN pip install exabgp

# https://www.howtoforge.com/linux-mkfifo-command/
RUN mkfifo /run/exabgp.in && \
    mkfifo /run/exabgp.out && \
    chmod 666 /run/exabgp.in && \
    chmod 666 /run/exabgp.out

#RUN exabgp --fi > /usr/local/etc/exabgp/exabgp.env

COPY exabgp.env /usr/local/etc/exabgp/exabgp.env

COPY exabgp.conf /etc/exabgp.conf

COPY start.sh /start.sh

COPY print.py /handlers/print.py

RUN chmod 777 /start.sh

CMD ["/start.sh"]
