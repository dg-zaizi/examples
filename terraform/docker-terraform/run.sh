#!/usr/bin/env bash
HOST_DIR="$1"

if [[ $# -lt 1 ]]; then
  HOST_DIR="${PWD:?}"
fi

TF_IMAGE_VERSION="$(
  docker images --filter "reference=ubuntu-terraform" --format "{{.Tag}}"|sort|tail -1
)"

CONTAINER_MOUNT_DIR=/host

docker run \
  --rm \
  --tty \
  --interactive \
  --mount "type=bind,source=${HOST_DIR},target=${CONTAINER_MOUNT_DIR},readonly" \
  --workdir "${CONTAINER_MOUNT_DIR}" \
  --entrypoint 'terraform' \
  "ubuntu-terraform:${TF_IMAGE_VERSION:?}" \
  "${@:2}"
