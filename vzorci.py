# -*- coding: utf-8 -*-
"""
Copyright (c) 2012 University of Ljubljana, Faculty of Electrical Engineering.
All rights reserved. Licensed under the Academic Free License version 3.0.

@author Jure Sokolić, jure.sokolic@gmail.com
@version 15/06/2012

"""
import mmap
from numpy import *
# Razred lahko interpretira datoteke z vzorci tipa isolet5.data
class Vzorci:
    def __init__(self, ucni_vzorci, testni_vzorci, n_znacilk, n_razredov):
        self.ucni = ucni_vzorci
        self.testni = testni_vzorci
        self.n_znacilk = n_znacilk
        self.n_razredov = n_razredov
        self.n_ucni = self.st_vzorcev(ucni_vzorci)
        self.n_testni = self.st_vzorcev(testni_vzorci)
        
        self.znacilke_ucni, self.razredi_ucni = self.naredi_polja(ucni_vzorci,self.n_ucni, n_znacilk,n_razredov)
        self.znacilke_testni, self.razredi_testni = self.naredi_polja(testni_vzorci,self.n_testni, n_znacilk,n_razredov)
    
    # praktično samo prešteje število vrstic
    def st_vzorcev(self,datoteka):
        f = open(datoteka, 'r')
        lines = 0
        buf_size = 1024 * 1024
        read_f = f.read # loop optimization
        buf = read_f(buf_size)
        while buf:
            lines += buf.count('\n')
            buf = read_f(buf_size)
        f.close()
        return lines
    
    # celotno txt datoteko pretvori v dve polji: znacilke in razredi
    def naredi_polja(self,datoteka, st_vrstic, st_znacilk, st_razredov):
        a = zeros((st_vrstic, st_znacilk+1))
        vhodi = zeros((st_vrstic, st_znacilk))
        izhodi = zeros((st_vrstic, st_razredov))
        f = open(datoteka, 'r')
        i = 0
        while (i >= 0):
            s1 = f.readline()
            if len(s1) == 0:
                break
            a[i,:] = fromstring(s1[0:-2], sep=', ')
            vhodi[i,:] = a[i,0:-1]
            izhodi[i,a[i,-1]-1] = 1
            i +=1
        f.close()
        return vhodi, izhodi