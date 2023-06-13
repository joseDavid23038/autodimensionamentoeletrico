metodo = 'B1'
bitolaMin = 2.5
P=7200
V=127
I = P/V
n_circuitos = 3
temperatura_ambiente = 30
isolamento = "PVC"
local = "Teto"

#Tratamento de dados coletados
tabela_usada  = ""
condicao  = ""

#Funçaõ para condição e tbela escolhida
def condicao_de_instalacao(isolamento,local):
    if isolamento == "PVC" and (local == "Teto" or local =="Parede"):
       condicao = 'PVCAMBIENTE'
    if isolamento == "PVC" and local == "Solo":
       condicao = 'PVCSOLO'
    if (isolamento == "EPR" or isolamento == "XLPE") and (local == "Teto" or local =="Parede"):
       condicao = 'EPRAMBIENTE'
    if (isolamento == "EPR" or isolamento == "XLPE") and (local == "Solo"):
       condicao = 'EPRSOLO'
    return condicao

def tabela_a_ser_usada(isolamento):
    if isolamento == "PVC":
        tabela_usada = "DOIS_COBRE_PVC.xlsx" 
    if isolamento == "XLPE" or isolamento == "EPR":
        tabela_usada = "DOIS_COBRE_EPR_XLPE.xlsx" 
    return tabela_usada

#Chamando a função
condicao = condicao_de_instalacao(isolamento,local)
tabela_usada = tabela_a_ser_usada(isolamento)


import pandas as pd
tabela_inicial = pd.read_excel(tabela_usada)
#print(tabela_inicial)

disjuntores = pd.read_excel("DISJUNTORES.xlsx")
#print(disjuntores)

temperatura = pd.read_excel("TEMPERATURA.xlsx")
#print(temperatura)

agrupamento = pd.read_excel("AGRUPAMENTO.xlsx")


#Fator de correção
coluna_temperatura = 'TEMPERATURA'
linha_fator_temperatura = 0

maior_temperatura_mais_proxima = temperatura.loc[linha_fator_temperatura][coluna_temperatura]

while float(maior_temperatura_mais_proxima)<= temperatura_ambiente:
    linha_fator_temperatura = linha_fator_temperatura+1
    maior_temperatura_mais_proxima = temperatura.loc[linha_fator_temperatura][coluna_temperatura]
    fator_temperatura = temperatura.loc[linha_fator_temperatura][condicao]
    
fator_agrupamento = agrupamento.loc[n_circuitos+1][metodo]    

fator_de_correcao = fator_agrupamento*fator_temperatura
print(fator_de_correcao)

#Disjuntor
coluna_disjuntor = 'DISJUNTOR'
linha_disjuntor = 0

disjuntor = disjuntores.loc[linha_disjuntor][coluna_disjuntor]

while float(disjuntor)<= I:
    linha_disjuntor = linha_disjuntor+1
    disjuntor = disjuntores.loc[linha_disjuntor][coluna_disjuntor]

print("Disjuntor de:",disjuntor,"amperes")


#Seção do 
bit = 'SEÇÃO'
linha_bitola = 0

tabela = tabela_inicial.copy()
tabela[metodo] = tabela[metodo]*fator_de_correcao
#print(tabela)

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