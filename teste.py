#Importando Bibliotecas____________________________________________________________________________________________________________________________________________________________
import streamlit as st
#https://mrbravin-autodimensionamentoeletrico-teste-kcs6ty.streamlit.app__________________________________________________________________________________________________________________________________________________________________________________


# Criando uma Barra Lateral ________________________________________________________________________________________________________________________________________________________
bar = st.sidebar
bar.title("MENU") 

state_page = 1 

inicial = st.container()
redi = st.container()
sobre = st.container()

pagina_inicial = bar.button("Página Inicial", type="primary")
pagina_redi = bar.button("Redimensionamento", type="primary")
pagina_sobre = bar.button("Sobre o Projeto", type="primary")


if pagina_inicial:
  stage_page = 1
  
elif pagina_redi:
  stage_page = 2

elif pagina_sobre:
  stage_page = 3

else:
  stage_page = 1

#_______________________________________________________________________________________________________________________________________________________________________________


# Criando a Pagina Inicial____________________________________________________________________________________________________________________________________________________________
if stage_page == 1:
  inicial.empty()
  with inicial:
    st.markdown('''

    # Bem vindo
    ### Redimensionamento de Circuito Elétricos

    Essa aba é direcionada a armazenar as informações do seu circuito elétrico, na qual estas, serão usadas para encontrar o disjuntor e bitola ideal para o seu sistema.
    Lembresse, aarmação e montagem de todo aparato elétrico deve ser realizada por um profissional, nosso trabalho é encontrar uma escala de produto que satisfaça suas necessidades.
    Conduto, o material e contas disponibilizados ainda assim devem ser revisados por um profisional cetificado.  

    ''')
#______________________________________________________________________________________________________________________________________________________________________________


# Criando a Aba de Redimencionamento______________________________________________________________________________________________________________________________________________
metodo = ""

if stage_page == 2:
  redi.empty()
  with redi:
    st.title("Redimensionamento de Circuitos")
    st.write('<font size="6">Selecione as variáveis do seu circuito:</font>', unsafe_allow_html=True)
    with st.form(key='redimensionamento_form'):
      metodo_usado = st.selectbox("Método", ["-", "A1","A2", "B1","B2", "C", "D"])
      tensao = st.selectbox("Tensão", ["",127, 220,380])
      potencia = st.slider("Potência Total do Circuito", min_value=100, max_value=26000)
      num_circuitos = st.slider("Circuitos no mesmo eletrodulto", min_value=1, max_value=30)
      temperatura = st.slider("Temperatura", min_value=0, max_value=50)
      
      botao_enviar = st.form_submit_button("Enviar", type="primary")
    
    if botao_enviar:
      metodo = metodo_usado.value
      v = tensao.value
      p = potencia.value
      i = p/v
      st.write(i)
    
#_______________________________________________________________________________________________________________________________________________________________________________


# Criando Pagina "Sobre"_________________________________________________________________________________________________________________________________________________________
if stage_page == 3:
  sobre.empty()
  with sobre:
    st.markdown("""
    # Sobre o Projeto:
    
    ### Esse projeto foi criado para ajudar no dicimencionamento de circuitos elétricos. 
    
   Criadores e Idealizadores:  
    -Emelyn  
    -José David  
    -Daniel Bravin  
    -Gustavo Matos  
    
    """)
#________________________________________________________________________________________________________________________________________________________________________________

