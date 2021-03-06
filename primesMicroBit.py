# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 20:19:42 2018
Copyright James Robinson 2018
All Rights Reserved
"""

import math
from microbit import *

doMod = True

def isPrime(num):                                   #Prime number finding function
                                                    #Note: faster then converting it into a loop    
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):    
        if num % i == 0:
            return False
        
    return True

i = 1
x = 1

while 1 < 2:
    
    if isPrime(i):
        x = x + 1
        
        if doMod == True:
            if x % 1000 == 0:
                display.scroll(str(i))
        
        else:
            display.scroll(str(i))
        
    i = i + 1
