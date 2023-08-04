# Pi Fan Controller

Raspberry Pi fan controller.

## Description

This repository provides scripts that can be run on the Raspberry Pi that will
monitor the core temperature and start the fan when the temperature reaches
a certain threshold.

To use this code, you'll have to install a fan. Instructions can be found in many
guides online (by everyone with different specificities):
- [Control Your Raspberry Pi Fan (and Temperature) with Python](https://howchoo.com/g/ote2mjkzzta/control-raspberry-pi-fan-temperature-python).
- [PWM Regulated Fan Based on CPU Temperature for Raspberry Pi](https://www.instructables.com/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/)
- [Circuit for temperature-controlled dual-fan Raspberry Pi case](https://scarff.id.au/blog/2021/circuit-for-temperature-controlled-dual-fan-raspberry-pi-case/)

## Running

First, clone the repo:

    git clone https://github.com/rigon/pi-fan-controller

Then, start the fan controller:

    cd pi-fan-controller
    ./fancontrol.py

You can run the command with:
 - `-p` to print the current status in every interval
 - `-d` to run indefinitely

You might need to install the dependency `RPi.GPIO` in your system (should be available by default):

    sudo apt-get install python3-rpi.gpio

Or with `pip`:

    sudo apt install python3-pip
    sudo pip3 install -r requirements.txt

## Running as service

Just run the install script:

    ./script/install

This script will start the fan controller as well.
