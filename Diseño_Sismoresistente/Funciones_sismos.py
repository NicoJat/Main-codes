import numpy as np

def BNewmarkJr(Sg2,zi,T,m,w):

    delta = 0.01
    Kp = ((2*np.pi/T)**2)*m

    xn1 = np.zeros(len(Sg2))
    xvn1 = np.zeros(len(Sg2))
    xan1 = np.zeros(len(Sg2))

    xo = 0
    xvo = 0
    xn1[0] = xo
    xvn1[0] = xvo
    xan1[0] = ((-Sg2[0,1]*m) - (2*zi*w*m*xvo) - ((w**2)*xo))/m

    for i in np.arange(1, len(Sg2)):
        xn1[i] = xn1[i-1] + (delta*xvn1[i-1]) + (((delta**2)/2)*xan1[i-1])
        xvn1[i] = xvn1[i-1] + (delta*(0.5*(xan1[i-1] + xan1[i])))
        xan1[i] = (1/(m+(2*zi*w*delta*0.5*m)))*((-Sg2[i,1]*m) - (Kp*xn1[i]) - ((2*zi*w*m)*(xvn1[i-1]+(delta*0.5*xan1[i-1]))))

    Sa_max = np.max(np.abs(xan1))

    return xn1, xvn1, xan1, Sa_max

'''
def BNewmarkClassic():
'''

def Spec_NEC(n, z, fa, fd, fs, r, I, R, fip, fie):
    To = 0.1*fs*(fd/fa)
    Tc = 0.55*fs*(fd/fa)
    Tl = 2.4*fd

    j = 0
    Spec = []
    SpecI = []
    Tmp = []
    for T in np.arange(0,Tl,0.01):
        if T <= To:
            Tmp.append(T)
            Spec.append(z*fa*(1 + ((n-1)*(T/To))))
            SpecI.append(n*z*fa/(R*fip*fie))
        elif T > To and T < Tc:
            Tmp.append(T)
            Spec.append(n*z*fa)
            SpecI.append(n*z*fa/(R*fip*fie))
        else:
            Tmp.append(T)
            Spec.append(n*z*fa*((Tc/T)**r))
            SpecI.append(n*z*fa*((Tc/T)**r)/(R*fip*fie))
        
        j+=1

    return Spec, SpecI, Tmp


'''
Matriz de Rigidez y masas
'''

def K_M(num_col, H, E, tipo, I, vector, m, coef_castigo):

    k = []
    M = np.zeros((len(H), len(H)))
    for i in range(len(H)):
        ki = ((num_col*12)*E*I[i])/(H[i]**3)
        k.append(ki)
        M[i,i] = m[i]
    
    j = 0
    K = np.zeros((len(H), len(H)))
    for i in range(len(k)-1):
        K[i,i] = k[i] + k[i+1]
        K[i,j+1] = -k[i+1]
        K[i+1,j] = -k[i+1]
        K[len(k)-1,len(k)-1] = k[len(H)-1]
        j+=1

    return K, M, k
    
