tabela_usada = "DOIS_COBRE_PVC.xlsx" 
metodo = 'B1'
bitolaMin = 2.5
FT = 0.5
P=1550
V=220
I = P/V
#print(I)

import pandas as pd
tabela_inicial = pd.read_excel(tabela_usada)
#print(tabela_inicial)

tabela = tabela_inicial.copy()
tabela[metodo] = tabela[metodo]*FT
#print(tabela)

disjuntores = pd.read_excel("DISJUNTORES.xlsx")
#print(disjuntores)

coluna_disjuntor = 'DISJUNTOR'
linha_disjuntor = 0

disjuntor = disjuntores.loc[linha_disjuntor][coluna_disjuntor]

while float(disjuntor)<= I:
    linha_disjuntor = linha_disjuntor+1
    disjuntor = disjuntores.loc[linha_disjuntor][coluna_disjuntor]

print("Disjuntor de:",disjuntor,"amperes")

bit = 'SEÇÃO'
linha_bitola = 0

Imax = tabela.loc[linha_bitola][metodo]
fio = tabela.loc[linha_bitola][bit]

while float(Imax) <= disjuntor:
    linha_bitola = linha_bitola+1
    Imax = tabela.loc[linha_bitola][metodo]
    fio = tabela.loc[linha_bitola][bit]

while float(fio)<bitolaMin:
    linha_bitola = linha_bitola+1
    Imax = tabela.loc[linha_bitola][metodo]
    fio = tabela.loc[linha_bitola][bit]

print("Fio de:",fio,"mm2, que suporta até:",Imax,"amperes")