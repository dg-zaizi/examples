#!/usr/bin/env bash
HOST_DIR="$1"

if [[ $# -lt 1 ]]; then
  HOST_DIR="${PWD:?}"
fi

CONTAINER_MOUNT_DIR=/host

docker run \
  --rm \
  --tty \
  --interactive \
  --mount "type=bind,source=${HOST_DIR},target=${CONTAINER_MOUNT_DIR},readonly" \
  --mount "type=bind,source=${HOME}/.aws/config,target=/root/.aws/config,readonly" \
  --mount "type=bind,source=${HOME}/.aws/credentials,target=/root/.aws/credentials,readonly" \
  --workdir "${CONTAINER_MOUNT_DIR}" \
  --entrypoint 'bash' \
  "ubuntu-aws:0.0.1" \
  "${@:2}"
