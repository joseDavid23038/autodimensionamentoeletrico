import pandas as pd
import numpy as np

tabela_disjuntores = pd.read_excel("Dados\DISJUNTORES.xlsx")
tabela_agrupamento = pd.read_excel("Dados\AGRUPAMENTO.xlsx")
tabela_temperatura = pd.read_excel("Dados\TEMPERATURA.xlsx")
tabela_inicial = pd.read_excel("Dados\DOIS_COBRE_PVC.xlsx")

def disjuntor(P, V, disjuntores = tabela_disjuntores ):
    I = P/V
    for linha in disjuntores.itertuples():
        coluna = "DISJUNTOR"
        if getattr(linha, coluna) > I:
            return getattr(linha, coluna)

def bitola(disjuntor, bitola_min, metodo, tabela = tabela_inicial):
    bit = 'SEÇÃO'
    I_max = tabela[metodo].values
    fios = tabela[bit].values
    finais = []
    for valor in I_max:
        if valor > disjuntor:
            finais.append(valor)
            break
    for valor in fios:
        if valor >= bitola_min:
            finais.append(valor)
            break
    return finais

# def dimensionar(tabela, metodo = 'B1', Bitola_min = 2.5, FT = 0.5, P = 1550, V = 220):
def fator_temperatura(condição, temperatura_ambiente, temperatura = tabela_temperatura):
    for temperatura in temperatura.iterrows():
        temperatura_usada = getattr(temperatura, condição)
        if getattr(temperatura, condição) > temperatura_ambiente:
            return temperatura_usada


def fator_agrupamento(n_circuitos, metodo, agrupamento = tabela_agrupamento):
    return agrupamento.loc[n_circuitos+1][metodo]

def fator_correcao(agrupamento, temperatura):
    return agrupamento*temperatura

    
if __name__ == "__main__":
    
    P=1550
    V=220
    print(disjuntor(P,V))