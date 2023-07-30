#pip install openpyxl
pip install pandas

import pandas as pd
import numpy as np

tabela_disjuntores = pd.read_excel("Dados/DISJUNTORES.xlsx")
tabela_agrupamento = pd.read_excel("Dados/AGRUPAMENTO.xlsx")
tabela_temperatura = pd.read_excel("Dados/TEMPERATURA.xlsx")

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


def disjuntor_inicial(P, V, disjuntores = tabela_disjuntores ):
    """
    args:
        P: Potência 
        V: Tensão
        disjuntores: A tabela de disjuntores a ser usada na análise (opcional)
    returns: 
        O disjuntor adequado para as condições especificadas.
    """
    I = P/V
    for linha in disjuntores.itertuples(): # Itera linha por linha na tabela de disjuntores
        coluna = "DISJUNTOR"
        if getattr(linha, coluna) > I:
            return getattr(linha, coluna)



# def dimensionar(tabela, metodo = 'B1', Bitola_min = 2.5, FT = 0.5, P = 1550, V = 220):
def fator_temperatura(condicao, temperatura_ambiente):
    """
    args:
        condicao: Condição de instalação
        temperatura_ambiente: Temperatura média do amibiente. 
        Fator de temperatura.
    """
    coluna_temperatura = 'TEMPERATURA'
    linha_fator_temperatura = 0
    temperatura = tabela_temperatura

    maior_temperatura_mais_proxima = temperatura.loc[linha_fator_temperatura][coluna_temperatura]

    while float(maior_temperatura_mais_proxima)<= temperatura_ambiente:
        linha_fator_temperatura = linha_fator_temperatura+1
        maior_temperatura_mais_proxima = temperatura.loc[linha_fator_temperatura][coluna_temperatura]
        fator_temperatura = temperatura.loc[linha_fator_temperatura][condicao]
    return float(fator_temperatura)


def fator_agrupamento(n_circuitos, metodo, agrupamentos = tabela_agrupamento):
    """
    args:
        n_circuitos: Número de circuitos a serem considerados.
        Método: Método de instalação usado.
        agrupamentos: A tabela de agrupamento a ser usada na análise.
    returns: 
        Fator de temperatura.
    """
    return agrupamentos.loc[n_circuitos+1][metodo]

def fator_correcao(agrupamento, temperatura):
    """
    args:
        agrupamento: O fator de agrupamento.
        temperatura: O fator de temperatura
    returns: 
        Fator de agrupamento.
    """
    return agrupamento*temperatura

def bitola_min(tipo_instalacao): # Essa função determina o valor mínimo a ser comparado na função seguinte. Apenas usada em lógica interna.
    if tipo_instalacao == "Iluminação": 
        bitola_min = 1.5
    if tipo_instalacao == "Tomadas de Uso Específico" or tipo_instalacao =="Tomadas de Uso Geral":
        bitola_min = 2.5
    return bitola_min
    
def bitola(disjuntor, bitola_min, metodo, correcao, isolamento): 
    """
    args:
        disjuntor: A bitola deve suportar uma corrente superior a que desarma disjuntor e por isso, o disjuntor é o referencial inicial para o bitola
        bitola_min: circuitos de iluminação têm bitola mínima de 1,5mm enquanto os de tomada têm de 2,5mm. Isso serve para as pessoas não pegarem fio mais fino.
        metodo: Método de instalação 
        correcao: O fator de correção reduz o 
        isolamento: Referente ao tipo de isolamento. Se o fio é de EPR ou PVC, isso implica sobre o aquecimento e o fator de correção deste.
    returns: 
        finais: lista com disjuntor final e tamanho ideal de bitola.
    """
    tabela_usada = tabela_a_ser_usada(isolamento)
    if tabela_usada == "DOIS_COBRE_PVC.xlsx":
        tabela = pd.read_excel("Dados\\DOIS_COBRE_PVC.xlsx")
    if tabela_usada == "DOIS_COBRE_EPR_XLPE.xlsx":
        tabela = pd.read_excel("Dados\\DOIS_COBRE_EPR_XLPE.xlsx")
    bit = 'SEÇÃO'
    I_max = correcao * tabela[metodo].values
    fios = tabela[bit].values
    finais = []

    # checa a tabela até achar o valor certo de corrente, 
    # e então, na mesma linha, seleciona o tamanho do fio.
    for valor, secao in zip(I_max, fios):
        if valor > disjuntor:
            finais.append(valor)
            if secao >= bitola_min:
                finais.append(secao)
            else:
                # Isso é pra caso o tamanho observado seja menor que o mínimo
                for valor in fios:
                    if valor >= bitola_min:
                        finais.append(valor)
                        break
            break
    return finais


if __name__ == "__main__":
    #Esse parte serve apenas como teste de funcionamento das funções
   '''''
    metodo = "A1"
    tipo_instalacao = "Iluminação"
    tensao = 127
    potencia = 2000
    num_circuitos = 4
    isolamento = "PVC"
    local = "Parede"
    temperatura_ambiente = 55 


    condicao = condicao_de_instalacao(isolamento,local)
    disjuntores = tabela_disjuntores
    disjuntor = disjuntor_inicial(potencia, tensao, disjuntores)
    ftemperatura = fator_temperatura(condicao, temperatura_ambiente)
    agrupamento = fator_agrupamento(num_circuitos, metodo, agrupamentos = tabela_agrupamento)
    correcao = fator_correcao(agrupamento, ftemperatura)
    print(correcao)
    bitola_mn = bitola_min(tipo_instalacao)
    secao = bitola(disjuntor, bitola_mn, metodo, correcao, isolamento)
    print(secao[1])
    '''''
