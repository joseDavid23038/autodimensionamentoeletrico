#Importando Bibliotecas____________________________________________________________________________________________________________________________________________________________
import streamlit as st
from json import loads

#__________________________________________________________________________________________________________________________________________________________________________________

# Criando uma Barra Lateral ________________________________________________________________________________________________________________________________________________________
bar = st.sidebar

bar.title("MENU")

pagina_inicial = bar.button("Página Inicial")
pagina_redi = bar.button("Redimensionamento")
pagina_sobre = bar.button("Sobre o Projeto")

#____________________________________________________________________________________________________________________________________________________________________________


# Criando alternador de Paginas_____________________________________________________________________________________________________________________________________________________
inicial = st.container()
redi = st.container()

#_______________________________________________________________________________________________________________________________________________________________________________


# Criando a Pagina Inicial____________________________________________________________________________________________________________________________________________________________

if pagina_inicial:
  inicial.empty()
  with inicial:
    st.markdown('''

    # Bem vindo
    ### Redimensionamento de Circuito Elétricos

    Essa aba é direcionada a armazenar as informações do seu circuito elétrico, na qual estas, serão usadas para encontrar o disjuntor e bitola ideal para o seu sistema.
    Lembresse, aarmação e montagem de todo aparato elétrico deve ser realizada por um profissional, nosso trabalho é encontrar uma escala de produto que satisfaça suas necessidades.
    Conduto, o material e contas disponibilizados ainda assim devem ser revisados por um profisional cetificado.  

    ''')
if pagina_redi:
  redi.empty()
  with redi:
    st.button("Teste")

dica = False

botao_dica = st.button('?', type="primary")
if botao_dica:
  dica = not dica 
 
if dica:
  st.write('Botãoes de interrogação "?", são usados para quando houver dúvidas')
  
    
#_____________________________________________________________________________________________________________________________________________________________________________


