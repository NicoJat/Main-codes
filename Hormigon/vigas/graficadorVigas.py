import matplotlib.pyplot as plt

def grafVIG(b, Tramo, Ltotal, XmaxQ, XmaxF, XminQ, XminF, maxCortante, maxFlector, minCortante, minFlector, DFQ, DMF, X):

    #Graf. principal de fuerza cortante
    plt.figure(figsize=(11, 6))
    plt.plot(X, DFQ)
    plt.title('Diagrama de Fuerza Cortante', fontsize = 16, pad = 20)
    plt.xlabel('x [m]')
    plt.ylabel('Fuerza cortante [Tonf]')
    plt.axhline(linewidth = 3)
    plt.xlim(0, Ltotal)
    plt.grid()

    #Textos para valores máximos y mínimos
    LacumQ = 0
    for i in range(b):
        if i > 0:
            LacumQ += Tramo[i-1].L
        ubicMax = LacumQ + XmaxQ[i]
        ubicMin = LacumQ + XminQ[i]
        if ubicMax == Ltotal:
            ubicMax = Ltotal - Tramo[i].L/2
        if ubicMin == Ltotal:
            ubicMin = Ltotal - Tramo[i].L/2
        plt.text(ubicMax, maxCortante[i], '$Q_{max} = $' + \
                    str(round(maxCortante[i],2)) + '$Tonf$', fontsize=7)
        plt.text(ubicMin, minCortante[i], '$Q_{min} = $' + \
                    str(round(minCortante[i],2)) + '$Tonf$', fontsize=7)
            
    #Para sombrear el graf.
    Xgraf = [0] + X
    Xgraf.append(Ltotal)

    DFQgraf = [0] + DFQ
    DFQgraf.append(0)

    plt.fill(Xgraf, DFQgraf, 'b', alpha=0.3)

    #Divisores de tramos
    vertical = 0
    for i in range(b - 1):
        vertical += Tramo[i].L
        plt.axvline(vertical, color='black')

    plt.show()



    #Graf. principal
    plt.figure(figsize=(11, 6))
    plt.plot(X, DMF)
    plt.title('Diagrama de momento flector', fontsize = 16, pad=20)
    plt.xlabel('x [m]')
    plt.ylabel('Momento flector [Tonf*m]')
    plt.gca().invert_yaxis() #invierte el eje y
    plt.axhline(linewidth = 3)
    plt.xlim(0, Ltotal)
    plt.grid()

    #Colocar Textos de valores máximos y mínimos en flexión
    LacumM = 0
    for i in range(b):
        if i > 0:
            LacumM += Tramo[i-1].L
        ubicMax = LacumM + XmaxF[i]
        ubicMin = LacumM + XminF[i]
        if ubicMax == Ltotal:
            ubicMax = Ltotal - Tramo[i].L/2
        if ubicMin == Ltotal:
            ubicMin = Ltotal - Tramo[i].L/2
        plt.text(ubicMax, maxFlector[i], '$M_{max} = $' + \
                    str(round(maxFlector[i],2)) + '$Tonf*m$', fontsize=7)
        plt.text(ubicMin, minFlector[i], '$M_{min} = $' + str(round(minFlector[i],2)) + '$Tonf*m$', fontsize=7)
            
    #Para sombrear el graf.
    Xgraf = [0] + X
    Xgraf.append(Ltotal)

    DMFgraf = [0] + DMF
    DMFgraf.append(0)

    plt.fill(Xgraf, DMFgraf, 'b', alpha=0.3)

    #Divisores de tramos
    vertical = 0
    for i in range(b - 1):
        vertical += Tramo[i].L
        plt.axvline(vertical, color='black')

    plt.show()


