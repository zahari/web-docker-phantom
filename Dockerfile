FROM tutum/apache-php

MAINTAINER Zahari Zahariev <zahari@outlook.com>

RUN apt-get update && \
    apt-get install -yq git && \
    rm -rf /var/lib/apt/lists/*
RUN rm -fr /app
ADD app/ /app
#RUN composer self-update && \
#    composer install
