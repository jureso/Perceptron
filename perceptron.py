# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 20:40:04 2012

@author: jureso
"""

from numpy  import *
import pylab

class Perceptron:
    beta = 0.5       
    def __init__(self, n1plast, n2plast, n3plast):
        #lahko ga definiramo s prej naučenimi matrikami uteži, ali pa samo določimo strukturo
        if isinstance(n1plast, ndarray): #podane so matrike uteži
            self.w01 = n1plast
            self.w12 = n2plast
            self.w23 = n3plast
            self.n1 = n1plast.shape[1]
            self.n2 = n2plast.shape[1]
            self.n3 = n3plast.shape[1]
        else: #podana je samo struktura
            self.n1 = n1plast
            self.n2 = n2plast
            self.n3 = n3plast
            self.w01 = random.rand(self.n1 +1, self.n1) - 0.5 + spacing(1) #prvi argument je začetek povezave, drugi pa konec povezave
            self.w12 = random.rand(self.n1 +1, self.n2) - 0.5 + spacing(1)
            self.w23 = random.rand(self.n2+1, self.n3) - 0.5 + spacing(1)        
            self.x1 = zeros(self.n1)
            self.x2 = zeros(self.n2)
            self.x3 = zeros(self.n3)
        
        self.dw01 = zeros((self.n1 +1, self.n1)) 
        self.dw12 = zeros((self.n1 +1, self.n2)) #prvi argument je začetek povezave, drugi pa konec povezave
        self.dw23 = zeros((self.n2+1, self.n3))

        self.d3 = zeros((self.n3))
        self.d2 = zeros((self.n2))
        self.d1 = zeros((self.n1))
        
    def x123(self,vhod):
        input_1 = insert(vhod,len(vhod),1)
        for i in range(0,self.n1):
            self.x1[i] = dot(self.w01[:,i], input_1)
            self.x1[i] = 1/(1+exp(-self.x1[i]))
        input_1 = insert(self.x1,len(self.x1),1)    
        for i in range(0,self.n2):
            self.x2[i] = dot(self.w12[:,i], input_1)
            self.x2[i] = 1/(1+exp(-self.x2[i]))
        input_1 = insert(self.x2,len(self.x2),1)     
        for i in range(0,self.n3):
            self.x3[i] = dot(self.w23[:,i], input_1)
            self.x3[i] = 1/(1+exp(-self.x3[i]))
        
    def izracunaj_d3(self, izhod):
        self.d3 = (izhod-self.x3)*(1-self.x3)*self.x3  
        
    def delta_w23(self):
        input_1 = insert(self.x2,len(self.x2),1)
        for i in range(0,len(input_1)):
            self.dw23[i,:] = self.d3*self.beta*input_1[i]
        
    def delta_w12(self):
        input_1 = insert(self.x1,len(self.x1),1)
        for i in range(0,len(input_1)):
            self.dw12[i,:] = self.d2*self.beta*input_1[i]
        
    def delta_w01(self, vhod):
        input_1 = insert(vhod,len(vhod),1)
        for i in range(0,len(input_1)):
            self.dw01[i,:] = self.d1*self.beta*input_1[i]        
      
    def izracunaj_d2(self):
        temp = sum(self.w23*self.d3, axis = 1)
        self.d2 = (1-self.x2)*self.x2*temp[0:-1]
        
    def izracunaj_d1(self):
        temp = sum(self.w12*self.d2, axis = 1)
        self.d1 = (1-self.x1)*self.x1*temp[0:-1]
        
    def vzvratno_ucenje(self,vhod,izhod):
        self.x123(vhod)        
        self.izracunaj_d3(izhod)
        self.izracunaj_d2()
        self.izracunaj_d1()
        self.delta_w23()        
        self.delta_w12()        
        self.delta_w01(vhod)
        self.w23 = self.w23 + self.dw23
        self.w12 = self.w12 + self.dw12
        self.w01 = self.w01 + self.dw01
        return max(abs(self.dw01).max(), abs(self.dw01).max(),abs(self.dw01).max())
        
    def razvrsti(self, vhod):
        self.x123(vhod)
        return self.x3
        
        
def main():
    iz1 = array([0, 1])
    iz2 = array([1, 0])
    vh1 = array([1, 0])
    vh2 = array([0, 1])
    vh3 = array([1, 1])
    vh4 = array([0, 0])
    
    P = Perceptron(2,2,2)
    P.beta = 0.5
    x =zeros(10000)
    y =zeros(10000)
    for i in range(0, 10000):
        x[i] = i
        P.vzvratno_ucenje(vh1, iz1)
        P.vzvratno_ucenje(vh2, iz1)
        P.vzvratno_ucenje(vh3, iz2)
        y[i]=   P.vzvratno_ucenje(vh4, iz2)
        
    pylab.plot(x,y)
    pylab.show()
        
    print P.razvrsti(vh1)
    print P.razvrsti(vh2)
    print P.razvrsti(vh3)
    print P.razvrsti(vh4)
        
if __name__ == "__main__":
    main()
    

