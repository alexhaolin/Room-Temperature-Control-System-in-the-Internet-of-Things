import threading
from app.module import I2CSenseHatAdaptor

class SenseHat():
    rotateDeg = 270
    clearFlag = False
    
    def __init__(self):
        self.set_rotation(self.rotateDeg)
        
    def clear(self):
        self.clearFlag = True
        
    def get_humidity(self):
        test = threading.Thread(target=I2CSenseHatAdaptor.I2CSenseHatAdaptor().run())
        test.start()
        test.join()
    
    def get_temperature(self):
        return self.get_get_temperature_from_humidity()

    
    def get_get_temperature_from_humidity(self):
        # NOTE: This is just a sample
        return 21.4
    
    def get_temperature_from_pressure(self):
        return self.get_get_temperature_from_humidity()
    
    def get_pressure(self):
        # NOTE: This is just a sample
        return 31.5
    
    def set_rotation(self, rotateDeg):
        self.rotateDeg = rotateDeg
    
    def show_letter(self, val):
        print(val)
    
    def show_message(self, msg):
        print(msg) 