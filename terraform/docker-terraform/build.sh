#!/usr/bin/env bash
TERRAFORM_VERSION="$1"

if [[ $# -lt 1 ]]; then
  TERRAFORM_VERSION="$(curl \
      --location \
      --silent \
      https://releases.hashicorp.com/terraform \
    | grep -Eo '^\s*<a [^>]*>terraform_[0-9]+\.[0-9]+\.[0-9]+<' \
    | grep -Eo 'terraform_[0-9]+\.[0-9]+\.[0-9]+' \
    | grep -Eo '[0-9]+\.[0-9]+\.[0-9]+' \
    | awk -F "." '{printf "%03d.%03d.%03d %s\n", $1, $2, $3, $0}' \
    | sort \
    | tail -1 \
    | cut -d " " -f 2)"
fi

printf 'TERRAFORM_VERSION=%s\n' "${TERRAFORM_VERSION}"

IMAGE="ubuntu-terraform:${TERRAFORM_VERSION}"

docker rmi "${IMAGE}"
docker build \
  --build-arg "tf_version=${TERRAFORM_VERSION}" \
  --tag "${IMAGE}" \
  .
