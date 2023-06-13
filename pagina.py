#Importando Bibliotecas____________________________________________________________________________________________________________________________________________________________
import streamlit as st
#import funcoes
from funcoes import *

tabela_disjuntores = pd.read_excel("Dados\DISJUNTORES.xlsx")
tabela_agrupamento = pd.read_excel("Dados\AGRUPAMENTO.xlsx")
tabela_temperatura = pd.read_excel("Dados\TEMPERATURA.xlsx")


# Configurando a Página_______________________________________________________________________________________________________________________________________________________
st.set_page_config(page_title="Redimencionamento", layout="wide", page_icon="U&#x26A1;",initial_sidebar_state="collapsed")

#______________________________________________________________________________________________________________________________________________________________________________


# Criando uma Barra Lateral ________________________________________________________________________________________________________________________________________________________
bar = st.sidebar
bar.title("Contato:")
bar.write("Envie erros, duvidas ou sugestões no email caso haja alguma pendência")
bar.write("email: danielbravin@hotmail.com")
bar.write("[GitHub da Página](https://github.com/MrBravin/autodimensionamentoeletrico/edit/main/teste.py)")

#_______________________________________________________________________________________________________________________________________________________________________________

st.title("Redimencionamento De Circuitos")   # Essa função define um titulo, basicamente, uma string com uma edição específica.

st.divider()                   #A função "diviser" é usada para criar um corte cinza na tela, meramente para melhor oragnização dos itens. 

with st.expander("About Us"):  #Aqui a função expander, cria um item que ao ser clicado se expande mostrando quaisquer itens que se deja, seja um texto ou um botão.  
  st.markdown("""
  # Sobre o Projeto:

  ### Esse projeto foi criado para ajudar no dimencionamento de circuitos elétricos. 

  Criadores e Idealizadores:  
  -Daniel Bravin  
  -Gustavo Matos  
  -Emelyn Alves
  -José David  
  
  """)
st.divider()  


entrada, saida = st.tabs(["Entrada","Saída"])  # Criando Duas telas, Entrada, Saida

# Criando a aba Entrada________________________________________________________________________________________________________________________________________________________
with entrada:
  st.markdown('''

    # Bem vindo

    Essa aba é direcionada a armazenar as informações do seu circuito elétrico, na qual estas, serão usadas para encontrar o disjuntor e bitola ideal para o seu sistema.
    Lembresse, aarmação e montagem de todo aparato elétrico deve ser realizada por um profissional, nosso trabalho é encontrar uma escala de produto que satisfaça suas necessidades.
    Conduto, o material e contas disponibilizados ainda assim devem ser revisados por um profisional cetificado.  

    ''')
  st.markdown('''
  ### Informe suas Variáveis:
  ###### Aba direcionada a receber as variaveis de seus circúitos.
  ''')
  variaveis, ajuda = st.columns([14,6])
  with variaveis:
    metodo = st.selectbox("Método de Instalação:", ["A1","A2", "B1","B2", "C", "D"])
    tensao = st.selectbox("Tensão:", [127, 220,380])
    potencia = st.number_input("Potência Total do Circuito:", min_value=60, max_value=8500, value=2000)
    num_circuitos = st.number_input("Circuitos no mesmo eletrodulto:", min_value=1, max_value=30, value=5)
    isolamento = st.selectbox("Tipo de Isolamento:", ["PVC","XLPE","EPR"])
    local = st.selectbox("Local de Instalação:", ["Parede","Chão","Teto"])  
    temperatura = st.slider("Temperatura:", min_value=0, max_value=50, value=25)
    
  with ajuda:
    st.markdown(''' 
    ###### Sobre o Método:
    ''')
    if st.button("?", type="primary", key="Método"):
      st.write("O Método de Referencia se refere ao modo de instalação de todo o circuito.")
      st.image("https://raw.githubusercontent.com/emelyn23017/autodimensionamentoeletrico/main/Imagens/M%C3%A9todos%20de%20refer%C3%AAncia%20ABNT%20NBR5410.jpg")
      st.markdown("Caso ainda haja duvidas, consulte o material guia: [NBR5410](https://docente.ifrn.edu.br/jeangaldino/disciplinas/2015.1/instalacoes-eletricas/nbr-5410?page=30) (Informações sobre os tipos de metodo se encontram apartir da página 98)")
      
    st.markdown(''' 
    ###### Sobre a Tensão:
    ''')
    if st.button("?", type="primary", key="Tensão"):
      st.write("A Tensão(DDP) é referente a tensão de linha do seu circuito, consulte o seu provedor de energia caso desconheça.")
      
    st.markdown(''' 
    ###### Sobre a Potência:
    ''')
    if st.button("?", type="primary", key="Potência"):
      st.write("Potência é referente a soma da potencia máxima individual de todos os pontos de energização do circuito, por exmplo: Tomadas de uso geral, tomadas de uso especifico...")
    st.markdown(''' 
    ###### Sobre o nº de Circuitos:
    ''')
    if st.button("?", type="primary", key="Circuitos"):
      st.write("Numero de circuitos ou condutores dentro do mesmo eletroduto.")
  
    st.markdown(''' 
    ###### Sobre o Isolamento:
    ''')
    if st.button("?", type="primary", key="Isolamento"):
      st.write("Informe o Tipo de material utilzado no isolamento dos condutores.")
      
    st.markdown(''' 
    ###### Sobre o Local:
    ''')
    if st.button("?", type="primary", key="Local"):
      st.write("Informe o local por onde os eletrodutos, que contém seu circuito, passam, se estão contido na parede, no teto ou no chão.")
      
    st.markdown(''' 
    ###### Sobre a Temperatura:
    ''')
    if st.button("?", type="primary", key="Temperatura"):
      st.write("Temperatura média do local da instalação, ou mesmo da sua região/cidade.")
      
    
  
#______________________________________________________________________________________________________________________________________________________________________________


# Criando a Aba de Saída de Dados______________________________________________________________________________________________________________________________________________
with saida:
  st.markdown("""
  # Resultado do Redimencionamento:
  
  Essa aba é direcionada à mostrar o resultado do redimensionameto do circuito dado, aqui ficaram expostas as conclusões do trabalho,
  mostrando o disjuntor mais adequado e a bitola do fio condutor ideal para o seu sistema.
  
  """)
  
  corrente = int(potencia/tensao)
  st.markdown(f'''
  #### A corrente do seu sistema é: {corrente}
  
  ''')


