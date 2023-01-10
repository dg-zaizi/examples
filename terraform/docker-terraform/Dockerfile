FROM ubuntu:latest

ARG tf_version
ARG tf_zip="terraform_${tf_version}_linux_amd64.zip"
ARG tf_url="https://releases.hashicorp.com/terraform/${tf_version}/${tf_zip}"

RUN apt-get update \
  && apt-get upgrade --yes \
  && apt-get install --yes --no-install-recommends \
    ca-certificates curl unzip \
  && curl --location --remote-name "${tf_url}" \
  && unzip "${tf_zip}" \
  && rm -fv "${tf_zip}" \
  && mv terraform /bin/ \
  && apt-get purge --yes curl unzip \
  && apt-get autoclean \
  && apt-get autoremove --yes \
  && rm -rf /var/lib/apt/lists/*
