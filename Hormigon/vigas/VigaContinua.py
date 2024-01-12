import numpy as np
import matplotlib.pyplot as plt


class VigaB:
    '''Definimos un tramo de viga.
    E: Módulo de elasticidad
    I: Inercia de la sección transversal
    L: Longitud del tramo'''
    def __init__(self, E, I, L):
        '''ATRIBUTOS:
            self.E: Módulo de elasticidad
            self.I: Inercia de la sección transversal
            self.L: Longitud del tramo
            self.k: matriz de rigidez del tramo'''
        self.E = E
        self.I = I
        self.L = L
        
        #Matriz de rigidez del elemento
        self.k = E * I / L**3 * np.array([
                [12., 6*L, -12, 6*L],
                [6*L, 4*L**2, -6*L, 2*L**2],
                [-12, -6*L, 12, -6*L],
                [6*L, 2*L**2, -6*L, 4*L**2]
            ])
        

class Carga:
    '''Clase carga'''
    def __init__(self, tipo):
        '''
        tipo = 0: Carga puntual
        tipo = 1: Carga distribuida
        tipo = 2: Momento cocentrado
        '''
        self.tipo = tipo
    
    def Tipo(self):
        if self.tipo == 0:
            print("Carga puntual")
        elif self.tipo == 1:
            print('Carga distribuida')
        elif self.tipo == 2:
            print('Momento concentrado')
        else:
            print('No definido')


class CargaPuntual(Carga):
    '''Clase carga puntual'''
    def __init__(self, P=0, a=0):
        '''Carga puntual P.
        P: valor de la carga. Positivo hacia abajo.
        a: posicion de la carga respecto al extremo izquierdo del tramo.'''
        Carga.__init__(self, 0)
        self.P = P
        self.a = a
    
    def __str__(self):
        return 'Carga puntual\n   Valor= ' + str(self.P) + 'N' \
    + '\n   Posición, x= ' + str(self.a) + 'm'
    
    #Reacciones nodales equivalentes
    def Qf(self, L):
        '''Reacciones nodales equivalentes para una carga puntual.
        L: Longitud de la viga'''
        a = self.a
        b = L - a
        return self.P / L**2 * np.array([
                [b**2 / L * (3*a + b)],
                [a * b**2],
                [a**2 / L * (a + 3*b)],
                [-a**2 * b]
            ])
    
    #Fuerza cortante en una sección (viga sin apoyos)
    def FQ(self, x, L):
        '''Aporte a la fuerza cortante en una sección debido a una carga puntual,
        x: posición de la sección considerada respecto al extremo izquierdo
        L: longitud del tramo'''
        if self.a < x <= L:
            return -self.P
        else:
            return 0
         
    #Momento flector en una sección (viga simplemente apoyada)
    def MF(self, x, L):
        '''Aporte al Momento flector en una sección debido a una carga puntual,
        x: posición de la sección considerada respecto al extremo izquierdo
        L: longitud del tramo'''
        if 0 <= x < self.a:
            return (1 - self.a/L) * self.P * x
        elif x <= L:
            return self.a * self.P * (1 - x/L)
        else:
            return 0
        

class CargaDistribuida(Carga):
    '''Clase carga distribuida'''
    def __init__(self, q=0, a=0, l=0):
        '''Carga puntual P.
        P: valor de la carga. Positivo hacia abajo.
        a: distancia entre el extremo izquierdo del tramo y el inicio de la carga.
        l: longitud de la carga distribuida'''
        Carga.__init__(self, 1)
        self.q = q
        self.a = a
        self.l = l
    
    def __str__(self):
        return 'Carga distribuida\n   Valor= ' + str(self.q) + 'N/m'\
    ', ' + '\n   Inicio= ' + str(self.a) + 'm' + '\n   Longitud= ' + str(self.l) + 'm'
    
    def Qf(self, L):
        '''Reacciones nodales equivalentes para una carga
        unifomemente distribuida.
        L: longitud de la viga'''
        q = self.q
        a = self.a
        b = L - self.a - self.l
        return q * L / 2 * np.array([
                [1 - a/L**4*(2*L**3 - 2*a**2*L + a**3) - b**3/L**4*(2*L - b)],
                [L/6*(1 - a**2/L**4*(6*L**2 - 8*a*L + 3*a**2) - b**3/L**4*(4*L - 3*b))],
                [1 - a**3/L**4*(2*L - a) - b/L**4*(2*L**3 - 2*b**2*L + a**3)],
                [-L/6*(1 - a**3/L**4*(4*L - 3*a) - b**2/L**4*(6*L**2 - 8*b*L + 3*b**2))]
            ])
            
    #Fuerza cortante en una sección (viga sin apoyos)
    def FQ(self, x, L):
        '''Aporte a la fuerza cortante en una sección debido a la carga distribuida.
        x: posición de la sección considerada respecto al extremo izquierdo
        L: Longitud del tramo'''
        if self.a <= x < self.a + self.l:
            return -self.q * (x - self.a)
        elif x <= L:
            return -self.q * self.l
        else:
            return 0
    
    #Momento flector en una sección (viga simplemente apoyada)
    def MF(self, x, L):
        '''Aporte al momento flector en una sección debido a la carga distribuida.
        x: posición de la sección considerada respecto al extremo izquierdo
        L: Longitud del tramo'''
        V1 = self.q*self.l/L*(L - self.a - self.l/2)
        V2 = self.q*self.l - V1
        if 0 <= x < self.a:
            return V1 * x
        elif x <= self.a + self.l:
            return V1*x - 0.5*self.q*(x-self.a)**2
        elif x <= L:
            return V2 * (L - x)
        else:
            return 0
        

class MomentoConcentrado(Carga):
    '''Clase momento concentrado'''
    def __init__(self, M=0, a=0):
        '''Momento concentrado M.
        M: valor del momento concentrado. Antihorario positivo
        a: posición del momento respecto al extremo izquierdo del tramo'''
        Carga.__init__(self, 2)
        self.M = M
        self.a = a
    
    def __str__(self):
        return 'Momento concentrado\n   Valor= ' + str(self.M) + 'Nm' \
    + '\n   Posición, x= ' + str(self.a) + 'm'
    
    def Qf(self, L):
        '''Reacciones nodales equivalentes para un momento concetrado.
        L: longitud de la viga'''
        a = self.a
        b = L - a
        return self.M / L**2 * np.array([
                [-6*a*b/L],
                [b*(b - 2*a)],
                [6*a*b/L],
                [a*(a - 2*b)]
            ])
    
    #Fuerza cortante en una sección (viga sin apoyos)
    def FQ(self, x, L):
        '''Aporte a la fuerza cortante en una sección debido a la carga distribuida.
        x: posición de la sección considerada respecto al extremo izquierdo'''
        return 0
    
    #Momento flector en una sección (viga simplemente apoyada)
    def MF(self, x, L):
        '''Aporte al momento flector en una sección debido a un momento concetrado,
        Estos valores corresponden al de una viga simplemente apoyada.
        x: posición de la sección considerada respecto al extremo izquierdo
        L: Longitud del tramo'''
        if 0 <= x < self.a:
            return self.M / L * x
        elif self.a < x <= L:
            return self.M * (x/L - 1)
        else:
            return 0
        


#########################
def calcVIG(Tramo, cargas, apoyoIzq, apoyoDer, b, nudos, K, C):
    #Longitud total de la viga
    Ltotal = 0
    for i in range(b):
        Ltotal += Tramo[i].L


    #Los grados de libertad restringidos son:
    gdlRest = []

    #En general
    for i in range(b):
        gdlRest.append(2*i)
        
    #Extremo izquierdo
    if apoyoIzq == 0: #empotramiento
        gdlRest.insert(1, 1)
    elif apoyoIzq == 1: #restricción al giro
        gdlRest[0] = 1
    elif apoyoIzq == 3: #voladizo
        del gdlRest[0]
    else: #apoyo de segundo grado
        pass

    #Extremo derecho
    if apoyoDer == 0: #empotramiento
        gdlRest.append(2*b)
        gdlRest.append(2*b + 1)
    elif apoyoDer == 1: #restricción al giro
        gdlRest.append(2*b + 1)
    elif apoyoDer == 2: #apoyo de segundo género
        gdlRest.append(2*b)
    else: #voladizo
        pass


    #Número de reacciones (grados de libertad restringidos)
    r = len(gdlRest)

    #Desplazamiento de apoyos (vector columna r x 1)
    a = np.zeros(r)



    #Modificación de la matriz de rigidez por el enfoque de penalización
    S = K
    cont = 0 #contador para identificar los elementos de C
    for i in gdlRest:
        S[i,i] += C[cont]
        cont += 1


    #Reacciones nodales equivalentes en cada tramo
    QF = [0]*b #para guardar los vectores de reacciones nodales equivalentes de cada tramo

    for i in range(b): #recorre todos los tramos
        for j in range(len(cargas[i])): #considera todas las cargas de cada tramo
            QF[i] += cargas[i][j].Qf(Tramo[i].L)


    #Ensamble del vector Qf para todos los gdl, incluidos los restringidos
    Qf = np.zeros((2*nudos,1))
    for i in range(b):
        Qf[2*i:2*i+4,:] += QF[i]


    #Modificación del vector de cargas por el enfoque de penalización
    P = Qf
    for i in range(r):
        P[gdlRest[i],0] = Qf[gdlRest[i],0] + C[i,0] * a[i]


    #Desplazamientos nodales
    d = -np.linalg.inv(S) @ P

    #Desplazamientos nodales por tramo
    u = []
    for i in range(b):
        u.append(d[2*i:2*i+4,:])


    #Fuerzas en cada tramo
    F = []
    for i in range(b):
        F.append(Tramo[i].k @ u[i] + QF[i])

    #Reacciones
    δ = d[gdlRest]
    R = -C * (δ - a)

    #Número de secciones a tomar para los gráficos en cada tramo
    numS = 100
    Xt = [] #para guardar las x de cada tramo
    for i in range(b):
        Xt.append(np.linspace(0, Tramo[i].L, numS)) #Ubicación de las secciones


    Cortantes = []
    for i in range(b): #para cada tramo
        
        #Cortantes como vigas sin apoyo
        Q0 = np.zeros(numS)
        for j in range(len(cargas[i])): #considera todas las cargas de cada tramo
            m = 0 #para enumerar las secciones
            for x in Xt[i]: #recorre las secciones
                Q0[m] += cargas[i][j].FQ(x, Tramo[i].L)
                m += 1
        
        #Cortantes en el extremo izquierdo, obtenido del cálculo
        Q1 = F[i][0]
        
        #Cortante total
        Cortantes.append(Q0 + Q1)


    #Máximos y mínimos valores de fuerza cortante (en cada tramo)
    maxCortante = [] #Cortantes máximos por cada tramo
    minCortante = [] #Cortantes mínimos por cada tramo
    XmaxQ= [] #ubicaciones de los máximos en cada tramo
    XminQ = [] #ubicaciones de los mínimos en cada tramo
    for i in range(b):
        maxQ = max(Cortantes[i]) #Máximo cortante
        minQ = min(Cortantes[i]) #Mínimo cortante
        maxCortante.append(maxQ)
        minCortante.append(minQ)
        indMaxQ = np.where(Cortantes[i] == maxQ )[0][0] #ubicación del máximo cortante
        indMinQ = np.where(Cortantes[i] == minQ )[0][0] #ubicación del mínimo cortante
        XmaxQ.append(Xt[i][indMaxQ])
        XminQ.append(Xt[i][indMinQ])


    Flectores = []
    for i in range(b): #para cada tramo
        
        #Momentos como tramos simplemente apoyados
        M0 = np.zeros(numS)
        for j in range(len(cargas[i])): #considera todas las cargas de cada tramo
            m = 0 #para enumerar las secciones
            for x in Xt[i]: #recorre las secciones
                M0[m] += cargas[i][j].MF(x, Tramo[i].L)
                m += 1
        
        #Momentos debidos a los empotramientos o a la continuidad de la viga
        M1 = -F[i][1] + (F[i][3] + F[i][1]) / Tramo[i].L * Xt[i]
        
        #Momento total
        Flectores.append(M0 + M1)


    #Máximos y mínimos valores de momento flector (en cada tramo)
    maxFlector = [] #Flector máximo en cada tramo
    minFlector = [] #Flector mínimo en cada tramo
    XmaxF= [] #ubicaciones de los flectores máximos por tramo
    XminF = [] #ubicaciones de los mínimos flectores por tramo
    for i in range(b):
        maxF = max(Flectores[i]) #Máximo flector
        minF = min(Flectores[i]) #Mínimo flector
        maxFlector.append(maxF)
        minFlector.append(minF)
        indMaxF = np.where(Flectores[i] == maxF )[0][0] #ubicación del máximo flector
        indMinF = np.where(Flectores[i] == minF )[0][0] #ubicación del mínimo flector
        XmaxF.append(Xt[i][indMaxF])
        XminF.append(Xt[i][indMinF])


    #Valores de x para los gráficos
    X = []
    Lacum = 0
    for i in range(b):
        if i > 0:
            Lacum += Tramo[i-1].L
        Xprov = Xt[i] + Lacum
        Xlist = Xprov.tolist()
        X += Xlist


    #Valores de la fuerza cortante para los gráficos
    DFQ = []
    for i in range(b):
        #Valores para el DFQ tipo lista
        Corta = (Cortantes[i]).tolist()
        DFQ += Corta




    #Valores del momento flector para los gráficos
    DMF = []
    for i in range(b):
        #Valores para el DMF tipo lista
        Flex = (Flectores[i]).tolist()
        DMF += Flex


    return Ltotal, XmaxQ, XmaxF, XminQ, XminF, maxCortante, maxFlector, minCortante, minFlector, DFQ, DMF, X