#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

ON_THRESHOLD = 55  # (degrees Celsius) Fan kicks on at this temperature.
OFF_THRESHOLD = 45  # (degress Celsius) Fan shuts off at this temperature.
SLEEP_INTERVAL = 5  # (seconds) How often we check the core temperature.
GPIO_PIN = 17  # Which GPIO pin you're using to control the fan.

def get_temp():
    """Get the core temperature.

    Read file from /sys to get CPU temp in temp in C *1000

    Returns:
        int: The core temperature in thousanths of degrees Celsius.
    """
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        temp_str = f.read()

    try:
        return int(temp_str) / 1000
    except (IndexError, ValueError) as e:
        raise RuntimeError('Could not parse temperature output: {}'.format(e))

if __name__ == '__main__':
    # Validate the on and off thresholds
    if OFF_THRESHOLD >= ON_THRESHOLD:
        raise RuntimeError('OFF_THRESHOLD must be less than ON_THRESHOLD')

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.OUT)

    while True:
        temp = get_temp()
        value = GPIO.input(GPIO_PIN)

        # Start the fan if the temperature has reached the limit and the fan
        # isn't already running.
        # NOTE: `value` returns 1 for "on" and 0 for "off"
        if temp > ON_THRESHOLD and value == GPIO.LOW:
            GPIO.output(GPIO_PIN, GPIO.HIGH)  # Turn the fan on

        # Stop the fan if the fan is running and the temperature has dropped
        # to 10 degrees below the limit.
        elif value == GPIO.HIGH and temp < OFF_THRESHOLD:
            GPIO.output(GPIO_PIN, GPIO.LOW)  # Turn the fan off

        time.sleep(SLEEP_INTERVAL)
