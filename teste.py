#Importando Bibliotecas
import streamlit as st
from json import loads




st.markdown(
    """
    <style>
    body {
        background-color: #D3D3D3;
    }
    </style>
    """,
    unsafe_allow_html=True
)



#Criando a Pagina Inicial
st.markdown('''

# **!! Bem vindo !!**
### Redimensionamento de Circuito Elétricos

Essa aba é direcionada a armazenar as informações do seu circuito elétrico, na qual estas, serão usadas para encontrar o disjuntor e bitola ideal para o seu sistema.
Lembresse, aarmação e montagem de todo aparato elétrico deve ser realizada por um profissional, nosso trabalho é encontrar uma escala de produto que satisfaça suas necessidades.
Conduto, o material e contas disponibilizados ainda assim devem ser revisados por um profisional cetificado.  
''')	

button_width = 100
button_height = 50
margin = 10

# Obter a largura e altura da tela
st.session_state.screen_width = st.session_state.screen_width or st.experimental_get_query_params().get("screen_width", [0])[0]
st.session_state.screen_height = st.session_state.screen_height or st.experimental_get_query_params().get("screen_height", [0])[0]

# Adicionar um botão no canto inferior direito
button_position = (st.session_state.screen_width - button_width - margin, st.session_state.screen_height - button_height - margin)
if st.button('Clique aqui', key='my_button', position=button_position, width=button_width, height=button_height):
    st.write('Você clicou no botão!')






# Criando uma Barra Lateral 
st.sidebar.title("MENU")

st.sidebar.selectbox("Qual o Metodo Utilizado",["Metodo A","Método B","Método C","Metodo D"])
st.button("TESTE",type="primary")
 
