import sys,os
sys.path.append('/home/pi/workspace/iot-device/Lab1/iot-device/apps')

from labs.module03 import TempSensorAdaptor
import threading



test = threading.Thread(target=TempSensorAdaptor.TempSensorAdaptor().run())
test.start()
test.join()
