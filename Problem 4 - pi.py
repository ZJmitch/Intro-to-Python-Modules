#Justin Mitchell
#2/21/2021

#Problem 4 approximation for pi

import math

def pi():
    pi = 0
    n = 4
    d = 1
#The range can be increased to 100,000,000 to get a closer answer but the script takes too long to run
    for i in range(1,1000):
        a = 2 * (i%2) - 1
        pi += a * n / d
        d+= 2
        print(pi , math.pi)
pi()


#Program calculates an approximation for pi, increasing the range will get a closer answer. Program also prints the value for math.pi next to it.
