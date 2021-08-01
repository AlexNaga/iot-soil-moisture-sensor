from machine import ADC, Pin
import time


def value_in_millivolt(pin_in, pin_out):
    """
    Parameters:
        pin_in  : AO pin number to read from.
        pin_out : VCC pin number to turn on/off.

    Returns: Soil moisture value in millivolt (mV) between ~250-999 mV,
             where 250 means the plant is moist and 999 is dry.
    """

    adc = ADC()
    apin = adc.channel(pin=pin_in, attn=ADC.ATTN_11DB)
    pin_out = Pin(pin_out, mode=Pin.OUT, pull=Pin.PULL_DOWN)
    pin_out.value(1)

    time.sleep(2)

    volts = apin.value()
    pin_out.value(0)

    time.sleep(2)

    volt_reference = 4.096
    return volts / volt_reference
