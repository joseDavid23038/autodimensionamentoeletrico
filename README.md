#### Autodimensionamento elétrico

#### Introdução: 
O trabalho técnico referente ao dimensionamento elétrico costuma ocorrer por análise manual de dados. Essa análise geralmente é realizada com base no número de circuitos, métodos de instalação e outras condições identificadas na planta elétrica do local. Por isso, quando não realizada por profissionais a instalação está passível à riscos, que comprometem a segurança do local e da própria instalação. Com o objetivo de evitar possíveis acidentes ocasionados por desinstrução ou falha humana e facilitar o cálculo de dimensionamento elétrico, pretendemos criar um código em python, que utilize a bilioteca Pandas, para analizar as variáveis necessárias para o dimesionamento, compara-las com a Norma Regulamentadora vigente (NBR5410) e retornar as especificações do disjuntor e da seção transversal do fio a serem utilizados.

Nosso programa em si, é dividido em duas principais partes: 
  - Interface: Será a face do nosso programa e a responsável por coletar os dados do esquema elétrico do usuário. Utilizaremos o software Kivy para criá-la. Pretendemos fazer uma interface acessível e intuitiva. 
  - Análise de dados: Usando as variáveis disponibilizadas pelo usuário, relacionará estas com a NBR5410. Esta comparação, nos indicará qual será o disjuntor e a seção transversal do condutor mais indicados para o tipo de instalação especificado. 

INTERFACE (Front-end):

ANÁLISE (Back-end):
