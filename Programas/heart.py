import math
from turtle import *

def heat(k):
    return 12*math.sin(k)**3
def heatb(k):
        return 12*math.cos(k)-5*\
        math.cos(2*k) - 2*\
                    math.cos(3*k)-\
                    math.cos(4*k)
speed(0)
bgcolor("black")
for i in range(10000):
      goto(heat(i)*20, heatb(i)*20)
      for j in range(5):
            color("#f73487")
            goto(0,0)
done()