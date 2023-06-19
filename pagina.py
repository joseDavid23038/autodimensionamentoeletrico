#Importando Bibliotecas____________________________________________________________________________________________________________________________________________________________
import streamlit as st
#import funcoes
from funcoes import *

# Configurando a Página_______________________________________________________________________________________________________________________________________________________
st.set_page_config(page_title="Redimensionamento", layout="wide", page_icon="U&#x26A1;",initial_sidebar_state="collapsed")

#______________________________________________________________________________________________________________________________________________________________________________


# Criando uma Barra Lateral ________________________________________________________________________________________________________________________________________________________
bar = st.sidebar
bar.title("Contato:")
bar.write('''
Envie suas dúvidas ou sugestões para nós por e-mail!
Houve algum erro durante a utilização? Nos informe.
e-mails para contato: 
danielbravin@hotmail.com
emelyn.a.ilum@gmail.com
programming.gustamatos@gmail.com 
[GitHub da Página](https://github.com/MrBravin/autodimensionamentoeletrico/edit/main/teste.py)
''') #Adicionar e-mail do José David!!!

#_______________________________________________________________________________________________________________________________________________________________________________

st.title("Autodimensionamento elétrico - redimensionamento de circuitos residenciais")   # Essa função define um título, basicamente, uma string com uma edição específica.

st.divider()                   #A função "divider" é usada para criar um corte cinza na tela, meramente para melhor organização dos itens. 

with st.expander("About Us"):  #Aqui a função expander, cria um item que ao ser clicado se expande mostrando quaisquer itens que se deseja, seja um texto ou um botão.  
  st.markdown("""
  # Sobre o Projeto:

  ### Esse projeto foi criado a fim de auxiliar o dimensionamento de circuitos elétricos residenciais no Brasil. 
  Com o objetivo de evitar possíveis acidentes ocasionados por desinstrução ou falha humana e facilitar o cálculo de dimensionamento elétrico, 
  criamos este site para que você possa fazer o autodimensionamento elétrico da sua casa! Nós analizamos as variáveis necessárias para o dimesionamento,
  as comparamos com a NBR5410 e, como resultado, indicamos para você o disjuntor e da seção transversal do fio a serem utilizados na sua casa! 
  Autodimensione e fique seguro! 
  
  Criadores e idealizadores:  
  - Daniel Bravin  
  - Gustavo Matos  
  - Emelyn Alves
  - José David  
  
  """) #Expandir a motivação da criação do projeto (porque criamos o projeto), utilizar uma linguagem um pouco menos formal a fim de criar uma maior proximidade com o usuário. 
st.divider()  


entrada, saida = st.tabs(["Dados","Resultado"])  # Criando Duas telas, Entrada, Saída *mudança para Dados e Resultado, respectivamente. 

# Criando a aba Entrada________________________________________________________________________________________________________________________________________________________
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
  variaveis, ajuda = st.columns([14,6])
  with variaveis:
    metodo = st.selectbox("Método de Instalação:", ["A1","A2", "B1","B2", "C", "D"])
    tensao = st.selectbox("Tensão:", [127, 220, 380])
    potencia = st.number_input("Potência Total do Circuito:", min_value=60, max_value=8500, value=2000)
    num_circuitos = st.number_input("Circuitos no mesmo eletroduto:", min_value=1, max_value=30, value=5)
    isolamento = st.selectbox("Tipo de Isolamento:", ["PVC","XLPE","EPR"])
    local = st.selectbox("Local de Instalação:", ["Parede","Chão","Teto"])  
    temperatura = st.slider("Temperatura:", min_value=0, max_value=50, value=25)
    
  with ajuda:
    st.markdown(''' 
    ###### Sobre o Método:
    ''')
    if st.button("?", type="primary", key="Método de referência"):
      st.write("O Método de referência é o modo de instalação do seu circuito.")
      st.image("https://raw.githubusercontent.com/emelyn23017/autodimensionamentoeletrico/main/Imagens/M%C3%A9todos%20de%20refer%C3%AAncia%20ABNT%20NBR5410.jpg")
      st.markdown("Caso ainda haja dúvidas, consulte o material-guia: [NBR5410](https://docente.ifrn.edu.br/jeangaldino/disciplinas/2015.1/instalacoes-eletricas/nbr-5410?page=30) (Informações sobre os tipos de metodo se encontram apartir da página 98)")
      
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
with saida:
  st.markdown("""
  # Resultado do Redimensionamento:

  Aqui estão o disjuntor mais adequado e a seção transversal ideal do fio para seu sistema!
  A segurança vem sempre em primeiro lugar, portanto lembre-se de consultar um profissional. 

  """)
  disjuntor_inicial = disjuntor_inicial(potencia,tensao)
  corrente = int(potencia/tensao)
  st.markdown(f'''
  #### A corrente mínima que o disjuntor precisa aguentar: {disjuntor_inicial}
  
  ''') # O resultado ainda é apenas um teste 


