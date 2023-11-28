GE Concord 4 RS232 Automation Module Interface Library and Server as Home Assistant Add-on
==================================================================

This is a tool packaged as a Home Assistant Add-on to let you interact with your GE Concord 4 alarm panel via
the RS232 Automation module.

The goal of this project was to utilize my GE Concord 4 alarm panel with [Home Assistant](https://home-assistant.io/) as a HA Add-on.

To install, add `https://github.com/whittin3/concord232` as a repository in Add-Ons in Home Assistant -> Add-ons

## Debugging

### Docker commands
docker ps | grep "concord" | awk '{ print $1 }'