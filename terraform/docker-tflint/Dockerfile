FROM ubuntu:latest

RUN apt update \
  && apt install --yes curl unzip \
  && curl --location --remote-name \
    https://raw.githubusercontent.com/terraform-linters/tflint/master/install_linux.sh \
  && chmod +x install_linux.sh \
  && ./install_linux.sh
