FROM debian:unstable

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y && \
 apt-get install build-essential debhelper devscripts equivs \
 software-properties-common -y
