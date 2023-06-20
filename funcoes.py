import pandas as pd #importa a biblioteca pandas (utilizada para analisar e organizar os dados)
import numpy as np #importa a biblioteca numpy (utilizada para realizar os cálculos necessários para o dimensionamento elétrico)

import pip #importa o pip, um gerenciador das bibliotecas que iremos utilizar
pip.main(["install", "openpyxl"]) #instala a biblioteca openpyxl, que consegue acessar, ler e criar arquivos .xlsx (Excel)

tabela_disjuntores = pd.read_excel("Dados/DISJUNTORES.xlsx") #acessa, por meio da biblioteca pandas, a tabela com os dados sobre disjuntores
tabela_agrupamento = pd.read_excel("Dados/AGRUPAMENTO.xlsx") #acessa, por meio da biblioteca pandas, a tabela com os dados sobre o agrupamento de fios
tabela_temperatura = pd.read_excel("Dados/TEMPERATURA.xlsx") #acessa, por meio da biblioteca pandas, a tabela com os dados sobre a temperatura do ambiente

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
    return pd.read_excel(tabela_usada)


def disjuntor_inicial(P, V, disjuntores = tabela_disjuntores):
    """
    Calcula o valor da intensidade de corrente. 
    Args:
        P: Potência 
        V: Tensão
        Disjuntores: A tabela de disjuntores a ser usada na análise (opcional)
    Returns: 
        O disjuntor adequado para as condições especificadas.
    """
    I = P/V #Calcula a intensidade de corrente (I), a partir dos argumentos P e V dados pelo usuário
    for linha in disjuntores.itertuples(): #Itera a tabela de disjuntores pelo método .itertuples()
        coluna = "DISJUNTOR" 
        if getattr(linha, coluna) > I: #O método getattr analisa os valores da tabela. Se o valor obtido através da tabela for maior que o I
            return getattr(linha, coluna) #Retorna o disjuntor adequado



# def dimensionar(tabela, metodo = 'B1', Bitola_min = 2.5, FT = 0.5, P = 1550, V = 220):
def fator_temperatura(condicao, temperatura_ambiente, temperaturas = tabela_temperatura):
    """
    Args:
        condicao: Condição de instalação
        temperatura_ambiente: Temperatura média do amibiente. 
        temperaturas: A tabela de temperatura a ser usada na análise.
    Returns: 
        Fator de temperatura.
    """
    for temperatura in temperaturas.itertuples():
        temperatura_usada = getattr(temperatura, condicao)
        if temperatura_usada > temperatura_ambiente:
            return temperatura_usada


def fator_agrupamento(n_circuitos, metodo, agrupamentos = tabela_agrupamento):
    """
    Args:
        n_circuitos: Número de circuitos a serem considerados.
        Método: Método de instalação usado.
        agrupamentos: A tabela de agrupamento a ser usada na análise.
    Returns: 
        Fator de temperatura.
    """
    return agrupamentos.loc[n_circuitos+1][metodo]

def fator_correcao(agrupamento, temperatura):
    """
    Args:
        agrupamento: O fator de agrupamento.
        temperatura: O fator de temperatura
    Returns: 
        Fator de agrupamento.
    """
    return agrupamento*temperatura

def bitola_min(tipo_instalacao):
    if tipo_instalacao == "Iluminação":
        bitola_min = 1.5
    if tipo_instalacao == "Tomada de Uso Específico" or tipo_instalacao =="Tomadas de Uso Geral":
        bitola_min = 2.5
    return bitola_min

def bitola(disjuntor, bitola_min, metodo, correcao, isolamento):
    """
    args:
        disjuntor: 
        bitola_min: 
        metodo: Método de instalação
        correcao: 
        isolamento:
    returns: 
        finais: lista com disjuntor final e tamanho ideal de bitola.
    """
    tabela = tabela_a_ser_usada(isolamento)
    bit = 'SEÇÃO'
    I_max = correcao * tabela[metodo].values
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


if __name__ == "__main__":
    
    '''metodo = "A1"
    tipo_instalacao = "Iluminação"
    tensao = 127
    potencia = 500
    num_circuitos = 4
    isolamento = "PVC"
    local = "Parede"
    temperatura = 60 '''

   
    condicao = condicao_de_instalacao(isolamento,local)
    disjuntores = tabela_disjuntores
    disjuntor = disjuntor_inicial(potencia, tensao, disjuntores)
    temperaturas = tabela_temperatura
    ftemperatura = fator_temperatura(condicao, temperatura, temperaturas)
    agrupamentos = tabela_agrupamento
    agrupamento = fator_agrupamento(num_circuitos, metodo, agrupamentos)
    correcao = fator_correcao(agrupamento, ftemperatura)
    bitola_mn = bitola_min(tipo_instalacao)
    secao = bitola(disjuntor, bitola_mn, metodo, correcao, isolamento)
    print(secao)
