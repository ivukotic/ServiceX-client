FROM python:3.7-slim 

RUN apt-get -y update
RUN apt-get -y install vim wget dnsutils

COPY .servicex /
COPY run.sh /
COPY test.py /
RUN chmod +x /run.sh
CMD ["/run.sh"]