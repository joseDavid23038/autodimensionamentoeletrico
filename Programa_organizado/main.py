import pandas as pd
import numpy as np

def disjuntor(disjuntores, I):
    for linha in disjuntores.itertuples():
        if linha.DISJUNTOR > I:
            return linha.DISJUNTOR

def bitola(disjuntor, tabela, bit, bitola_min, metodo):
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
    


if __name__ == "__main__":
    disjuntores = pd.read_excel("Dados\DISJUNTORES.xlsx")
    I = 7200/220
    print(disjuntor(disjuntores, I))