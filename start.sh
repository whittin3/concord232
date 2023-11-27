#!/usr/bin/with-contenv bashio

CONFIG_PATH=/data/options.json
DEVICE_ARG="$(bashio::config 'device')"
DEBUG_ARG="$(bashio::config 'debug')"
declare -a ARG_ARRAY=()
ARG_ARRAY+=('--serial');
ARG_ARRAY+=("$DEVICE_ARG");
if $DEBUG_ARG; then
  ARG_ARRAY+=('--debug');
fi

concord232_server "${ARG_ARRAY[@]}"