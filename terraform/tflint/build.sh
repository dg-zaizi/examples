#!/usr/bin/env bash
IMAGE_VERSION=0.0.1
IMAGE="ubuntu-tflint:${IMAGE_VERSION}"

docker rmi "${IMAGE}"
docker build --tag "${IMAGE}" .
