# -*- coding: utf-8 -*-
import math

def ca(r):
    c = math.pi * (r ** 2)
    return round(c, 5)

rad = int(input('Please input Radius:'))

print(ca(rad))