FROM python:3.8

ENV TERRAFORM_VERSION=1.0.8

RUN apt-get update && \
    apt-get install curl ca-certificates git openssl unzip wget && \
    cd /tmp && \
    wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/bin && \
    rm -rf /tmp/* && \
    rm -rf /var/cache/apk/* && \
    rm -rf /var/tmp/*

ADD requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /opt/working