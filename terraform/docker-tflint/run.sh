#!/usr/bin/env bash
if [[ $# -lt 1 ]]; then
  printf 'Usage: host_mount_dir [OPTION or FILE or DIR...]\n'
  exit 1
fi

CONTAINER_MOUNT_DIR=/host

docker run \
  --rm \
  --tty \
  --interactive \
  --mount "type=bind,source=${1},target=${CONTAINER_MOUNT_DIR},readonly" \
  --workdir "${CONTAINER_MOUNT_DIR}" \
  --entrypoint 'tflint' \
  ubuntu-tflint:0.0.1 \
  "${@:2}"
