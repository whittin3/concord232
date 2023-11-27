#!/usr/bin/with-contenv bashio

CONFIG_PATH=/data/options.json
DEVICE_ARG="$(bashio::config 'device')"
DEBUG_ARG="$(bashio::config 'debug')"
declare -a OPTIONAL_ARG_ARRAY=()
if $DEBUG_ARG; then
  OPTIONAL_ARG_ARRAY+=('--debug true');
fi
OPTIONAL_ARGS=$(IFS=" "; echo "${OPTIONAL_ARG_ARRAY[*]}")
concord232_server --serial "$DEVICE_ARG" "$OPTIONAL_ARGS"