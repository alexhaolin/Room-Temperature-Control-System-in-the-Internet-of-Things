
import time

from labs.module01 import SystemPerformanceAdaptor

thread1 = SystemPerformanceAdaptor.SystemPerformanceAdaptor(1,"Thread-1",1)

print("Starting system performance app daemon thread...")
thread1.start()

while (True):
    time.sleep(5)
    pass