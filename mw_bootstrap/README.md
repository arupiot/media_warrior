# media_warrior bootstrap framework

This directory includes all the files to be used to bootstrap the installation of the Raspberry Pi SD card image 
for the Media Warrior cloud connected sound and light player.

## Hypriot

* Get latest version of the Hypriot linux image from the [Hypriot github repo](https://github.com/hypriot/image-builder-rpi/releases).
* Download and install the `flash` script and install its prerequisites as indicated in the [flash github repo](https://github.com/hypriot/flash).
* Run the flash script to bake the Hypriot linux image into the SD card with the following command
```bash
flash --hostname HOSTNAME --ssid WIFISSID --password WIFIPASSWORD--userdata mw-user-data.yaml --bootconf mw_config.txt hypriotos.img
```
and making sure that you've changed the Wi-Fi ssid (WIFISSID) and password (WIFIPASSWORD) to your local Wi-Fi configuration and HOSTNAME to the
name you'd like to use for your media_warrior host.

## Fabric

TO DO


