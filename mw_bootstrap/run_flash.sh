#!/bin/sh
flash --hostname media-warrior \
      --userdata mw-user-data.yaml \
      --bootconf mw_config.txt \
      hypriotos-rpi-v1.9.0.img
