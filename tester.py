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


testni = 'isolet1+2+3+4.data'
ucni = 'isolet5.data'
# Ustvarimo objekt vzorci, kjer so shranjena polja učnih in testnih vzorcev
V = Vzorci(ucni,testni,617,26)

# Ustvarimo objekt ucitelj. Ucitelj definira svoj perceptron s strukturo podano z argumenti
U = Ucitelj(V.n_znacilk,200,V.n_razredov)
U.parametri(0.000001, 2, 0.5) # takšni parametri so nastavljeni samo za demonstracijo delovanja
delta_w, iteracij, cas = U.ucenje(V.znacilke_ucni,V.razredi_ucni)

print ('Največja sprememba uteži: ' + str(delta_w))
print ('Število iteracij: ' + str(iteracij))
print ('Čas učenja: ' + str(cas))

# Datoteke wxx.npy vsebijejo vrednosti uteži za perceptron, ki ga opisujem v poročilu
w1 = load('w01.npy')
w2 = load('w12.npy')
w3 = load('w23.npy')
# Ustvarimo nov objekt ucitelj, kjer njegov perceptron definiramo s polji uteži nevronov perceptrona
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

