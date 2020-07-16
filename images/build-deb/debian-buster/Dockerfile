FROM debian:buster-backports

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y && \
 apt-get install build-essential debhelper/buster-backports \
 devscripts equivs software-properties-common -y
