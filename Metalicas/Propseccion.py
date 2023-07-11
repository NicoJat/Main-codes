# %%
import numpy as np

class propseccioni:
    

    def __init__(self, bf1,bf2,hw,tf1,tf2,tw):
        self.bf1 =bf1
        self.bf2 =bf2
        self.hw = hw
        self.tf1 =tf1
        self.tf2 =tf2
        self.tw = tw

    def area(self):
        area = (self.bf1*self.tf1)+(self.bf2*self.tf2)+(self.tw*self.hw) 
        return area
    
    def centroidxi(self):
        centroidxi = (np.maximum(self.bf1, self.bf2)*0.5)
        return centroidxi
    
    def centroidyi(self):
        centroidyi = (((self.tf2/2)*(self.bf2*self.tf2))+((self.tf2+(self.hw/2))*(self.tw*self.hw))+((self.tf2+self.hw+(self.tf1/2))*(self.bf1*self.tf1)))/((self.bf1*self.tf1)+(self.bf2*self.tf2)+(self.tw*self.hw))
        return centroidyi
    
    def inerciaxi(self):
        inerciaxi = (((self.bf1*(self.tf1**3)/12))+(self.bf1*self.tf1*np.abs(((self.tf2+(self.tf1/2)+self.hw-((((self.tf2/2)*(self.bf2*self.tf2))+((self.tf2+(self.hw/2))*(self.tw*self.hw))+((self.tf2+self.hw+(self.tf1/2))*(self.bf1*self.tf1)))/((self.bf1*self.tf1)+(self.bf2*self.tf2)+(self.tw*self.hw)))))**2))) + ((self.tw*(self.hw**3)/12)+(self.hw*self.tw*np.abs(((self.tf2+(self.hw/2)-((((self.tf2/2)*(self.bf2*self.tf2))+((self.tf2+(self.hw/2))*(self.tw*self.hw))+((self.tf2+self.hw+(self.tf1/2))*(self.bf1*self.tf1)))/((self.bf1*self.tf1)+(self.bf2*self.tf2)+(self.tw*self.hw)))))**2))) + ((self.bf2*(self.tf2**3)/12)+(self.bf2*self.tf2*(((((self.tf2/2)*(self.bf2*self.tf2))+((self.tf2+(self.hw/2))*(self.tw*self.hw))+((self.tf2+self.hw+(self.tf1/2))*(self.bf1*self.tf1)))/((self.bf1*self.tf1)+(self.bf2*self.tf2)+(self.tw*self.hw)))-(self.tf2/2))**2))
        return inerciaxi
    
    def inerciayi(self):
        inerciayi = (((self.tf1*(self.bf1**3)/12))) + ((self.hw*(self.tw**3)/12)) + ((self.tf2*(self.bf2**3)/12))
        return inerciayi
    
    def inerciapi(self):
        inerciapi = ((((self.bf1*(self.tf1**3)/12))+(self.bf1*self.tf1*np.abs(((self.tf2+(self.tf1/2)+self.hw-((((self.tf2/2)*(self.bf2*self.tf2))+((self.tf2+(self.hw/2))*(self.tw*self.hw))+((self.tf2+self.hw+(self.tf1/2))*(self.bf1*self.tf1)))/((self.bf1*self.tf1)+(self.bf2*self.tf2)+(self.tw*self.hw)))))**2)))) + ((self.tw*(self.hw**3)/12)+(self.hw*self.tw*np.abs(((self.tf2+(self.hw/2)-((((self.tf2/2)*(self.bf2*self.tf2))+((self.tf2+(self.hw/2))*(self.tw*self.hw))+((self.tf2+self.hw+(self.tf1/2))*(self.bf1*self.tf1)))/((self.bf1*self.tf1)+(self.bf2*self.tf2)+(self.tw*self.hw)))))**2))) + ((self.bf2*(self.tf2**3)/12)+(self.bf2*self.tf2*(((((self.tf2/2)*(self.bf2*self.tf2))+((self.tf2+(self.hw/2))*(self.tw*self.hw))+((self.tf2+self.hw+(self.tf1/2))*(self.bf1*self.tf1)))/((self.bf1*self.tf1)+(self.bf2*self.tf2)+(self.tw*self.hw)))-(self.tf2/2))**2)) + ((((self.tf1*(self.bf1**3)/12))) + ((self.hw*(self.tw**3)/12)) + ((self.tf2*(self.bf2**3)/12)))
        return inerciapi
    
    def x0i(self):
        x0i = np.maximum((self.bf1/2),(self.bf2/2))
        return x0i
    
    def y0i(self):
        y0i = (self.tf1*(self.bf1**3)*self.hw)/((self.tf1*(self.bf1**3))+(self.tf2*(self.bf2**3)))
        return y0i
    
    def rxi(self):
        rxi = np.sqrt(((((self.bf1*(self.tf1**3)/12))+(self.bf1*self.tf1*np.abs(((self.tf2+(self.tf1/2)+self.hw-((((self.tf2/2)*(self.bf2*self.tf2))+((self.tf2+(self.hw/2))*(self.tw*self.hw))+((self.tf2+self.hw+(self.tf1/2))*(self.bf1*self.tf1)))/((self.bf1*self.tf1)+(self.bf2*self.tf2)+(self.tw*self.hw)))))**2)))) + ((self.tw*(self.hw**3)/12)+(self.hw*self.tw*np.abs(((self.tf2+(self.hw/2)-((((self.tf2/2)*(self.bf2*self.tf2))+((self.tf2+(self.hw/2))*(self.tw*self.hw))+((self.tf2+self.hw+(self.tf1/2))*(self.bf1*self.tf1)))/((self.bf1*self.tf1)+(self.bf2*self.tf2)+(self.tw*self.hw)))))**2))) + ((self.bf2*(self.tf2**3)/12)+(self.bf2*self.tf2*(((((self.tf2/2)*(self.bf2*self.tf2))+((self.tf2+(self.hw/2))*(self.tw*self.hw))+((self.tf2+self.hw+(self.tf1/2))*(self.bf1*self.tf1)))/((self.bf1*self.tf1)+(self.bf2*self.tf2)+(self.tw*self.hw)))-(self.tf2/2))**2)))/((self.bf1*self.tf1)+(self.bf2*self.tf2)+(self.tw*self.hw))
        return rxi
    
    def ryi(self):
        ryi = np.sqrt(((((self.tf1*(self.bf1**3)/12))) + ((self.hw*(self.tw**3)/12)) + ((self.tf2*(self.bf2**3)/12)))/((self.bf1*self.tf1)+(self.bf2*self.tf2)+(self.tw*self.hw)))
        return ryi
    
    def cwi(self):
        cwi = ((self.hw**2)*self.tf1*(self.bf1**3)*(self.bf2**3))/(12*((self.bf1**3)+(self.bf2**3)))
        return cwi

#Terminar para secciones O, O huecos, cuadrado huecos, L & T!!


# %%
