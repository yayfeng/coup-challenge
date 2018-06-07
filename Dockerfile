FROM ubuntu:16.04

USER root

RUN ln -sf /usr/share/zoneinfo/Etc/UTC /etc/localtime

RUN apt-get update && \
    apt-get install --assume-yes python-pip && \
    pip install --upgrade pip==9.0.3 && \
    pip install nose

RUN useradd --create-home --home-dir /opt/service --shell /bin/bash service

WORKDIR /opt/service/

COPY VERSION \
     requirements.txt \
     apt-requirements.txt \
     ./

RUN apt-get update && \
    apt-get install -y $(cat apt-requirements.txt) &&\
    pip install \
        --no-cache-dir \
        --no-deps \
        -r requirements.txt

COPY coup_challenge_app coup_challenge_app
COPY setup.py ./

RUN pip install --no-deps -e .

RUN chown -R service:service /opt/service
USER service

ENTRYPOINT [ "coup-challenge-app" ]