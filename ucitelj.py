# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 15:21:07 2012

@author: jureso
"""
import mmap
from numpy  import *
from perceptron import *
from time import time

class Ucitelj:
    toleranca = 0.000001
    maxiter = 100
    def __init__(self, vhodi, izhodi):
        if isinstance(vhodi, str):
            print 'Nismo še tam'            
        self.n_vzorcev, self.dim_vzorcev = vhodi.shape
        self.n_vzorcev, self.n_razredov = izhodi.shape
    def nastavi_ucenje(self, n2):
        self.P = Perceptron(self.dim_vzorcev, n2, self.n_razredov)
            
    def ucenje(self, vhodi, izhodi):
        start = time()
        iter = 0
        delta_w = 1        
        while iter < self.maxiter:
            for i in range(0, self.n_vzorcev):
                delta_w = self.P.vzvratno_ucenje(vhodi[i,:],izhodi[i,:])
            if (delta_w < self.toleranca) and (iter > 0.1*self.maxiter):
                break            
            iter += 1
        print iter
        elapsed = (time()-start)
        return delta_w, iter, elapsed
    
    def testiraj(self, vhodi, izhodi):
        n_vzorcev, dim_vzorcev = vhodi.shape
        n_vzorcev, n_razredov = vhodi.shape
        uspesnost = zeros(n_razredov)
        stevilo_vzorcev = zeros(n_razredov)
        for i in range(0, n_vzorcev):
            razred = self.P.razvrsti(vhodi[i,:])
            stevilo_vzorcev[izhodi[i,:].argmax()] += 1
            if razred.argmax() == izhodi[i,:].argmax():
                uspesnost[izhodi[i,:].argmax()] += 1
        uspesnost = uspesnost/stevilo_vzorcev
        return uspesnost          
        
            

def main():
    #vhodi = array([[0, 1],[1, 0], [0,0], [1,1]])
    #izhodi = array([[1,0],[1,0],[0,1],[0,1]])
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
    U = Ucitelj(vhodi,izhodi)
    U.nastavi_ucenje(200)
    print 'start'
    dw, iteracij, cas = U.ucenje(vhodi,izhodi)
    print 'end'
    print dw
    print iteracij
    print cas
#    print U.P.razvrsti(vhodi[0,:])
#    print U.P.razvrsti(vhodi[1,:])
#    print U.P.razvrsti(vhodi[2,:])
#    print U.P.razvrsti(vhodi[3,:])
    
    print U.testiraj(vhodi,izhodi)

if __name__ == "__main__":
    main()