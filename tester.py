# -*- coding: utf-8 -*-
"""
Copyright (c) 2012 University of Ljubljana, Faculty of Electrical Engineering.
All rights reserved. Licensed under the Academic Free License version 3.0.

@author Jure Sokolić, jure.sokolic@gmail.com
@version 15/06/2012

"""

from numpy  import *
from perceptron import *
from vzorci import *
from ucitelj import *


testni = '/home/jureso/Documents/Perceptron/isolet1+2+3+4.data'
ucni = '/home/jureso/Documents/Perceptron/isolet5.data'
V = Vzorci(u,t,617,26)

U = Ucitelj(V.n_znacilk,200,V.n_razredov)
U.parametri(0.000001, 2)
delta_w, iteracij, cas = U.ucenje(V.znacilke_ucni,V.razredi_ucni)

print delta_w
print interacij
print cas
    
w1 = load('w01.npy')
w2 = load('w12.npy')
w3 = load('w23.npy')

U1 = Ucitelj(w1,w2,w3)
uspesnost, stevilo_vzorcev = U1.testiraj(V.znacilke_testni,V.razredi_testni)

print ('***Testni vzorci***' + '\n')

print ('Povprecna uspesnost: ' + '%.3f' % (sum(uspesnost*stevilo_vzorcev)/V.n_testni) + '\n')
print 'Razred Vzorci Uspesnost'
for i in range(0,V.n_razredov):
    print (str(i) + '  ' + str(int(stevilo_vzorcev[i])) + '  ' + '%.3f'% uspesnost[i])
    

uspesnost, stevilo_vzorcev = U1.testiraj(V.znacilke_ucni,V.razredi_ucni)

print ('***Učni vzorci***' + '\n')

print ('Povprecna uspesnost: ' + '%.3f' % (sum(uspesnost*stevilo_vzorcev)/V.n_ucni) + '\n')
print 'Razred Vzorci Uspesnost'
for i in range(0,V.n_razredov):
    print (str(i) + '  ' + str(int(stevilo_vzorcev[i])) + '  ' + '%.3f'% uspesnost[i])

