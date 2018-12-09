import sys,os
sys.path.append('/home/pi/workspace/iot-device/Lab1/iot-device/apps')
from app.common import ActuatorData
from app.module import SenseHatLedActivator

class TempActuatorEmulator(object):

    actuatordata = ActuatorData.ActuatorData()
    raisetemp = None
    lowertemp = None

    def __init__(self):
        self.raisetemp = "raise"
        self.lowertemp = "lower"
        
        
    def processMessage(self, actuatordata):
        if(actuatordata != self.actuatordata):
            self.actuatordata = actuatordata
            
        if(self.actuatordata.getCommand() == self.raisetemp):
            #send notification to GPIO
            ledactivator = SenseHatLedActivator.SenseHatLedActivator()
            ledactivator.setEnableLedFlag(True)
            ledactivator.setDisplayMessage("Set temperature to: " + self.actuatordata.getValue() + \
                                            "Turn on the heater, or you will freeze to death.")
            print("Set temperature to: " + self.actuatordata.getValue())
            ledactivator.run()

        if(self.actuatordata.getCommand() == self.lowertemp):
            #send notification to GPIO
            ledactivator = SenseHatLedActivator.SenseHatLedActivator()
            ledactivator.setEnableLedFlag(True)
            ledactivator.setDisplayMessage("Set temperature to: " + self.actuatordata.getValue() + \
                                           "Save the earth, turn off the heater.")
            print("Set temperature to: " + self.actuatordata.getValue())
            ledactivator.run()
        
    
    
        
            