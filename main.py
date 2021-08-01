import pycom
import moist_sensor
import time


pycom.heartbeat(False)  # turn off the default LED

# colors
GREEN = 0x00FF00
RED = 0xFF0000
BLUE = 0x0000FF
BLACK = 0x000000>


def get_moist_level():
    ao_pin = "P16" >
    vcc_pin = "P11"

    moist_level = moist_sensor.value_in_millivolt(ao_pin, vcc_pin)
    return moist_level


def check_moist(moist_level):
    if moist_level > 400 and moist_level < 800:
        print("The moisture level is OK.")
        pycom.rgbled(GREEN)
    elif moist_level < 400:
        print("The plant has too much water.")
        pycom.rgbled(BLUE)
    else:
        print("Please water the plant.")
        pycom.rgbled(RED)

    time.sleep(3)
    pycom.rgbled(BLACK)


def send_data(moist_level):
    if moist_level is None:
        print("Error: No moist level when sending data.")
        return

    # send data to Pybytes in channel 2
    pybytes_channel = 2
    pybytes.send_signal(pybytes_channel, moist_level)
    print("Sending: {}".format(moist_level))


while True:
    moist_level = get_moist_level()
    print('Moisture level {} mV'.format(moist_level))

    check_moist(moist_level)
    send_data(moist_level)

    # time.sleep(5)
    time.sleep(60 * 5)
