# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 15:07:22 2012

@author: jureso
"""
import mmap
from numpy import *
f = open('/home/jureso/Documents/Perceptron/isolet5.data', 'r')
lines = 0
buf_size = 1024 * 1024
read_f = f.read # loop optimization
buf = read_f(buf_size)
while buf:
    lines += buf.count('\n')
    buf = read_f(buf_size)


a = zeros((lines,618))
vhodi = zeros((lines, 617))
izhodi = zeros((lines, 26))
f.close()
f = open('/home/jureso/Documents/Perceptron/isolet5.data', 'r')
i = 0

while (i >= 0):
    s1 = f.readline()
    if len(s1) == 0:
        break
    a[i,:] = fromstring(s1[0:-2], sep=', ')
    i +=1
    
for i in range(0,lines):
    vhodi[i,:] = a[i,0:-1]
    izhodi[i,a[i,-1]-1] = 1