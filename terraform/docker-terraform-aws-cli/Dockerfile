FROM ubuntu:latest

ARG tf_version
ARG tf_zip="terraform_${tf_version}_linux_amd64.zip"
ARG tf_url="https://releases.hashicorp.com/terraform/${tf_version}/${tf_zip}"
ARG aws_zip="awscliv2.zip"
ARG aws_url="https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip"

RUN apt-get update \
  && apt-get upgrade --yes \
  && apt-get install --yes --no-install-recommends \
    ca-certificates curl unzip \
  && curl --location --remote-name "${tf_url}" \
  && unzip "${tf_zip}" \
  && rm -fv "${tf_zip}" \
  && mv terraform /bin/ \
  && curl --location "${aws_url}" --output "${aws_zip}" \
  && unzip "${aws_zip}" \
  && ./aws/install \
  && rm -fv "${aws_zip}" \
  && apt-get purge --yes curl unzip \
  && apt-get autoclean \
  && apt-get autoremove --yes \
  && rm -rf /var/lib/apt/lists/*
