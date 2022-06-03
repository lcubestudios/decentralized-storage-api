FROM php:8.1-apache

RUN apt update && apt upgrade -y
RUN apt install -y git zip nano python3 python3-pip build-essential libssl-dev libffi-dev python3-dev wget
RUN cd /tmp/ && wget https://go.dev/dl/go1.18.2.linux-amd64.tar.gz && rm -rf /usr/local/go && tar -C /usr/local -xzf go1.18.2.linux-amd64.tar.gz
RUN export PATH=$PATH:/usr/local/go/bin

WORKDIR /var/www/html/

COPY . . 
RUN pip3 install -r requirements.txt
RUN a2enmod cgi 

EXPOSE 80

