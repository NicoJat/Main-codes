import numpy as np


class BNewmark_DS_GR2_2023_02:

    def __init__(self, Sg2,zi,T,m,w):
        self.T = T
        self.m = m
        self.w = w
        self.zi = zi
        self.Sg2 = Sg2


    def BNewmark(self):

        delta = 0.01
        Kp = ((2*np.pi/self.T)**2)*self.m

        xn1 = np.zeros(len(self.Sg2))
        xvn1 = np.zeros(len(self.Sg2))
        xan1 = np.zeros(len(self.Sg2))

        xo = 0
        xvo = 0
        xn1[0] = xo
        xvn1[0] = xvo
        xan1[0] = ((-self.Sg2[0,1]*self.m) - (2*self.zi*self.w*self.m*xvo) - ((self.w**2)*xo))/self.m

        for i in np.arange(1, len(self.Sg2)):
            xn1[i] = xn1[i-1] + (delta*xvn1[i-1]) + (((delta**2)/2)*xan1[i-1])
            xvn1[i] = xvn1[i-1] + (delta*(0.5*(xan1[i-1] + xan1[i])))
            xan1[i] = (1/(self.m+(2*self.zi*self.w*delta*0.5*self.m)))*((-self.Sg2[i,1]*self.m) - (Kp*xn1[i]) - ((2*self.zi*self.w*self.m)*(xvn1[i-1]+(delta*0.5*xan1[i-1]))))

        Sa_max = np.max(np.abs(xan1))

        return xn1, xvn1, xan1, Sa_max