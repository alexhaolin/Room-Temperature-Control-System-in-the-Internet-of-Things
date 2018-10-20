import threading
from random import uniform
from labs.module02 import SmtpClientConnector
from labs.common import SensorData
from time import sleep

class TempSensorEmulator():
    threadID   = 0
    lowVal     = 0
    highVal    = 0
    cruTemp    = 0
    alertDiff  = 0
    sleepcycle = 0
    sensorid   = 1
    enableEmulator = False
    isPrevTempSet  = False
    
    connector = SmtpClientConnector.SmtpClientConnector()
    sensordata = SensorData.SensorData() 

    
    def __init__(self, threadID, lowVal, highVal, curTemp):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.lowVal = lowVal
        self.highVal = highVal
        self.curTemp = curTemp
        self.sleepcycle = self.connector.pollCycleSecs
        self.enableEmulator = self.connector.enableEmulator
    
        
    def run(self):
        while True:
            if self.enableEmulator:
                
                self.curTemp = uniform(float(self.lowVal),float(self.highVal))
                self.sensordata.addValue(self.curTemp, 'Sensor'+str(self.sensorid))
                self.alertDiff = (self.sensordata.getMax() - self.sensordata.getMin())/6
                self.sensorid += 1;

                
               
                print('\n--------------------')
                print('New sensor readings:')
                print('  ' + str(self.sensordata))
                print('  Current Temperature: '+ str(round(self.curTemp, 3)))
                print('  Alert interval: [' + str(round(self.sensordata.getAverage()-self.alertDiff,3))+ \
                                            ',' + str(round(self.sensordata.getAverage()+self.alertDiff,3)) + ']' )
                print('  Average: ' + str(round(self.sensordata.getAverage(),3)))
            
                if self.isPrevTempSet == False:
                    self.prevTemp = self.curTemp
                    self.isPrevTempSet = True
                else:
                    if (abs(self.curTemp - self.sensordata.getAverage()) >= self.alertDiff):
                        print('|Alert|  Current temperature exceeds safe range: ' +str(round(abs(self.cruTemp-self.sensordata.getAverage()), 3))) 
                        self.connector.publishMessage('Exceptional sensor data [test]', str(self.sensordata))
                        print('         Data has been sent to a remote system.')        

            sleep(self.sleepcycle)