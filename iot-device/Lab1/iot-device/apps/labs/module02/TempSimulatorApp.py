from labs.module02 import TempSensorEmulator
from test.test_enum import threading


test = threading.Thread(target=TempSensorEmulator.TempSensorEmulator(0,0,30,0).run())
test.start()
test.join()

