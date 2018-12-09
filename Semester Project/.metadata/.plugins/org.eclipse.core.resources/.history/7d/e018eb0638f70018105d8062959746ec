import sys,os
sys.path.append('/home/pi/workspace/iot-device/Lab1/iot-device/apps')

from labs.module04 import I2CSenseHatAdaptor
import threading

test = threading.Thread(target=I2CSenseHatAdaptor.I2CSenseHatAdaptor().run())
test.start()
test.join()
