FROM python:3.8-slim 

RUN apt-get -y update
RUN apt-get -y install vim wget dnsutils
RUN python -m pip install minio

COPY servicex.yaml test.py run.sh /
RUN chmod +x /run.sh
CMD ["/run.sh"]