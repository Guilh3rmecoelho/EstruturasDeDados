📌 Conceitos de Variáveis e Tipos de Dados

🔹 Variáveis

Variáveis são espaços na memória que armazenam valores que podem ser manipulados pelo programa. Elas permitem que os dados sejam armazenados e acessados de maneira eficiente durante a execução do programa.
```pyhton
# Declarando variáveis
idade = 25  # Inteiro
altura = 1.75  # Flutuante
nome = "Carlos"  # String
estudante = True  # Booleano

# Exibindo os valores armazenados
print("Nome:", nome)
print("Idade:", idade, "anos")
print("Altura:", altura, "m")
print("É estudante?", estudante)
```

🔹 Tipos de Dados

Como foi citado na introdução os tipos de dados definem o tipo de valor que pode ser armazenado em uma variável. Alguns exemplos comuns incluem:

📌 Inteiros (int): Números inteiros, como 10, -5, 42.

📌 Flutuantes (float): Números decimais, como 3.14, -0.01, 2.718.

📌 Strings (str): Sequências de caracteres, como "hello", "ChatGPT".

📌 Booleanos (bool): Valores lógicos, podendo ser True ou False.

🔹 Relação com Alocação de Memória

O tipo de dado de uma variável determina o espaço que ela ocupa na memória. Por exemplo:

🖥️ Inteiro (int): Pode ocupar 4 bytes na memória.

🖥️ Flutuante (float): Pode ocupar 8 bytes.

🖥️ String (str): Pode ocupar um número variável de bytes, dependendo do tamanho do texto armazenado.

🛠️ Diferença entre Alocação Estática e Dinâmica

🚀 Tipo de Alocação

📖 Definição

🎯 Exemplo

🔵 Estática

A memória é alocada no momento da compilação e tem tamanho fixo.

Arrays de tamanho fixo em C.

🟢 Dinâmica

A memória é alocada durante a execução do programa, permitindo flexibilidade.

Uso de listas em Python ou malloc() em C.

📌 Resumo: A alocação de memória é um conceito fundamental na programação, influenciando diretamente o desempenho e a eficiência dos programas. Compreender a diferença entre alocação estática e dinâmica é essencial para otimizar o uso de recursos computacionais. 🚀
