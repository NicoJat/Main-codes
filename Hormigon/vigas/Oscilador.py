import numpy as np
import Funciones_sismos as BN
from scipy.linalg import eigh




def Oscilador(E, gdl, col, num_col, h, inercia_efectiva, m_piso, Spec, SpecI):
    I = np.ones(gdl)*((col**4)/12)*inercia_efectiva #m**4
    H = np.ones(gdl)*h #m
    m = np.ones(gdl)*m_piso    #Tonf*(s**2)*(m**-1)
    r = np.ones(gdl)
    coef_castigo = 1
    tipo = 1
    vector = 0

    #Matrices de Masa y Rigidez
    K, M, k = BN.K_M(num_col, H, E, tipo, I, vector, m, coef_castigo)

    V, D = eigh(K, M)  #scipy
    w = np.sqrt(V)
    T = 2*np.pi/w

    Sa_I = []
    Sa_E = []
    for i in range(len(V)):
        indices_I = [index for index, val in enumerate(SpecI[:, 0]) if round(val, 2) == round(T[i], 2)]
        indices_E = [index for index, val in enumerate(Spec[:, 0]) if round(val, 2) == round(T[i], 2)]
        
        Sa_I.append(SpecI[indices_I, 1])
        Sa_E.append(Spec[indices_E, 1])


    #Valor de aceleraciones espectrales correpondiente a T [Fracción de la gravedad]

    Lw = np.zeros(len(T))
    for i in range(len(T)):
        Lw[i] = D[:, i].T @ M @ r

    # # df_Lw = pd.DataFrame(Lw, columns=["Lw"])
    # # display(df_Lw)


    #Factor de excitación sísmica modal

    MT = np.sum(np.diag(M))
    M_e = np.zeros(len(T))

    for i in range(len(T)):
        M_e[i] = ((Lw[i]**2) / MT) * 100

    # # df_M_e = pd.DataFrame(M_e)
    # # display(df_M_e.style.set_caption('Masas efectivas'))


    #Masa efectiva [%]

    M_eacum = []
    M_eacum.append(M_e[0])

    for i in range(len(T)-1):
        M_eacum.append(M_eacum[i] + M_e[i+1])


    #Respuestas maximas modales
    g = 9.8
    qmax = np.zeros((gdl,gdl))
    for i in range(gdl):
        qmax[:,i] = ((Lw[i]*Sa_I[i]*g)/(V[i]))*(D[:,i])


    #Fuerzas Elásticas Máximas Modales ("Tiene Unidad")
    Qmax = np.zeros((gdl,gdl))
    for i in range(gdl):
        Qmax[:,i] = (Lw[i]*Sa_I[i]*g*M[i,i]*D[:,i])


    #Superposición modal
    #SRSS(Raíz cuadrada de la suma de los cuadrados)  &  #ABS(Suma)
    b = gdl #Numero de modos para la superposición (ver M_eacum al 90%): "))
    SR = np.zeros(gdl)
    abz = np.zeros(gdl)
    for i in range(gdl):
        for j in range(b):
            SR[i] = (Qmax[i,j]**2) + SR[i]
            abz[i] = np.abs(Qmax[i,j]) + abz[i]

    SRSS = np.sqrt(SR)
    aux33 = [abz,SRSS]

    # abz_tbl = pd.DataFrame(abz)
    # srss_tbl = pd.DataFrame(SR)
    # display(abz_tbl)
    # display(srss_tbl)


    #Distribución del cortante basal por piso
    F = ((SRSS+abz)/2)

    # tbl_F = pd.DataFrame(F)
    # display(tbl_F.style.set_caption('Distribución del cortante basal por piso'))

    ''' UTILIZAR SOLO SI EN CASO NO SE HA HECHO SUPERPOSICION PREVIAMENTE CON b '''
    '''¡¡¡ Debe ser estrictamente INFERIOR AL NUMERO DE MODOS DE VIBRACION ESCOGIDOS "<= b-1" !!!'''
    modo_vibracion = 0 

    # #Cortante Basal Maximo
    # print(f'El cortante basal máximo: {np.sum(F[:,modo_vibracion])}')

    # #Porcentaje de acuerdo al peso del edificio
    # p = MT*g
    # Porc =np.sum(F[:,modo_vibracion])*100/p
    # print(f'El Porcentaje de acuerdo al peso del edificio: {Porc}')

    # #Forma de la fuerza Normalizada para 3 modos de vibracion
    # F_n = []
    # for i in range(gdl):
    #     F_n.append(F[i,modo_vibracion]/np.max(F[:,modo_vibracion]))


    #Calculo de Derivas
    Derivas = []
    qmax = np.vstack((np.zeros(gdl), qmax))
    for i in range(gdl):
        Derivas.append((np.abs(qmax[i+1,modo_vibracion])-np.abs(qmax[i,modo_vibracion]))/H[0]*100)

    Derivas = np.flip(Derivas)
    Derivas_Pisos = np.column_stack((np.flip(np.arange(1, gdl+1)), Derivas))
    qmax = qmax[1:]

    return T, Sa_I, M_eacum, qmax, Qmax, F, Derivas_Pisos