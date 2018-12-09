import sys,os
sys.path.append('/home/pi/workspace/iot-device/Lab1/iot-device/apps')

from app.module import TempSensorAdaptor
import threading



test = threading.Thread(target=TempSensorAdaptor.TempSensorAdaptor().run())
test.start()
test.join()
