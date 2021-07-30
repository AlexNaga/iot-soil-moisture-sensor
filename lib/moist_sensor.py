from machine import ADC, Pin
import time


def value_in_millivolt(pin_in, pin_out):
    adc = ADC()
    apin = adc.channel(pin=pin_in, attn=ADC.ATTN_11DB)
    pin_out = Pin(pin_out, mode=Pin.OUT, pull=Pin.PULL_DOWN)
    pin_out.value(1)

    time.sleep(2)

    volts = apin.value()
    pin_out.value(0)

    time.sleep(2)

    return volts
