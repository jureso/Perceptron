# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 20:40:04 2012

@author: jureso
"""

from numpy  import *

class Perceptron:
    beta = 0.5       
    def __init__(self, n1plast, n2plast, n3plast):
        self.n1 = n1plast
        self.n2 = n2plast
        self.n3 = n3plast
        self.w12 = random.rand(self.n2, self.n1+1) - 0.5 + spacing(1) #prvi argument je začetek povezave, drugi pa konec povezave
        self.w23 = random.rand(self.n3, self.n2+1) - 0.5 + spacing(1)
        self.dw12 = zeros((self.n2, self.n1+1)) #prvi argument je začetek povezave, drugi pa konec povezave
        self.dw23 = zeros((self.n3, self.n2+1))
        #self.x2 = zeros((self.n2,1))
        #self.x3 = zeros((self.n3,1))
        self.d3 = zeros((self.n3))
        self.d2 = zeros((self.n2))
        
    def izhod_xi(self, vhod, utezi):
        #utezi:vrstica je izhodni nevron, stolpec je vir povezave
        #vhod je stolpični vektor
        temp = dot(utezi, insert(vhod,len(vhod),1))
        return (1/(1+exp(-temp))).T               

    def izhodi(self,vhod):
        self.x2 = self.izhod_xi(vhod,self.w12).T
        self.x3 = self.izhod_xi(self.x2,self.w23).T
        
    def izracunaj_d3(self, izhod):
        #izhod je stolpični vektor
        self.d3 = (izhod-self.x3)*(1-self.x3)*self.x3          
    def izracunaj_d2(self):
        ind = 0
        for x in self.x3:
            self.d2[ind] = (1-x)*x*sum(self.d3[ind]*self.w23[ind,:])
            ind += 1

    def popravi_w3(self):
        temp = insert(self.x2,len(self.x2),1)
        ind = 0
        for x in temp:
             self.dw23[:,ind] = self.beta*self.d3*x
             ind +=1        
        self.w23 = self.w23 + self.dw23
        
    def popravi_w2(self, vhod):
        temp = insert(vhod,len(vhod),1)
        ind = 0
        for x in temp:      
            self.dw12[:,ind] = self.beta*self.d2*x
            ind +=1
        self.w12 = self.w12 + self.dw12      
 
        
    def vzvratno_ucenje(self,vhod,izhod):
        self.izhodi(vhod)        
        self.izracunaj_d3(izhod)
        self.izracunaj_d2()
        #self.izracunaj_d1()
        self.popravi_w3()        
        #self.popravi_w2()
        self.popravi_w2(vhod)
        
    def razvrsti(self, vhod):
        self.izhodi(vhod)
        return self.x3
        
        
def main():    
    vh = array([[1], [2], [3]])
    iz = array([[4.], [5.], [6.]])
    P1 = Perceptron(3, 3, 3)
    print P1.w23
    P1.vzvratno_ucenje(vh,iz)
    print P1.w23
    
if __name__ == "__main__":
    main()
        
#vh = array([[1], [2], [3]])
#iz = array([4., 5., 6.])
#P1 = Perceptron(3, 3, 3)       
#P1.vzvratno_ucenje(vh,iz)