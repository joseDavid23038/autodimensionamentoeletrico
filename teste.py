#Importando Bibliotecas____________________________________________________________________________________________________________________________________________________________
import streamlit as st
#https://mrbravin-autodimensionamentoeletrico-teste-kcs6ty.streamlit.app__________________________________________________________________________________________________________________________________________________________________________________


# Criando uma Barra Lateral ________________________________________________________________________________________________________________________________________________________
bar = st.sidebar
#_______________________________________________________________________________________________________________________________________________________________________________

st.title("Redimencionamento De Circuitos")

with st.expander("About Us"):
  st.markdown("""
  # Sobre o Projeto:

  ### Esse projeto foi criado para ajudar no dicimencionamento de circuitos elétricos. 

  Criadores e Idealizadores:  
  -Daniel Bravin  
  -Gustavo Matos  
  -Emelyn 
  -José David  
  
  """)
st.divider()

# Criando Duas telas, Entrada, Saida____________________________________________________________________________________________________________________________________________________________
entrada, saida = st.tabs(["Entrada","Saída"])

with entrada:
  st.markdown('''
  ### Informe suas Variáveis:
  ###### Aba direcionada a receber as variaveis de seus circúitos.
  ''')
  variaveis, ajuda = st.columns([3,1])
  with variaveis:
    metodo_usado = st.selectbox("Método", ["-", "A1","A2", "B1","B2", "C", "D"])
    tensao = st.selectbox("Tensão", ["",127, 220,380])
    potencia = st.slider("Potência Total do Circuito", min_value=100, max_value=26000)
    num_circuitos = st.slider("Circuitos no mesmo eletrodulto", min_value=1, max_value=30)
    temperatura = st.slider("Temperatura", min_value=0, max_value=50)
  

  with ajuda:
    botao_metodo = st.button("?", type="primary")
    metodo = False
    if botao_metodo == True:
      if metodo == False
        metodo = True
      else:
        metodo = False
    
    if metodo:
      st.image("https://github.com/MrBravin/autodimensionamentoeletrico/blob/main/Interface.jpg?raw=true")
    else:
      st.write("Puts")
   
  
#______________________________________________________________________________________________________________________________________________________________________________


# Criando a Aba de Saída de Dados______________________________________________________________________________________________________________________________________________
with saida:
  st.title("Resultado do Dimensionamento")
  corrente = int(potencia/tensao)
  st.markdown(f'''
    
      
        
  ###### A corrente do seu sistema é: {corrente}
  
  ''')
  


# Criando Pagina "Sobre"_________________________________________________________________________________________________________________________________________________________


  
    
    
#________________________________________________________________________________________________________________________________________________________________________________

