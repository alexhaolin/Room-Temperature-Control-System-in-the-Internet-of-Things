import smbus
import threading
from time import sleep

import sys,os
sys.path.append('/home/pi/workspace/iot-device/Lab1/iot-device/apps')

from labs.common import ConfigUtil
from labs.common import ConfigConst
from sense_hat import SenseHat

i2cBus = smbus.SMBus(1)

acc = None
mag = None
pre = None
hum = None
temp = None

enableControl = 0x2D
enableMeasure = 0x08
enableEmulator = False

accAddr = 0x1C
magAddr = 0x6A
preAddr = 0x5C
humAddr = 0x5F

begAddr   = 0x28
totBytes  = 6

DEFAULT_RATE_IN_SEC = 5
rateInSec = 0

sense = None


class I2CSenseHatAdaptor(threading.Thread):
        
        
        def __init__(self):
            super(I2CSenseHatAdaptor, self).__init__()
            
            
            self.config = ConfigUtil.ConfigUtil(ConfigConst.DEFAULT_CONFIG_FILE_NAME)
            self.config.loadConfig()
            flag= self.config.getProperty(ConfigConst.DEVICE, ConfigConst.ENABLE_EMULATOR_KEY)
            self.enableEmulator = flag
            self.rateInSec = DEFAULT_RATE_IN_SEC
            
            print('Configuration data...\n' + str(self.config))
            
            self.initI2CBus()
        
        def initI2CBus(self):
            print("Initializing I2C bus and enabling I2C addresses...")
            
            i2cBus.write_byte_data(accAddr, enableControl, enableMeasure)
            i2cBus.write_byte_data(magAddr, enableControl, enableMeasure)
            i2cBus.write_byte_data(preAddr, enableControl, enableMeasure)
            i2cBus.write_byte_data(humAddr, enableControl, enableMeasure)
            
        
            self.acc = i2cBus.read_i2c_block_data(accAddr, begAddr, totBytes)
            self.mag = i2cBus.read_i2c_block_data(magAddr, begAddr, totBytes)
            self.pre = i2cBus.read_i2c_block_data(preAddr, begAddr, totBytes)
            self.hum = i2cBus.read_i2c_block_data(humAddr, begAddr, totBytes)
        
        def displayAccelerometerData(self):
            print("Accelero: ")
            print(self.acc)
            
        def displayMagnetometerData(self):
            print("Magneto: ")
            print(self.mag)
            
        def displayPressuremeterData(self):
            print("Pressure: ")
            print(self.pre)
            
        def displayHumiditymeterData(self):
            print("Humidity: ")
            print(self.hum)
            
            
            
        def run(self):
            while True:
                if self.enableEmulator:
                    print("----------------------")
                    self.displayAccelerometerData()
                    self.displayMagnetometerData()
                    self.displayPressuremeterData()
                    self.displayHumiditymeterData()
                
                sleep(self.rateInSec)
            
    
    
    
    
    
    
    