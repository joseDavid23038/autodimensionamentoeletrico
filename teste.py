#Importando Bibliotecas
import streamlit as st
from json import loads


#Criando a Pagina Inicial
st.markdown('''
# **Bem vindo**
### Redimensionamneto de Circuito Elétricos 
''')
arquivo = st.file_uploader("arquivo aqui")
if arquivo:
  st.image(arquivo)	
  
else:
  st.error("Arraste um arquivo")
		

# Criando uma Barra Lateral 
st.sidebar.title("MENU")

st.selectbox("Qual o Metodo Utilizado",["Metodo A","Método B","Método C","Metodo D"])
st.button("B")
