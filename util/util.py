import numpy
import time

def wait():
   wait_time = abs(numpy.random.normal(4, 1, 1))
   time.sleep(wait_time)
