import numpy as np

'''
def BNewmarkClassic():
'''

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
Espesctro Respuesta de la NEC
'''
def Spec_NEC(n, z, fa, fd, fs, r, I, R, fip, fie, scale):
    To = 0.1*fs*(fd/fa)
    Tc = 0.55*fs*(fd/fa)
    Tl = 2.4*fd*scale

    j = 0
    Spec1 = []
    SpecI1 = []
    Tmp = []
    for T in np.arange(0,Tl,0.01):
        if T <= To:
            Tmp.append(T)
            Spec1.append(z*fa*(1 + ((n-1)*(T/To)))*I)
            SpecI1.append(n*z*fa*I/(R*fip*fie))
        elif T > To and T < Tc:
            Tmp.append(T)
            Spec1.append(n*z*fa*I)
            SpecI1.append(n*z*fa*I/(R*fip*fie))
        else:
            Tmp.append(T)
            Spec1.append(n*z*fa*((Tc/T)**r)*I)
            SpecI1.append(n*z*fa*((Tc/T)**r)*I/(R*fip*fie))
        
        j+=1

    Spec = np.column_stack((Tmp,Spec1))
    SpecI = np.column_stack((Tmp,SpecI1))

    return Spec, SpecI, Tmp, To, Tc, Tl


'''
Espesctro Respuesta de la ASCE 7-16
'''
def Spec_ASCE7(Tl, Fa, Fv, Ss, S1, limite):
    Sms = Fa*Ss
    Sm1 = Fv*S1
    Sds = (2/3)*Sms
    Sd1 = (2/3)*Sm1
    Ts = Sd1/Sds
    To = 0.2*(Sd1/Sds)

    '''
    1era_porción de la curva, 0 <= T < T0
    Ver en sección 11.4-6
    Sa = Sds*(0.4+(0.6*T/T0))

    2da_porción de la curva, T0 <= T <= Ts
    Sds

    3era_porción de la curva, Ts <= T <= Tl
    Sa = Sd1/T

    4ta_porción de la curva
    Sa = (Sd1*Tl)/(T**2)
    '''

    j = 0
    Spec_ASCE = []
    #SpecI = []
    Tmp = []
    for T in np.arange(0,limite,0.01):
        if T <= To:
            Tmp.append(T)
            Spec_ASCE.append(Sds*(0.4+(0.6*T/To)))
            #SpecI.append(n*z*fa/(R*fip*fie))
        elif T > To and T < Ts:
            Tmp.append(T)
            Spec_ASCE.append(Sds)
            #SpecI.append(n*z*fa/(R*fip*fie))
        elif T > Ts and T < Tl:
            Tmp.append(T)
            Spec_ASCE.append(Sd1/T)
            #SpecI.append(n*z*fa*((Ts/T)**r)/(R*fip*fie))
        else:
            Tmp.append(T)        
            Spec_ASCE.append((Sd1*Tl)/(T**2))    
        j+=1

    Spec_ASCE = np.column_stack((Tmp,Spec_ASCE))

    return Spec_ASCE, Tmp



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
