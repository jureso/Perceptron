# -*- coding: utf-8 -*-
"""
Copyright (c) 2012 University of Ljubljana, Faculty of Electrical Engineering.
All rights reserved. Licensed under the Academic Free License version 3.0.

@author Jure Sokolić, jure.sokolic@gmail.com
@version 15/06/2012

"""

from numpy  import *
from perceptron import *
from time import time

class Ucitelj:
    toleranca = 0.000001
    maxiter = 300
    def __init__(self, arg1, arg2, arg3): #stevilo znacilk, srednje plasti in razredov ali pa matrike w
        self.P = Perceptron(arg1, arg2, arg3)
        
    def parametri(self, toleranca, maxiter, beta):
        self.toleranca = toleranca
        self.maxiter = maxiter
        self.P.beta = beta
    
    def ucenje(self, vhodi, izhodi):
        start = time()
        iter = 0
        delta_w = 1        
        while iter < self.maxiter:
            for i in range(0, vhodi.shape[0]):
                delta_w = self.P.vzvratno_ucenje(vhodi[i,:],izhodi[i,:])
            if (delta_w < self.toleranca) and (iter > 0.1*self.maxiter):
                break            
            iter += 1
        elapsed = (time()-start)
        return delta_w, iter, elapsed
        
    # razvrsti vse vzorce in vrne statistiko
    def testiraj(self, vhodi, izhodi):
        n_vzorcev, dim_vzorcev = vhodi.shape
        n_vzorcev, n_razredov = izhodi.shape
        uspesnost = zeros(n_razredov)
        stevilo_vzorcev = zeros(n_razredov)
        for i in range(0, n_vzorcev):
            razred = self.P.razvrsti(vhodi[i,:])
            stevilo_vzorcev[izhodi[i,:].argmax()] += 1
            if razred.argmax() == izhodi[i,:].argmax():
                uspesnost[izhodi[i,:].argmax()] += 1
        uspesnost = uspesnost/stevilo_vzorcev
        return uspesnost, stevilo_vzorcev         
