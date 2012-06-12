# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 15:21:07 2012

@author: jureso
"""

from numpy  import *
from perceptron import *

class Ucitelj:
    toleranca = 0.0000001
    maxiter = 100000
    def __init__(self, vhod, izhod):
        if isinstance(vhod, str):
            print 'Nismo še tam'            
        self.n_vzorcev, self.dim_vzorcev = vhodi.shape
        self.n_vzorcev, self.n_razredov = vhodi.shape
    def nastavi_ucenje(self, n2):
        self.P = Perceptron(self.dim_vzorcev, n2, self.n_razredov)
            
    def ucenje(self, vhodi, izhodi):
        iter = 0        
        while iter < maxiter:
            
            iter += 1
            
        
            

def main():
    vhodi = array([[0, 1],[1, 0], [0,0], [1,1]])
    izhodi = array([[1,0],[1,0],[0,1],[0,1]])
    U = Ucitelj(vhodi,izhodi)
    

if __name__ == "__main__":
    main()