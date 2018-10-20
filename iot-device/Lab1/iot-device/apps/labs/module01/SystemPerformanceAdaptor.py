
import psutil
import time
from test.test_enum import threading

class SystemPerformanceAdaptor(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    
    def run(self):
        while True:
            if 1:
                print('\n--------------------')
                print('New system performance readings:')
                print(' ' + str(psutil.cpu_stats()))
                print(' ' + str(psutil.virtual_memory()))
#                print(' ' + str(psutil.sensors_temperatures(False)))
            time.sleep(5)
    

        