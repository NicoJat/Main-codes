import numpy as np
import pandas as pd

def Varillas(As,tolerancia):
    xlsx_file = 'Tablas de varillas1.xlsx'
    Varillas_normales = pd.read_excel(xlsx_file, sheet_name='Varillas normales')
    # display(Varillas_normales)

    V1_10 = Varillas_normales.iloc[1:14,0:12]
    Data1_10 = V1_10.to_numpy
    Datos1_10 = Data1_10()
    Datos1_10 = Datos1_10.astype(float)

    V11_20 = Varillas_normales.iloc[17:30,2:12]
    Datos11_20 = V11_20.to_numpy
    Datos11_20 = Datos11_20()
    Datos11_20 = Datos11_20.astype(float)

    Varillas_comp = np.concatenate((Datos1_10, Datos11_20), axis=1)
    # display(pd.DataFrame(Varillas_comp))

    NumVarillas = []
    phiVarillas = []
    Areas = []

    for i in range(12): # Máximo número de filas
        for j in range(20): # Máximo número de columnas
            if Varillas_comp[i+1, j+2] >= As and Varillas_comp[i+1, j+2] <= As + tolerancia:
                if Varillas_comp[i+1, 0] <= 12:
                    # Esto por si en caso existen combinaciones cuyas varillas sean inferiores o iguales a 12mm, estos son para estribos
                    pass
                else:
                    NumVarillas.append(Varillas_comp[0, j+2])
                    phiVarillas.append(Varillas_comp[i+1, 0])
                    Areas.append(Varillas_comp[i+1, j+2])
                    Varillas = np.column_stack((NumVarillas, phiVarillas, Areas))

    return Varillas




def Varillas_comb(As,tolerancia):

    xlsx_file = 'Tablas de varillas1.xlsx'
    Varillas_combinadas = pd.read_excel(xlsx_file, sheet_name='Varillas combinadas')

    #Combinadas
    V0_49 = Varillas_combinadas.iloc[0:50,0:17]
    Data0_49 = V0_49.to_numpy
    Datos0_49 = Data0_49()
    Datos0_49 = Datos0_49.astype(float)

    #Combinadas
    Varillas_comp_comb = Datos0_49
    #display(pd.DataFrame(Varillas_comp_comb))
    
    NumVarillas1 = []
    phiVarillas1 = []
    NumVarillas2 = []
    phiVarillas2 = []
    Areas_comb = []
    for i in range(48): #maximo numero de filas
        for j in range(15): #maximo numero de columnas
            if Varillas_comp_comb[i+2,j+2]>=As and Varillas_comp_comb[i+2,j+2]<=As+tolerancia:
                if Varillas_comp_comb[i+2,1]<=12 or Varillas_comp_comb[1,j+2]<=12 or Varillas_comp_comb[i+2,1]==0:
                    '''Esto por si en caso existen combinaciones cuyas varillas 
                    sean inferiores o iguales a 12mm, estos son para estribos.'''
                    pass
                else:
                    if (i+2)<7 and (i+2)>2:
                        NumVarillas1.append(Varillas_comp_comb[i+2,0])
                        phiVarillas1.append(Varillas_comp_comb[i+2,1])
                        NumVarillas2.append(Varillas_comp_comb[0,j+2])
                        phiVarillas2.append(Varillas_comp_comb[1,j+2])
                        Areas_comb.append(Varillas_comp_comb[i+2,j+2])
                        Varillas_comb = np.column_stack((NumVarillas1,phiVarillas1,NumVarillas2,phiVarillas2,Areas_comb))
                    elif (i+2)<13 and (i+2)>7:
                        NumVarillas1.append(Varillas_comp_comb[i+2,0])
                        phiVarillas1.append(Varillas_comp_comb[i+2,1])
                        NumVarillas2.append(Varillas_comp_comb[0,j+2])
                        phiVarillas2.append(Varillas_comp_comb[7,j+2])
                        Areas_comb.append(Varillas_comp_comb[i+2,j+2])
                        Varillas_comb = np.column_stack((NumVarillas1,phiVarillas1,NumVarillas2,phiVarillas2,Areas_comb))
                    elif (i+2)<19 and (i+2)>13:
                        NumVarillas1.append(Varillas_comp_comb[i+2,0])
                        phiVarillas1.append(Varillas_comp_comb[i+2,1])
                        NumVarillas2.append(Varillas_comp_comb[0,j+2])
                        phiVarillas2.append(Varillas_comp_comb[13,j+2])
                        Areas_comb.append(Varillas_comp_comb[i+2,j+2])
                        Varillas_comb = np.column_stack((NumVarillas1,phiVarillas1,NumVarillas2,phiVarillas2,Areas_comb))
                    elif (i+2)<25 and (i+2)>19:
                        NumVarillas1.append(Varillas_comp_comb[i+2,0])
                        phiVarillas1.append(Varillas_comp_comb[i+2,1])
                        NumVarillas2.append(Varillas_comp_comb[0,j+2])
                        phiVarillas2.append(Varillas_comp_comb[19,j+2])
                        Areas_comb.append(Varillas_comp_comb[i+2,j+2])
                        Varillas_comb = np.column_stack((NumVarillas1,phiVarillas1,NumVarillas2,phiVarillas2,Areas_comb))
                    elif (i+2)<32 and (i+2)>26:
                        NumVarillas1.append(Varillas_comp_comb[i+2,0])
                        phiVarillas1.append(Varillas_comp_comb[i+2,1])
                        NumVarillas2.append(Varillas_comp_comb[0,j+2])
                        phiVarillas2.append(Varillas_comp_comb[26,j+2])
                        Areas_comb.append(Varillas_comp_comb[i+2,j+2])
                        Varillas_comb = np.column_stack((NumVarillas1,phiVarillas1,NumVarillas2,phiVarillas2,Areas_comb))
                    elif (i+2)<38 and (i+2)>32:
                        NumVarillas1.append(Varillas_comp_comb[i+2,0])
                        phiVarillas1.append(Varillas_comp_comb[i+2,1])
                        NumVarillas2.append(Varillas_comp_comb[0,j+2])
                        phiVarillas2.append(Varillas_comp_comb[32,j+2])
                        Areas_comb.append(Varillas_comp_comb[i+2,j+2])
                        Varillas_comb = np.column_stack((NumVarillas1,phiVarillas1,NumVarillas2,phiVarillas2,Areas_comb))
                    elif (i+2)<44 and (i+2)>38:
                        NumVarillas1.append(Varillas_comp_comb[i+2,0])
                        phiVarillas1.append(Varillas_comp_comb[i+2,1])
                        NumVarillas2.append(Varillas_comp_comb[0,j+2])
                        phiVarillas2.append(Varillas_comp_comb[38,j+2])
                        Areas_comb.append(Varillas_comp_comb[i+2,j+2])
                        Varillas_comb = np.column_stack((NumVarillas1,phiVarillas1,NumVarillas2,phiVarillas2,Areas_comb))
                    elif (i+2)<50 and (i+2)>44:
                        NumVarillas1.append(Varillas_comp_comb[i+2,0])
                        phiVarillas1.append(Varillas_comp_comb[i+2,1])
                        NumVarillas2.append(Varillas_comp_comb[0,j+2])
                        phiVarillas2.append(Varillas_comp_comb[44,j+2])
                        Areas_comb.append(Varillas_comp_comb[i+2,j+2])
                        Varillas_comb = np.column_stack((NumVarillas1,phiVarillas1,NumVarillas2,phiVarillas2,Areas_comb))

    return Varillas_comb

