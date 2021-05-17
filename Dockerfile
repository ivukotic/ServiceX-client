FROM python:3.8-slim 

RUN apt-get -y update
RUN apt-get -y install vim wget dnsutils
RUN python -m pip install minio
RUN python -m pip install servicex_clients
RUN python -m pip install coffea[servicex]


COPY servicex.yaml test*.py run.sh /
CMD ["/run.sh"]