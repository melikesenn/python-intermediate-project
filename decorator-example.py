import math
import time
"""
import math
import time
def usalma(a,b):
    start = time.time()
    time.sleep(1)
    print(math.pow(a,b))
    finish = time.time()

    print("fonksiyon \n "+str(finish-start)+"saniye sürdü")

def faktoriyel(num):
    start = time.time()
    time.sleep(1)
    print(math.factorial(num))

    finish = time.time()
    print("fonksiyon" + str(finish - start) + "saniye sürdü")

usalma(2,3)
faktoriyel(3)

"""

#zamanı içerde değil dışarıda hesaplatma

import math
import time

def calculate_timee(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon süresi"+str(finish-start))

    return inner

@calculate_timee
def usalma(a,b):

    print(math.pow(a,b))


@calculate_timee
def faktoriyel(num):
    time.sleep(1)
    print(math.factorial(num))



usalma(2,3)
faktoriyel(2)
