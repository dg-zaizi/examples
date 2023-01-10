FROM ubuntu:latest

ARG aws_zip="awscliv2.zip"
ARG aws_url="https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip"

RUN apt-get update \
  && apt-get upgrade --yes \
  && apt-get install --yes --no-install-recommends \
    ca-certificates curl unzip \
  && curl --location "${aws_url}" --output "${aws_zip}" \
  && unzip "${aws_zip}" \
  && ./aws/install \
  && rm -fv "${aws_zip}" \
  && apt-get purge --yes curl unzip \
  && apt-get autoclean \
  && apt-get autoremove --yes \
  && rm -rf /var/lib/apt/lists/*
