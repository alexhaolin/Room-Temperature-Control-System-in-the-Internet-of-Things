from datetime import datetime
 
 
class SensorData():
    timeStamp   = None
    name        = 'Not set'
    current  = 0
    min      = 0
    max      = 0
    average  = 0
    total    = 0
    sampleCount = 0
     
    def _init_(self):
        self.timeStamp = str(datetime.now())
        self.sampleCount = 0
     
    def addValue(self, newval, name):
        self.sampleCount += 1
        self.timeStamp = str(datetime.now())
        self.name = name
        self.current = newval
        self.total = self.current + self.total
        self.average = self.total / self.sampleCount

        if (self.current < self.min):
            self.min = self.current
             
        if (self.current > self.max):
            self.max = self.current
    
            
     
    def getAverage(self):
        return self.average
     
    def getMax(self):
        return self.max
     
    def getMin(self):
        return self.min
     
    def getCurrent(self):
        return self.current
     
    def setName(self,name):
        self.name = name
     
    def __str__(self):
        customStr = \
                   str(self.name + ':' + \
                   '\n\tTime:       ' + self.timeStamp + \
                   '\n\tCurrent:    ' + str(round(self.current,3)) + \
                   '\n\tAverage:   ' + str(round(self.average,3)) + \
                   '\n\tSamples:   ' + str(self.sampleCount) + \
                   '\n\tMin:           ' + str(round(self.min,3)) + \
                   '\n\tMax:          ' + str(round(self.max,3)))
         
        return customStr
