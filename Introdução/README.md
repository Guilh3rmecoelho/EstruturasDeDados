# 📌 Estruturas de Dados em Python  

📚 **Repositório para estudos acadêmicos sobre Listas Encadeadas, Listas Ordenadas e Árvores Binárias em Python.**  

## 🚀 Sobre o Repositório  
Este repositório foi criado para ajudar estudantes e desenvolvedores a **compreender e dominar estruturas de dados em Python**. Aqui, você encontrará conteúdos explicativos, exemplos práticos e implementações das principais estruturas de dados utilizadas na ciência da computação.  


---
## O que é estrutura de dados ?
As **estruturas de dados** são uma forma de organizar e armazenar dados para que eles possam ser acessados e trabalhados com eficiência. Eles definem a relação entre os dados e as operações que podem ser realizadas nos dados. Existem vários tipos de estruturas de dados definidas que facilitam aos cientistas de dados e engenheiros da computação se concentrarem no quadro principal da solução de problemas maiores, em vez de se perderem nos detalhes da descrição e do acesso aos dados. Além disso as estruturas de dados são os blocos de construção fundamentais da programação de computadores. Eles definem como os dados são organizados, armazenados e manipulados dentro de um programa. Compreender as estruturas de dados é muito importante para o desenvolvimento de algoritmos eficientes e eficazes. 
<!-- Explicando o que é estrutura de dados 1. Introdução às Estruturas de Dados- 1 -->
---

## 📌 Tipos de Dados em Python  

### 🔵 **1. Estruturas de Dados Primitivas**  
As estruturas primitivas são os tipos básicos fornecidos pela linguagem.  

✔️ **Inteiros (`int`)**  
✔️ **Flutuação (`float`)**  
✔️ **String (`str`)**  
✔️ **Booleano (`bool`)**  


🟢 **Exemplo de implementação:**  

✔️ **Inteiros (`int`)**  
Você pode usar um número inteiro para representar dados numéricos e, mais especificamente, números inteiros de infinito negativo a infinito, como 4, 5 ou -1.
```python
# Tipos de dados primitivos em Python

# Interios (int)
idade = 24
ano = 2025

print(idade, ano)  # Saída: 24 2025
`````
✔️ **Flutuação (`float`)**  
Float" significa "número de ponto flutuante". Você pode usá-lo para números racionais, geralmente terminando com um número decimal, como 1,11 ou 3,14.
```python
# Flutuação (float)
pi = 3.14159
altura = 1.75
print(pi, altura)  # Saída: 3.14159 1.75
```
✔️ **String (`str`)**  
String é uma sequência de caracteres, normalmente usado para representar texto. É considerado um tipo de dados que permite a manipulação e processamento de dados textuais em programas de computador.
```python
# String (str)
nome = "Python"
saudacao = "Olá, mundo!"
print(nome, saudacao)  # Saída: Python Olá, mundo!
```
✔️ **Booleano (`bool`)**  
Esse tipo de dados incorporado pode assumir os valores: True e False, o que geralmente os torna intercambiáveis com os inteiros 1 e 0. Os booleanos são úteis em expressões condicionais e de comparação.
``` python
# Booleano (bool)
maior_de_idade = True
menor_de_idade = False
print(maior_de_idade, menor_de_idade)  # Saída: True False
```
---


### 🔵 **2. Estruturas de Dados não Primitivas**  

✔️ **Matrizes (`array`)**  
✔️ **Listas (`list`)**  
✔️ **Tuplas (`tuple`)**  
✔️ **Dicionários (`dict`)**  
✔️ **Conjuntos (`set`)**  
✔️ **Arquivos (`file`)**  


🟢 **Exemplo de implementação:**  

✔️ **Matrizes(`array`)**
Matrix é um conjunto bidimensional de elementos, organizados em linhas e colunas. É representado como uma grade retangular, com cada elemento na intersecção de uma linha e coluna.
 ```
# Matrizes (Arrays) em Python - utilizando listas aninhadas
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[1][2])  # Saída: 6

          Coluna 0  Coluna 1  Coluna 2  
Linha 0   [1           2         3]  
Linha 1   [4           5         6]  ⬅️ matriz[1][2]  
Linha 2   [7           8         9]
```

✔️ **Listas(`list`)**
As listas em Python são usadas para armazenar coleções de itens heterogêneos. Eles são mutáveis, o que significa que você pode alterar o conteúdo deles sem alterar a identidade. Você pode reconhecer as listas por seus colchetes [ e ] que contêm elementos separados por vírgula ,. As listas são incorporadas ao Python: você não precisa invocá-las separadamente.

``` python
# Lista em Python
frutas = ["maçã", "banana", "uva", "laranja"]
frutas.append("abacaxi")  # Adicionando um novo elemento
print(frutas)  
# Saída: ['maçã', 'banana', 'uva', 'laranja', 'abacaxi']
```
✔️ **Tuplas(`tuple`)**
As tuplas são outro tipo de dados de sequência padrão. A diferença entre tuplas e lista é que as tuplas são imutáveis, o que significa que, uma vez definidas, você não pode excluir, adicionar ou editar nenhum valor dentro delas. Isso pode ser útil em situações em que você pode passar o controle para outra pessoa, mas não quer que ela manipule os dados na sua coleção, mas talvez apenas os veja ou realize operações separadamente em uma cópia dos dados.
``` python
# Tupla em Python (imutável)
coordenadas = (10.5, 20.3)
print(coordenadas[0])  # Saída: 10.5
```
✔️ **Dicionário(`dict`)**
Um dicionário Python é uma forma de coleção de dados em que se guarda uma chave e um valor correspondente. É similar a um dicionário mesmo, em que há sempre um termo e uma tradução. Assim, você encontra um valor pelo elemento correspondente — diferentemente de encontrar por um índice como em uma lista. O dicionário é uma forma de organização similar a um de banco de dados, mais completa e abrangente para diversas situações. 

``` python
# Dicionário em Python (chave-valor)
aluno = {
    "nome": "Carlos",
    "idade": 21,
    "curso": "Engenharia"
}
print(aluno["nome"])  # Saída: Carlos
```
✔️ **Conjuntos (`set`)**
Os conjuntos são uma coleção de objetos distintos (exclusivos). Eles são úteis para criar listas que contêm apenas valores exclusivos no conjunto de dados. É uma coleção não ordenada, mas mutável, o que é muito útil quando você está analisando um conjunto de dados enorme.

``` python
# Conjuto (set)
conjunto_numeros = {1, 2, 3, 4, 5, 5, 6}

print(conjunto_numeros)  
# Saída: {1, 2, 3, 4, 5, 6}  (valores duplicados são removidos automaticamente)

# Adicionando um novo elemento
conjunto_numeros.add(7)
print(conjunto_numeros)  
# Saída: {1, 2, 3, 4, 5, 6, 7}

# União de conjuntos
outro_conjunto = {5, 6, 7, 8, 9}
uniao = conjunto_numeros.union(outro_conjunto)
print(uniao)  
# Saída: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Interseção de conjuntos
intersecao = conjunto_numeros.intersection(outro_conjunto)
print(intersecao)  
# Saída: {5, 6, 7}
```
✔️ **Arquivos (`files`)**
Os arquivos são tradicionalmente uma parte das estruturas de dados. E, embora o big data seja comum no setor de ciência de dados, uma linguagem de programação sem a capacidade de armazenar e recuperar informações armazenadas anteriormente dificilmente seria útil. Você ainda precisa usar todos os dados armazenados em arquivos nos bancos de dados e aprenderá como fazer isso.
``` python
### 🔹 #Arquivo 
# Criando e escrevendo em um arquivo de texto
with open("dados.txt", "w") as arquivo:
    arquivo.write("Este é um exemplo de arquivo em Python.\n")
    arquivo.write("Podemos armazenar textos e ler depois!")

print("Arquivo criado e dados escritos com sucesso!")
```
---


Agora que você já aprendeu um pouco sobre estruturas de dados, vamos explorar alguns exemplos práticos que fazem parte do seu dia a dia, muitas vezes, sem que você perceba!

#### 🛒 **1. E-commerce e Recomendação de Produtos**
Amazon🛒🛍
- Utilização de **listas e árvores** para armazenar e filtrar produtos.  
- Uso de **filas e pilhas** para gerenciar carrinhos de compra e histórico de navegação.

#### 💰 **2. Sistemas Bancários e Transações Financeiras**  
Banco do Brasil🪙
- Uso de **filas** para processar transações em tempo real.  
- Aplicação de **hashmaps (dicionários)** para armazenar informações seguras de clientes.

#### 🚗 **3. Aplicativos de Navegação **
  Google Maps, Waze 🛣️  
- Uso de **grafos** para encontrar o caminho mais curto entre dois pontos.  
- Aplicação de **estruturas hierárquicas** para armazenar mapas e rotas.
---


  ### Referencias
 Link | Tipo | Descrição | Autor 
------|--------|--------------| ------------|
https://www.datacamp.com/pt/tutorial/data-structures-python|Artigo|Tutorial de estruturas de dados Python|Sejal Jaiswal
https://www.geeksforgeeks.org/data-structures/|Blog|Tutorial de estruturas de dados| -
https://www.hashtagtreinamentos.com/dicionarios-em-python|Blog|Dicionários em Python: Descubra o que são e como usá-los!|-

