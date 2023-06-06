#Importando Bibliotecas
import streamlit as st
from json import loads


#Criando o titulo 
st.markdown('''
# **FOFOS DA BITOLA** 
#### APP para redimensionamento
''')
arquivo = st.file_uploader("arquivo aqui")
if arquivo:
  match arquivo.type.split('/'):
    case 'application','image':
      st.image(arquivo)	
			
		

# Criando uma Barra Lateral 
st.sidebar.title("MENU")

st.selectbox("Qual o Metodo Utilizado",["Metodo A","Método B","Método C","Metodo D"])
st.button("B")
