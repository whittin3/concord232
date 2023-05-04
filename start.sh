#!/usr/bin/with-contenv bashio
# CONFIG_PATH=/data/options.json
set -x
DEVICE_ARG="$(bashio::config 'device')"
concord232_server --serial "$DEVICE_ARG"