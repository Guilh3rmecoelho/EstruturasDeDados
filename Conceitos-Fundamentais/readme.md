📌 Conceitos de Variáveis e Tipos de Dados

🔵 Variáveis

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

🔵 Tipos de Dados

Como foi citado na introdução os tipos de dados definem o tipo de valor que pode ser armazenado em uma variável. Alguns exemplos comuns incluem:


📌 Inteiros (int): Números inteiros, como 10, -5, 42.

📌 Flutuantes (float): Números decimais, como 3.14, -0.01, 2.718.

📌 Strings (str): Sequências de caracteres, como "hello", "ChatGPT".

📌 Booleanos (bool): Valores lógicos, podendo ser True ou False.


🔵 Relação com Alocação de Memória

O tipo de dado de uma variável determina o espaço que ela ocupa na memória. Por exemplo:

🖥️ Inteiro (int): Pode ocupar 4 bytes na memória.

🖥️ Flutuante (float): Pode ocupar 8 bytes.

🖥️ String (str): Pode ocupar um número variável de bytes, dependendo do tamanho do texto armazenado.

🛠️ Diferença entre Alocação Estática e Dinâmica

Tipo de Alocação | Definição | Exemplo
------|--------|--------------|
Estática!|A memória é alocada no momento da compilação e tem tamanho fixo.|Arrays de tamanho fixo em C.
Dinâmica|A memória é alocada durante a execução do programa, permitindo flexibilidade.|Uso de listas em Python. 


🔵 Estática

A alocação estática ocorre com variáveis globais (alocadas fora de funções) ou quando variáveis locais (internas a uma função) são alocadas usando o modificador ''static''. Uma variável alocada estaticamente mantém seu valor durante toda a vida do programa, exceto quando explicitamente modificada.
``` C
#include <stdio.h>

int a = 0 ;  // variável global, aloc. estática

void incrementa(void)
{
          int b = 0 ; // variável local, aloc. automática
   static int c = 0 ; // variável local, aloc. estática
   
   printf ("a: %d, b: %d, c: %d\n", a, b, c) ;
   a++ ;
   b++ ;
   c++ ;
}

int main(void)
{
   int i ;
  
   for (i = 0; i < 5; i++)
      incrementa() ;

   return 0 ;
}

A execução desse código gera a seguinte saída:

  a: 0, b: 0, c: 0
  a: 1, b: 0, c: 1
  a: 2, b: 0, c: 2
  a: 3, b: 0, c: 3
  a: 4, b: 0, c: 4
```
🟢 Dinâmica

Na alocação dinâmica, o programa solicita explicitamente áreas de memória ao sistema operacional, as utiliza e depois as libera quando não forem mais necessárias, ou quando o programa encerrar. As requisições de memória dinâmica são geralmente alocadas na área de memória denominada heap.

``` C
#include <stdlib.h>
void * malloc (size_t size)
struct mystruct *ptr;
...
ptr = malloc( sizeof(struct mystruct) );
if (ptr == 0) abort();       // caso a alocação não tenha ocorrido

Liberação

A chamada ''free'' deve ser invocada para liberar uma área de memória previamente alocada dinamicamente:

#include <stdlib.h>
void free (void *ptr)

Esta função libera um bloco de memória previamente alocado, apontado por ''ptr''. Atenção: o ponteiro ''ptr'' continua apontando para o bloco liberado e por isso é aconselhável mudar seu valor para ''NULL'' após a liberação:

ptr = malloc (1024) ;
...
free (ptr) ;
ptr = NULL ;                 // não é obrigatório, mas aconselhável

```
Link | Tipo | Autor 
------|--------|--------------|
https://www.inf.ufpr.br/hexsel/ci067/10_aloc.html|Artigo|ufpr-Universidade Federal do Paraná
