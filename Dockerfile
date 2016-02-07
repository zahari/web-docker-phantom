FROM zahari/nginx-php

MAINTAINER Zahari Zahariev <zahari@outlook.com>

RUN rm -fr /www
ADD app /www
