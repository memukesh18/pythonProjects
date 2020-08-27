#!/usr/bin/python

import statistics as s

example_list = [5,4,2,4,5,3,4,4,7,5,9,3]

x = s.mean(example_list)
y = s.median(example_list)
z = s.mode(example_list)
d = s.stdev(example_list)
v = s.variance(example_list)


print('mean:',x)
print('median:',y)
print('mode:',z)
print('stdDev:',d)
print('variance',v)



