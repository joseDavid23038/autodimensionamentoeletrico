#Importando Bibliotecas____________________________________________________________________________________________________________________________________________________________
import streamlit as st
#Importando funcoes.py
import os
import pandas as pd

from funcoes import *

# Configurando a Página_______________________________________________________________________________________________________________________________________________________
st.set_page_config(page_title="Redimensionamento", layout="wide", page_icon="U&#x26A1;",initial_sidebar_state="collapsed")

#______________________________________________________________________________________________________________________________________________________________________________


# Criando uma Barra Lateral ________________________________________________________________________________________________________________________________________________________
bar = st.sidebar 
bar.title("Contato:") #Adicionamos o contato para que o usuário possa sanar suas dúvidas, além da página do github para que possa ver como o código foi estruturado
bar.write('''
Envie suas dúvidas ou sugestões para nós por e-mail!
Houve algum erro durante a utilização? Nos informe.
e-mails para contato: 
danielbravin@hotmail.com
emelyn.a.ilum@gmail.com
programming.gustamatos@gmail.com 
jose23038@ilum.cnpem.br
[GitHub da Página](https://github.com/MrBravin/autodimensionamentoeletrico/edit/main/teste.py)
''')

#_______________________________________________________________________________________________________________________________________________________________________________

st.title("Autodimensionamento elétrico")   #Essa função define um título, basicamente, uma string com uma edição específica.

st.divider()                   #A função "divider" é usada para criar um corte cinza na tela, meramente para melhor organização dos itens. 

with st.expander("About Us"):  #Aqui a função expander, cria um item que ao ser clicado se expande mostrando quaisquer itens que se deseja, seja um texto ou um botão.  
  st.markdown("""
  # Sobre o Projeto:

  ### Esse projeto foi criado a fim de auxiliar o dimensionamento de circuitos elétricos residenciais no Brasil. 
  Com o objetivo de evitar possíveis acidentes ocasionados por desinstrução ou falha humana e facilitar o cálculo de dimensionamento elétrico, 
  criamos este site para que você possa fazer o autodimensionamento elétrico da sua casa! Nós analizamos as variáveis necessárias para o dimesionamento,
  as comparamos com a NBR5410 e, como resultado, indicamos para você o [disjuntor](https://pt.wikipedia.org/wiki/Disjuntor) e da [seção transversal do fio](https://www.mundodaeletrica.com/bitola-de-fios-como-identificar/#:~:text=A%20se%C3%A7%C3%A3o%20transversal%20do%20cabo,n%C3%A3o%20%C3%A9%20a%20melhor%20defini%C3%A7%C3%A3o.) a serem utilizados na sua casa! 
  Autodimensione e fique seguro! 
  
  Criadores e idealizadores:  
  - Daniel Bravin  
  - Gustavo Matos  
  - Emelyn Alves
  - José David  
  
  """) 
st.divider()  


entrada, saida = st.tabs(["Dados","Resultado"])  # Criando Duas telas, Dados e Resultado, respectivamente. 

# Criando a aba Dados________________________________________________________________________________________________________________________________________________________
with entrada: 
  st.markdown('''

    # Bem-vind@!

    Essa aba é direcionada para armazenar as informações do seu circuito elétrico, que serão usadas para encontrar o disjuntor e bitola do fio (seção transversal) ideais para o seu sistema.
    Lembre-se: A armação e montagem de todo aparato elétrico deve ser realizada por um profissional, nosso trabalho é apenas encontrar uma escala de produto que satisfaça suas necessidades.
    Contudo, o material e contas disponibilizados ainda devem ser revisados por um profisional certificado. Vamos começar? 

    ''')
  st.markdown('''
  ### Informe suas variáveis:
  ###### Essa aba receberá as variáveis de seus circuitos. Atente-se aos dados! 
  ''')
  
  variaveis, ajuda = st.columns([14,6]) #Cria duas colunas, uma que receberá as variáveis do circuito e outra com botões de ajuda 
  
  #Coluna das variáveis__________________________________________________________________________________________________________
  with variaveis:
    metodo = st.selectbox("Método de Instalação:", ["A1","A2", "B1","B2", "C", "D"]) #Cria uma caixa de seleção com os tipos de métodos de instalação dos circuitos (6 possíveis escolhas)
    tipo_instalacao = st.selectbox("Tipo de Instalação:", ["Iluminação","Tomadas de Uso Específico", "Tomadas de Uso Geral"]) #Cria uma caixa de seleção com os tipos de instalação dos circuitos (3 possíveis escolhas)
    tensao = st.selectbox("Tensão:", [127, 220, 380]) #Cria uma caixa de seleção com as tensões possíveis para os circuitos (3 possíveis escolhas)
    potencia = st.number_input("Potência Total do Circuito:", min_value=60, max_value=8500, value=2000) #Cria uma entrada para números inteiros que variam de 60 a 8500, sendo o valor padrão: 2000 (valores de potência total)
    num_circuitos = st.number_input("Circuitos no mesmo eletroduto:", min_value=1, max_value=30, value=5) #Cria uma entrada para números inteiros que variam de 1 a 30, sendo o padrão: 5 (números de circuitos em um mesmo eletroduto) 
    isolamento = st.selectbox("Tipo de Isolamento:", ["PVC","XLPE","EPR"]) #Cria uma caixa de selação com os tipos de isolamentos possíveis: PVC, XLPE e EPR (3 possíveis escolhas)
    local = st.selectbox("Local de Instalação:", ["Parede","Chão","Teto"]) #Cria uma caixa de seleção com o local de instalação possível: Parede, chão ou teto (3 possíveis escolhas)
    temperatura_ambiente = st.slider("Temperatura:", min_value=0, max_value=50, value=25) #Cria uma barra de correr com os valores para a temperatura, que varia de 0 a 50, com valor padrão de 25
    
  #Coluna dos botões de ajuda______________________________________________________________________________________________________
  with ajuda:              #A coluna ajuda está organizada com as descrições das variáveis necessárias para o dimensionamento.
    st.markdown(''' 
    ###### Sobre o Método:
    ''')
    if st.button("?", type="primary", key="Método de referência"): #Cria um botão de ajuda 
      st.write("O Método de referência é o modo de instalação do seu circuito.")
      st.image("https://raw.githubusercontent.com/emelyn23017/autodimensionamentoeletrico/main/Imagens/M%C3%A9todos%20de%20refer%C3%AAncia%20ABNT%20NBR5410.jpg")
      st.markdown("Caso ainda haja dúvidas, consulte o material-guia: [NBR5410](https://docente.ifrn.edu.br/jeangaldino/disciplinas/2015.1/instalacoes-eletricas/nbr-5410?page=30) (Informações sobre os tipos de métodos se encontram a partir da página 98)")

    st.markdown(''' 
    ###### Sobre o Tipo de Instalação:
    ''')
    if st.button("?", type="primary", key="Instalação"):
      st.write(" Tipo de Instalação é referente em ultima instância ao uso do circuito, sendo para instalação de lampadas (Iluminação) ou para instalação de tomadas de uso Geral ou Específico (Aparelhos que utilizam mais de 10 A).")
      
    
    st.markdown(''' 
    ###### Sobre a Tensão:
    ''')
    if st.button("?", type="primary", key="Tensão"):
      st.write("A Tensão (Diferença de Potencial - DDP) é referente a tensão de linha do seu circuito, consulte o seu provedor de energia caso desconheça.")
      
    st.markdown(''' 
    ###### Sobre a Potência:
    ''')
    if st.button("?", type="primary", key="Potência"):
      st.write("Potência é referente a soma da potência máxima individual de todos os pontos de energização do circuito, por exemplo: tomadas de uso geral, tomadas de uso especifico; etc.")
    st.markdown(''' 
    ###### Sobre o nº de circuitos:
    ''')
    if st.button("?", type="primary", key="Circuitos"):
      st.write("Número de circuitos ou condutores dentro do mesmo eletroduto.")
  
    st.markdown(''' 
    ###### Sobre o Isolamento:
    ''')
    if st.button("?", type="primary", key="Isolamento"):
      st.write("Informe o tipo de material utilzado no isolamento dos condutores.")
      
    st.markdown(''' 
    ###### Sobre o Local:
    ''')
    if st.button("?", type="primary", key="Local"):
      st.write("Informe o local por onde passam os eletrodutos que contêm seu circuito. Informe se estão contidos na parede, no teto ou no chão.")
      
    st.markdown(''' 
    ###### Sobre a Temperatura:
    ''')
    if st.button("?", type="primary", key="Temperatura"):
      st.write("Temperatura média do local da instalação, ou mesmo da sua região/cidade.")
      
    
  
#______________________________________________________________________________________________________________________________________________________________________________


# Criando a Aba de Saída de Dados______________________________________________________________________________________________________________________________________________
with saida:   #A aba de Resultados apresenta os resultados a partir das funções importadas do arquivo 'funcoes.py' e das variáveis adicionadas pelo usuário na aba 'Dados'
  st.markdown("""
  # Resultado do Redimensionamento:

  Aqui estão o disjuntor mais adequado e a seção transversal ideal do fio para seu sistema!
  A segurança vem sempre em primeiro lugar, portanto lembre-se de consultar um profissional. 

  """) 
   # Abaixo estamos definindo algumas outras variaveis usando as funções importadas do "funcoes.py" e da aba "entrada".
  disjuntores = tabela_disjuntores
  condicao = condicao_de_instalacao(isolamento,local)
  disjuntor = disjuntor_inicial(potencia, tensao, disjuntores)
  ftemperatura = fator_temperatura(condicao, temperatura_ambiente)
  agrupamento = fator_agrupamento(num_circuitos, metodo, agrupamentos = tabela_agrupamento)
  correcao = fator_correcao(agrupamento, ftemperatura)
  bitola_mn = bitola_min(tipo_instalacao)
  secao = bitola(disjuntor, bitola_mn, metodo, correcao, isolamento)

  # Abaixo é a caixa de texto que irá conter os valores de retorno e finais do nosso codigo, capacidade do disjuntor e seção do fio. 
  st.markdown(f'''
  #### O disjuntor ideal para esse circuito deve ser de {int(disjuntor)} A.
  
  #### A seção transversal do seu fio deve ser igual ou superior a: {secao[1]} mm², nas condições selecionadas esse condutor suporta uma corrente aproximadamente : {int(secao[0])} A sem aquecer.

  ''') 
  # O resultado ainda é apenas um teste 
