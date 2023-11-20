# The 1085 Module is connected to 5V Reference so limit the movement of all linear actuators at 4.9V. No Input from the keyboard should be converted to pewer when the a2dc gives the reading of 4.9 V. 
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
def a2dc(channel_num):
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1015(i2c)
    if channel_num ==0:
        chan = AnalogIn(ads, ADS.P0)
    else if channel_num=1:
        chan = AnalogIn(ads, ADS.P1)
    else if channel_num==2:
        chan = AnalogIn(ads, ADS.P2)
    else if channel_num==3:
        chan = AnalogIn(ads, ADS.P3)
    print("{:>4}\t{:>4}".format('raw', 'v'))
    while True:
        print("{:>4}\t{:>4.3f}".format(chan.value, chan.voltage))
        time.sleep(0.1)
