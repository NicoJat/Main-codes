# %%
import numpy as np

class propseccioni:


    def __init__(self, bf1,bf2,hw,tf1,tf2,tw):
        self.bf1 = bf1
        self.bf2 = bf2
        self.hw = hw
        self.tf1 = tf1
        self.tf2 = tf2
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
    

class propseccionohuec:
    def __init__(self, d01, d02):
        self.d01 = d01
        self.d02 = d02 

    def areaohuec(self):
        areaohuec = (np.pi*(self.d02**2)*0.25)-(np.pi*(self.d01**2)*0.25)
        return areaohuec

    def centroidxohuec(self):
        centroidxohuec = self.d02/2
        return centroidxohuec
    
    def centroidyohuec(self):
        centroidyohuec = self.d02/2
        return centroidyohuec
    
    def inerciaxohuec(self):
        inerciaxohuec = np.pi*((self.d02/2)**4)*0.25 - np.pi*((self.d01/2)**4)*0.25
        return inerciaxohuec
    
    def inerciayohuec(self):
        inerciayohuec = np.pi*((self.d02/2)**4)*0.25 - np.pi*((self.d01/2)**4)*0.25
        return inerciayohuec
    
    def inerciapohuec(self):
        inerciapohuec = (np.pi*((self.d02/2)**4)*0.25 - np.pi*((self.d01/2)**4)*0.25) + (np.pi*((self.d02/2)**4)*0.25 - np.pi*((self.d01/2)**4)*0.25)
        return inerciapohuec
    
    def rxohuec(self):
        rxohuec = np.sqrt((np.pi*((self.d02/2)**4)*0.25 - np.pi*((self.d01/2)**4)*0.25)/((np.pi*(self.d02**2)*0.25)-(np.pi*(self.d01**2)*0.25)))
        return rxohuec
    
    def ryohuec(self):
        ryohuec = np.sqrt((np.pi*((self.d02/2)**4)*0.25 - np.pi*((self.d01/2)**4)*0.25)/((np.pi*(self.d02**2)*0.25)-(np.pi*(self.d01**2)*0.25)))
        return ryohuec   
    


class propseccionl:

    def __init__(self, a1l, a2l, e1l, e2l):
        self.a1l = a1l
        self.a2l = a2l
        self.e1l = e1l
        self.e2l = e2l 

    def areal(self):
        areal = (((self.a1l)*(self.e2l))+((self.a1l)*(self.e2l)))
        return areal

    def centroidxl(self):
        centroidxl = (((self.e1l/2*self.a1l*self.e1l)+(self.a2l/2*self.e2l*self.a2l))/(((self.a1l)*(self.e2l))+((self.a1l)*(self.e2l))))
        return centroidxl
    
    def centroidyl(self):
        centroidyl = ((((self.e2l+(self.a1l/2))*self.a1l*self.e1l)+((self.e2l/2)*self.a2l*self.e2l))/(((self.a1l)*(self.e2l))+((self.a1l)*(self.e2l))))
        return centroidyl
    
    def inerciaxl(self):
        inerciaxl = (((self.e1l*(self.a1l**3)/12))+(self.a1l*self.e1l*np.abs((((self.a1l/2)- ((((self.e2l+(self.a1l/2))*self.a1l*self.e1l)+((self.e2l/2)*self.a2l*self.e2l))/(((self.a1l)*(self.e2l))+((self.a1l)*(self.e2l)))))**2)))) + ((self.a2l*(self.e2l**3)/12)+(self.a2l*self.e2l*np.abs((((((self.e2l+(self.a1l/2))*self.a1l*self.e1l)+((self.e2l/2)*self.a2l*self.e2l))/(((self.a1l)*(self.e2l))+((self.a1l)*(self.e2l))))-(self.e2l/2))**2)))
        return inerciaxl
    
    def inerciayl(self):
        inerciayl = (((self.a1l*(self.e1l**3)/12))+(self.a1l*self.e1l*np.abs((((((self.e1l/2*self.a1l*self.e1l)+(self.a2l/2*self.e2l*self.a2l))/(((self.a1l)*(self.e2l))+((self.a1l)*(self.e2l))))-(self.e1l/2))**2)))) + ((self.e2l*(self.a2l**3)/12)+(self.a2l*self.e2l*np.abs(((self.a2l/2)-(((self.e1l/2*self.a1l*self.e1l)+(self.a2l/2*self.e2l*self.a2l))/(((self.a1l)*(self.e2l))+((self.a1l)*(self.e2l)))))**2)))
        return inerciayl

    def inerciapl(self):
        inerciapl = (((self.e1l*(self.a1l**3)/12))+(self.a1l*self.e1l*np.abs((((self.a1l/2)- ((((self.e2l+(self.a1l/2))*self.a1l*self.e1l)+((self.e2l/2)*self.a2l*self.e2l))/(((self.a1l)*(self.e2l))+((self.a1l)*(self.e2l)))))**2)))) + ((self.a2l*(self.e2l**3)/12)+(self.a2l*self.e2l*np.abs((((((self.e2l+(self.a1l/2))*self.a1l*self.e1l)+((self.e2l/2)*self.a2l*self.e2l))/(((self.a1l)*(self.e2l))+((self.a1l)*(self.e2l))))-(self.e2l/2))**2))) + (((self.a1l*(self.e1l**3)/12))+(self.a1l*self.e1l*np.abs((((((self.e1l/2*self.a1l*self.e1l)+(self.a2l/2*self.e2l*self.a2l))/(((self.a1l)*(self.e2l))+((self.a1l)*(self.e2l))))-(self.e1l/2))**2)))) + ((self.e2l*(self.a2l**3)/12)+(self.a2l*self.e2l*np.abs(((self.a2l/2)-(((self.e1l/2*self.a1l*self.e1l)+(self.a2l/2*self.e2l*self.a2l))/(((self.a1l)*(self.e2l))+((self.a1l)*(self.e2l)))))**2)))
        return inerciapl
    
    def rxl(self):
        rxl = np.sqrt((((self.e1l*(self.a1l**3)/12))+(self.a1l*self.e1l*np.abs((((self.a1l/2)- ((((self.e2l+(self.a1l/2))*self.a1l*self.e1l)+((self.e2l/2)*self.a2l*self.e2l))/(((self.a1l)*(self.e2l))+((self.a1l)*(self.e2l)))))**2)))) + ((self.a2l*(self.e2l**3)/12)+(self.a2l*self.e2l*np.abs((((((self.e2l+(self.a1l/2))*self.a1l*self.e1l)+((self.e2l/2)*self.a2l*self.e2l))/(((self.a1l)*(self.e2l))+((self.a1l)*(self.e2l))))-(self.e2l/2))**2)))/(((self.a1l)*(self.e2l))+((self.a1l)*(self.e2l))))
        return rxl
    
    def ryl(self):
        ryl = np.sqrt((((self.a1l*(self.e1l**3)/12))+(self.a1l*self.e1l*np.abs((((((self.e1l/2*self.a1l*self.e1l)+(self.a2l/2*self.e2l*self.a2l))/(((self.a1l)*(self.e2l))+((self.a1l)*(self.e2l))))-(self.e1l/2))**2)))) + ((self.e2l*(self.a2l**3)/12)+(self.a2l*self.e2l*np.abs(((self.a2l/2)-(((self.e1l/2*self.a1l*self.e1l)+(self.a2l/2*self.e2l*self.a2l))/(((self.a1l)*(self.e2l))+((self.a1l)*(self.e2l)))))**2)))/(((self.a1l)*(self.e2l))+((self.a1l)*(self.e2l))))
        return ryl
    
    def x0l(self):
        x0l = self.e1l/2
        return x0l
    
    def y0l(self):
        y0l = self.e2l/2
        return y0l
    
    def cwl(self):
        cwl = ((self.e1l**3)*(((self.a1l+(self.e2l/2))**3)+((self.a2l+(self.e1l/2))**3)))/36
        return cwl


class propsecciont:

    def __init__(self, bft, hwt, tft, twt):
        self.bft = bft
        self.hwt = hwt
        self.tft = tft
        self.twt = twt
                                                 

    def areat(self):
        areat = ((self.bft*self.tft)+(self.twt*self.hwt))
        return areat

    def centroidxt(self):
        centroidxt = (self.bft*0.5)
        return centroidxt
    
    def centroidyt(self):
        centroidyt = ((((self.hwt/2)*(self.twt*self.hwt))+((self.hwt+(self.tft/2))*(self.bft*self.tft)))/((self.bft*self.tft)+(self.twt*self.hwt)))
        return centroidyt
    
    def inerciaxt(self):
        inerciaxt = ((((self.bft*(self.tft**3)/12))+(self.bft*self.tft*np.abs(((self.hwt+self.tft)-((((self.hwt/2)*(self.twt*self.hwt))+((self.hwt+(self.tft/2))*(self.bft*self.tft)))/((self.bft*self.tft)+(self.twt*self.hwt)))-(self.tft/2))**2))) + ((self.twt*(self.hwt**3)/12)+(self.hwt*self.twt*np.abs(((((((self.hwt/2)*(self.twt*self.hwt))+((self.hwt+(self.tft/2))*(self.bft*self.tft)))/((self.bft*self.tft)+(self.twt*self.hwt)))-(self.hwt/2))**2)))))
        return inerciaxt
    
    def inerciayt(self):
        inerciayt = ((self.tft*(self.bft**3)/12) + (self.hwt*(self.twt**3)/12))
        return inerciayt

    def inerciapt(self):
        inerciapt = ((((self.bft*(self.tft**3)/12))+(self.bft*self.tft*np.abs(((self.hwt+self.tft)-((((self.hwt/2)*(self.twt*self.hwt))+((self.hwt+(self.tft/2))*(self.bft*self.tft)))/((self.bft*self.tft)+(self.twt*self.hwt)))-(self.tft/2))**2))) + ((self.twt*(self.hwt**3)/12)+(self.hwt*self.twt*np.abs(((((((self.hwt/2)*(self.twt*self.hwt))+((self.hwt+(self.tft/2))*(self.bft*self.tft)))/((self.bft*self.tft)+(self.twt*self.hwt)))-(self.hwt/2))**2))))) + ((self.tft*(self.bft**3)/12) + (self.hwt*(self.twt**3)/12))
        return inerciapt
    
    def rxt(self):
        rxt = np.sqrt(((((self.bft*(self.tft**3)/12))+(self.bft*self.tft*np.abs(((self.hwt+self.tft)-((((self.hwt/2)*(self.twt*self.hwt))+((self.hwt+(self.tft/2))*(self.bft*self.tft)))/((self.bft*self.tft)+(self.twt*self.hwt)))-(self.tft/2))**2))) + ((self.twt*(self.hwt**3)/12)+(self.hwt*self.twt*np.abs(((((((self.hwt/2)*(self.twt*self.hwt))+((self.hwt+(self.tft/2))*(self.bft*self.tft)))/((self.bft*self.tft)+(self.twt*self.hwt)))-(self.hwt/2))**2)))))/((self.bft*self.tft)+(self.twt*self.hwt)))
        return rxt
    
    def ryt(self):
        ryt = np.sqrt(((self.tft*(self.bft**3)/12) + (self.hwt*(self.twt**3)/12))/((self.bft*self.tft)+(self.twt*self.hwt)))
        return ryt
    
    def x0t(self):
        x0t = self.bft/2
        return x0t
    
    def y0t(self):
        y0t = self.hwt + (self.tft/2)
        return y0t
    
    def cwt(self):
        cwt = (((self.tft**3)*(self.bft**3))/144) + (((self.twt**3)*(self.hwt**3))//36)
        return cwt


class propseccionc:

    def __init__(self, a1c, a2c, a3c, e1c, e2c, e3c):
        self.a1c = a1c
        self.a2c = a2c
        self.a3c = a3c
        self.e1c = e1c
        self.e2c = e2c
        self.e3c = e3c                       

    def areac(self):
        areac = ((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c)))
        return areac

    def centroidxc(self):
        centroidxc = (((self.a1c/2*self.a1c*self.e1c)+(self.e2c/2*self.a2c*self.e2c)+(self.a3c/2*self.a3c*self.e3c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c))))
        return centroidxc
    
    def centroidyc(self):
        centroidyc = (((self.e3c/2*self.a3c*self.e3c)+((self.e3c+(self.a2c/2))*self.a2c*self.e2c)+((self.e3c+self.a2c+(self.e1c/2))*self.a1c*self.e1c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c))))
        return centroidyc
    
    def inerciaxc(self):
        inerciaxc = ((((self.a1c*(self.e1c**3)/12))+(self.a1c*self.e1c*np.abs(((self.e3c+(self.e1c/2)+self.a2c-(((self.e3c/2*self.a3c*self.e3c)+((self.e3c+(self.a2c/2))*self.a2c*self.e2c)+((self.e3c+self.a2c+(self.e1c/2))*self.a1c*self.e1c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c)))))**2)))) + ((self.e2c*(self.a2c**3)/12)+(self.a2c*self.e2c*np.abs(((self.e3c+(self.a2c/2)-(((self.e3c/2*self.a3c*self.e3c)+((self.e3c+(self.a2c/2))*self.a2c*self.e2c)+((self.e3c+self.a2c+(self.e1c/2))*self.a1c*self.e1c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c))))))**2))) + ((self.a3c*(self.e3c**3)/12)+(self.a3c*self.e3c*((((self.e3c/2*self.a3c*self.e3c)+((self.e3c+(self.a2c/2))*self.a2c*self.e2c)+((self.e3c+self.a2c+(self.e1c/2))*self.a1c*self.e1c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c))))-(self.e3c/2))**2)))
        return inerciaxc
    
    def inerciayc(self):
        inerciayc = ((((self.e1c*(self.a1c**3)/12))+(self.a1c*self.e1c*np.abs((((self.a1c/2)-(((self.a1c/2*self.a1c*self.e1c)+(self.e2c/2*self.a2c*self.e2c)+(self.a3c/2*self.a3c*self.e3c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c)))))**2)))) + ((self.a2c*(self.e2c**3)/12)+(self.a2c*self.e2c*np.abs(((((self.a1c/2*self.a1c*self.e1c)+(self.e2c/2*self.a2c*self.e2c)+(self.a3c/2*self.a3c*self.e3c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c))))-(self.e2c/2))**2))) + ((self.e3c*(self.a3c**3)/12)+(self.a3c*self.e3c*((self.a3c/2)-(((self.a1c/2*self.a1c*self.e1c)+(self.e2c/2*self.a2c*self.e2c)+(self.a3c/2*self.a3c*self.e3c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c)))))**2)))
        return inerciayc

    def inerciapc(self):
        inerciapc = ((((self.a1c*(self.e1c**3)/12))+(self.a1c*self.e1c*np.abs(((self.e3c+(self.e1c/2)+self.a2c-(((self.e3c/2*self.a3c*self.e3c)+((self.e3c+(self.a2c/2))*self.a2c*self.e2c)+((self.e3c+self.a2c+(self.e1c/2))*self.a1c*self.e1c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c)))))**2)))) + ((self.e2c*(self.a2c**3)/12)+(self.a2c*self.e2c*np.abs(((self.e3c+(self.a2c/2)-(((self.e3c/2*self.a3c*self.e3c)+((self.e3c+(self.a2c/2))*self.a2c*self.e2c)+((self.e3c+self.a2c+(self.e1c/2))*self.a1c*self.e1c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c))))))**2))) + ((self.a3c*(self.e3c**3)/12)+(self.a3c*self.e3c*((((self.e3c/2*self.a3c*self.e3c)+((self.e3c+(self.a2c/2))*self.a2c*self.e2c)+((self.e3c+self.a2c+(self.e1c/2))*self.a1c*self.e1c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c))))-(self.e3c/2))**2))) + ((((self.e1c*(self.a1c**3)/12))+(self.a1c*self.e1c*np.abs((((self.a1c/2)-(((self.a1c/2*self.a1c*self.e1c)+(self.e2c/2*self.a2c*self.e2c)+(self.a3c/2*self.a3c*self.e3c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c)))))**2)))) + ((self.a2c*(self.e2c**3)/12)+(self.a2c*self.e2c*np.abs(((((self.a1c/2*self.a1c*self.e1c)+(self.e2c/2*self.a2c*self.e2c)+(self.a3c/2*self.a3c*self.e3c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c))))-(self.e2c/2))**2))) + ((self.e3c*(self.a3c**3)/12)+(self.a3c*self.e3c*((self.a3c/2)-(((self.a1c/2*self.a1c*self.e1c)+(self.e2c/2*self.a2c*self.e2c)+(self.a3c/2*self.a3c*self.e3c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c)))))**2)))
        return inerciapc
    
    def rxc(self):
        rxc = np.sqrt(((((self.a1c*(self.e1c**3)/12))+(self.a1c*self.e1c*np.abs(((self.e3c+(self.e1c/2)+self.a2c-(((self.e3c/2*self.a3c*self.e3c)+((self.e3c+(self.a2c/2))*self.a2c*self.e2c)+((self.e3c+self.a2c+(self.e1c/2))*self.a1c*self.e1c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c)))))**2)))) + ((self.e2c*(self.a2c**3)/12)+(self.a2c*self.e2c*np.abs(((self.e3c+(self.a2c/2)-(((self.e3c/2*self.a3c*self.e3c)+((self.e3c+(self.a2c/2))*self.a2c*self.e2c)+((self.e3c+self.a2c+(self.e1c/2))*self.a1c*self.e1c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c))))))**2))) + ((self.a3c*(self.e3c**3)/12)+(self.a3c*self.e3c*((((self.e3c/2*self.a3c*self.e3c)+((self.e3c+(self.a2c/2))*self.a2c*self.e2c)+((self.e3c+self.a2c+(self.e1c/2))*self.a1c*self.e1c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c))))-(self.e3c/2))**2)))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c))))
        return rxc
    
    def ryc(self):
        ryc = np.sqrt(((((self.e1c*(self.a1c**3)/12))+(self.a1c*self.e1c*np.abs((((self.a1c/2)-(((self.a1c/2*self.a1c*self.e1c)+(self.e2c/2*self.a2c*self.e2c)+(self.a3c/2*self.a3c*self.e3c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c)))))**2)))) + ((self.a2c*(self.e2c**3)/12)+(self.a2c*self.e2c*np.abs(((((self.a1c/2*self.a1c*self.e1c)+(self.e2c/2*self.a2c*self.e2c)+(self.a3c/2*self.a3c*self.e3c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c))))-(self.e2c/2))**2))) + ((self.e3c*(self.a3c**3)/12)+(self.a3c*self.e3c*((self.a3c/2)-(((self.a1c/2*self.a1c*self.e1c)+(self.e2c/2*self.a2c*self.e2c)+(self.a3c/2*self.a3c*self.e3c))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c)))))**2)))/((self.a1c*self.e1c)+((self.a2c)*(self.e2c))+((self.a3c)*(self.e3c))))
        return ryc
    
    def x0c(self):
        x0c = ((self.a1c**2)+(self.a3c**2))/(2*(self.a2c+self.a1c+self.a3c))
        return x0c
    
    def y0c(self):
        y0c = ((self.a2c**2)+(2*self.a1c*self.a2c))/(2*self.a2c*(self.a1c+self.a3c))
        return y0c
    
    def cwc(self):
        cwc = (((self.a1c-(self.e2c/2))**3)*((self.a2c+(self.e1c/2)+(self.e3c/2))**2)*self.e3c*(2*((self.a2c+(self.e1c/2)+(self.e3c/2))*self.e2c)+(3*(self.a1c+(self.e2c/2))*self.e3c)))/(12*((self.a2c+(self.e1c/2)+(self.e3c/2))*self.e2c)+(6*(self.a1c+(self.e2c/2))*self.e3c))
        return cwc
    


class propseccionrechuec:

    def __init__(self, a1rech, a2rech, b1rech, b2rech):
        self.a1rech = a1rech
        self.a2rech = a2rech
        self.b1rech = b1rech
        self.b2rech = b2rech

    def areaohuec(self):
        areaohuec = ((self.a2rech*self.b2rech)-(self.a1rech*self.b1rech))
        return areaohuec

    def centroidxohuec(self):
        centroidxohuec = self.b2rech/2
        return centroidxohuec
    
    def centroidyohuec(self):
        centroidyohuec = self.a2rech/2
        return centroidyohuec
    
    def inerciaxohuec(self):
        inerciaxohuec = (((self.b2rech*(self.a2rech**3))/12)-((self.b1rech*(self.a1rech**3))/12))
        return inerciaxohuec
    
    def inerciayohuec(self):
        inerciayohuec = (((self.a2rech*(self.b2rech**3))/12)-((self.a1rech*(self.b1rech**3))/12))
        return inerciayohuec
    
    def inerciapohuec(self):
        inerciapohuec = (((self.b2rech*(self.a2rech**3))/12)-((self.b1rech*(self.a1rech**3))/12)) + (((self.a2rech*(self.b2rech**3))/12)-((self.a1rech*(self.b1rech**3))/12))
        return inerciapohuec
    
    def rxohuec(self):
        rxohuec = np.sqrt((((self.b2rech*(self.a2rech**3))/12)-((self.b1rech*(self.a1rech**3))/12))/((self.a2rech*self.b2rech)-(self.a1rech*self.b1rech)))
        return rxohuec
    
    def ryohuec(self):
        ryohuec = np.sqrt((((self.a2rech*(self.b2rech**3))/12)-((self.a1rech*(self.b1rech**3))/12))/((self.a2rech*self.b2rech)-(self.a1rech*self.b1rech)))
        return ryohuec   
