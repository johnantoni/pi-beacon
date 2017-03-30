## terminal login details:

    username: pi
    password: raspberry

# ----- install software -----

## update and upgrade raspberry pi software

    sudo apt-get update
    sudo apt-get upgrade

## install pigpiod

    wget abyz.co.uk/rpi/pigpio/pigpio.zip
    unzip pigpio.zip
    cd PIGPIO
    make
    sudo make install
    cd ~

## install bluetooth libraries

    sudo apt-get install libusb-dev
    sudo apt-get install libglib2.0-dev --fix-missing
    sudo apt-get install libudev-dev
    sudo apt-get install libical-dev
    sudo apt-get install libreadline-dev
    sudo apt-get install libdbus-glib-1-dev
    sudo apt-get install bluetooth bluez blueman
    sudo apt-get install python-bluez

# ----- start servo daemon & bluetooth dongle -----

you'll need to run these every time you start the raspberry pi

run pigpiod daemon

    sudo pigpiod

startup the bluetooth dongle

    sudo hciconfig hci0 up

# ----- how to get the pigpiod daemon & bluetooth dongle running every time automatically

## open the system crontab file

    sudo crontab -e

## first time it'll ask you which editor you want to use, select /bin/nano (2)

## add these two lines:

    @reboot sudo pigpiod
    @reboot sudo hciconfig hci0 up

then press ctrl-x and press 'y' to save your changes

## reboot the pi

    sudo shutdown -r now

## when it reboots you should be able to run the servo or scan for beacons without having to startup those daemons manually
