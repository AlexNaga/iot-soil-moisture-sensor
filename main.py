import pycom
import moist_sensor
import time


pycom.heartbeat(False)  # turn off the default LED

AO_PIN = "P16"  # pin to read from
VCC_PIN = "P11"  # pin we want to turn on/off

# colors
GREEN = 0x00FF00
RED = 0xFF0000
BLUE = 0x0000FF
BLACK = 0x000000


def check_moist():
    time.sleep(3)
    moist_level = (moist_sensor.value_in_millivolt(AO_PIN, VCC_PIN) / 4.096)
    print('Moisture level {} mV'.format(moist_level))

    # The soil sensor values are between ~250-999 mV, where the lowest value means the plant is moist and 999 is dry
    if moist_level > 400 and moist_level < 600:
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


while True:
    check_moist()
    time.sleep(2)
    #time.sleep(60 * 5)
