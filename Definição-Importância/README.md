# 📌 Estruturas de Dados: Definição e Importância  

As **estruturas de dados** desempenham um papel crucial no desenvolvimento de software, impactando diretamente a **eficiência, escalabilidade e desempenho** de um programa.  

---

## 🔵 **Estruturas de Dados Lineares e Não Lineares**  

###  **O que são estruturas Lineares**  
Começaremos nosso estudo de estruturas de dados considerando quatro estruturas simples, mas muito uteis. Pilhas, filas, deques e listas são exemplos de coleções de dados cujos itens são ordenados de acordo com ordem que são inseridos ou removidos da estrutura. Uma vez que um item é inserido, fica em uma mesma posição em relação aos demais itens que foram inseridos antes ou que serão inseridos depois.Estruturas lineares podem ser consideradas como tendo duas extremidades,de frente e traseira por exemplo.O que distingue uma estrutura linear de outra é a maneira em que itens são inseridos e removidos, em particular a extremidade onde estes inserções e remoções ocorrem. Por exemplo, uma estrutura pode permitir que novos itens sejam inseridos em apenas uma das extremidades (pilhas e filas). Algumas estruturas podem permitir que itens sejam removidos de ambas as extremidades

## 🔵 **Principais Fatores que Afetam o Desempenho**

### 1️⃣ Complexidade de Tempo (Big-O Notation)

A eficiência de uma estrutura de dados é geralmente medida usando a notação Big-O, que descreve como o tempo de execução cresce com o tamanho dos dados.
Estrutura de Dados | Inserção |	Remoção | Busca
------|--------|--------------|------|
Lista Simples (Array)|O(1) no final, O(n) no início|O(n)|O(n)
Fila (Queue)|O(1)|O(1)|O(n)
Pilha (Stack)|O(1)|O(1)|O(n)
Lista Encadeada|O(1)| O(1) (se no início)|O(n)
Dicionário (Hash Table)|O(1)|O(1)|O(1)
Árvore de Busca Binária (BST)|O(log n)|O(log n)|O(log n)

 Uma estrutura como uma hash table é muito eficiente para buscas rápidas (O(1)), enquanto uma lista encadeada é útil quando precisamos de inserção e remoção frequentes sem realocação.

### 2️⃣ Consumo de Memória

Cada estrutura de dados consome memória de maneira diferente:

  Listas e Arrays armazenam elementos de forma contígua na memória, o que pode exigir realocações.
  Filas e Pilhas podem ser implementadas com arrays ou listas encadeadas, impactando o uso de memória.
  Dicionários (Hash Tables) usam mais espaço para armazenar índices (hashes), mas oferecem buscas rápidas.
  Árvores equilibradas (como AVL ou Red-Black) exigem mais memória devido aos ponteiros adicionais, mas garantem eficiência na busca.

 ### 3️⃣ Casos de Uso e Escolha Certa
  Link | Tipo | Descrição 
------|--------|--------------|
Precisa armazenar e acessar elementos rapidamente pelo índice?|Array/Listas
Precisa processar dados em ordem FIFO?|Fila (Queue)
Precisa processar dados em ordem LIFO?|Pilha (Stack)
Precisa de buscas rápidas e flexíveis?|Dicionário (Hash Table)
Precisa de busca ordenada e eficiente?|Árvore de Busca Binária (BST)

## 🟢 **Principais Estruturas Lineares**  

### ✔️ **Pilhas (Stacks)**  
 Uma pilha (stack) é uma coleção ordenada de itens onde a inserção de novos itens e a remoção de itens existentes sempre ocorrem na mesma extremidade. Este extremidade é comumente chamada de topo. A extremidade oposta ao topo é conhecida como base, seguem o princípio **LIFO** (*Last In, First Out*), onde o último elemento inserido é o primeiro a ser removido.  


```python
# Criando uma pilha (usando lista)
pilha = []

# Adicionando elementos na pilha
pilha.append(10)   # Adiciona no topo
pilha.append(20)
pilha.append(30)

# Removendo elementos da pilha (remover do topo)
topo = pilha.pop()  # Remove o último elemento
print("Elemento removido do topo:", topo)

# Acessando o topo da pilha
topo_pilha = pilha[-1]  # Acessa o último elemento sem remover
print("Elemento no topo:", topo_pilha)

# Exibindo a pilha final
print("Pilha final:", pilha)
```

### ✔️ **Filas (Queues)**  
 Uma fila (queue) é uma coleção ordenada de itens em que a inserção de novos itens acontece em uma extremidade, chamado de “fim” (rear), e a remoção de itens existente ocorre no outro extremo, comumente chamado de “início” (front). Um elemento é inserido no fim da fila e faz o seu caminho em direção ao início, esperando até aquele momento em que é o próximo elemento seja removido. O item inserido mais recentemente na fila deve aguardar no final do coleção. O item que está na coleção há mais tempo está mais próximo do início. Este princípio de ordenação é às vezes chamado de FIFO, primeiro a entrar, primeiro a sair (first-in first-out). Também é conhecido como “primeiro a chegar, primeiro a ser servido” (first-come first-serverd).


``` python
from collections import deque

# Criando uma fila (usando deque)
fila = deque()

# Adicionando elementos na fila
fila.append(10)   # Adiciona no final da fila
fila.append(20)
fila.append(30)

# Removendo elementos da fila (remoção do início)
primeiro = fila.popleft()  # Remove o primeiro elemento da fila
print("Elemento removido da frente:", primeiro)

# Acessando o primeiro e o último elemento
frente = fila[0]   # Primeiro elemento
ultimo = fila[-1]   # Último elemento

print("Primeiro elemento na fila:", frente)
print("Último elemento na fila:", ultimo)

# Exibindo a fila final
print("Fila final:", fila)
```
### ✔️ **Deques (Double-ended Queues)**  
Uma deque, também é conhecida como fila de duas extremidades, é uma coleção ordenada de itens semelhantes à fila. Tem duas extremidades, uma é o início (front) e uma é o fim (rear), e os itens permanecem posicionados na coleção. O que faz um deque diferente é a natureza não-restritiva de adicionar e remover itens. Novos itens podem ser adicionados no início ou no fim. Da mesma forma, itens existentes podem ser removidos de qualquer uma das extremidades,embora a deque possa assumir muitas das características de pilhas e filas, não requer a oredanação LIFO nem a FIFO que são impostas para essas estruturas de dados.
 
``` python
from collections import deque

# Criando um deque
deque_exemplo = deque()

# Adicionando elementos
deque_exemplo.append(10)      # Adiciona no final
deque_exemplo.append(20)
deque_exemplo.appendleft(5)   # Adiciona no início

# Removendo elementos
deque_exemplo.pop()           # Remove do final
deque_exemplo.popleft()       # Remove do início

# Acessando o primeiro e último elemento
primeiro = deque_exemplo[0]  
ultimo = deque_exemplo[-1]  

# Exibindo o deque final
print("Deque final:", deque_exemplo)
``` 
Para saber mais sobre algoritmos de backtracking desça até as referencias https://www.engwhere.com.br/utilitarios-agenda-calendario-apontamentos-e-tarefas/

### ✔️ **Listas**  
Uma lista é uma coleção de itens em que cada item tem uma posição relativa em relação aos outros. Mais especificamente, nos referiremos este tipo de lista como uma lista desordenada. Podemos considerar que a lista possui um primeiro item, um segundo item, um terceiro item e assim por diante. Nós também podemos no referirmos ao início da lista (o primeiro item) ou ao final da lista (o último item). Por simplicidade, vamos supor que as listas não podem conter itens duplicados.

``` python
# Criando uma lista de números
numeros = [10, 20, 30, 40, 50]

# Adicionando elementos
numeros.append(60)  # Adiciona no final
numeros.insert(2, 25)  # Adiciona na posição 2

# Removendo elementos
numeros.remove(40)  # Remove o valor 40
ultimo = numeros.pop()  # Remove o último elemento

# Acessando elementos
primeiro = numeros[0]  # Primeiro elemento
ultimo = numeros[-1]  # Último elemento

# Percorrendo a lista
for num in numeros:
    print(num)

# Saída da lista após as operações
print("Lista final:", numeros)
```
---

📌 **Uso comum:** Implementação de listas de tarefas, sistemas de atendimento (ex: filas de banco).  

---

### ✔️ **Estruturas Não Lineares**  
Os elementos **não seguem uma sequência fixa** e podem ter múltiplas conexões.  

🔵 **Exemplos:**  

### ✔️ **Árvores (Trees)**
Uma árvore é uma estrutura de dados recursiva que permite representar dados dispostos de maneira hierárquica, é composta por um conjunto de nós, existe um nó raiz que contém zero ou mais sub-árvores, cujas raízes(nós internos) estão ligadas diretamente à raiz, Os nós que não têm filhos são chamados de folhas (nós externos).

<img src="https://www.alura.com.br/artigos/assets/estruturas-de-dados-introducao/imagem4.png" width="50%" alt="Texto Alternativo">


### ✔️ **Grafos (Graphs):** 
o grafo (graph) é um conjunto de nós (ou vértices), ordenados ou não e ligados por arestas, formando uma estrutura em forma de rede. O grafo abaixo pode ser representado da seguinte forma:

<img src="https://raw.githubusercontent.com/the-akira/PythonExperimentos/master/Algoritmos/Dijkstra/Imagens/Grafo.png" width="50%" alt="Texto Alternativo">

### ✔️**Tabelas Hash (Hash Tables):** 
A função hash é uma função que, a partir de uma entrada de dados, gera um valor numérico que identifica a posição de um elemento em uma tabela hash. Nós já vimos algumas outras estruturas de dados aqui nesse perfil, como buscar um elemento em uma lista encadeada ou em uma árvore binária, e vimos que a complexidade dessas operações é O(n) e O(log n), respectivamente. A tabela hash, por sua vez, consegue fazer essa busca em O(1), ou seja, em tempo constante. Isso significa que, não importa o tamanho da tabela, a busca será feita no mesmo tempo.

**Exemplo de uso:**
Um exemplo clássico de uso de tabela hash é a lista telefônica.

Imagine que você quer encontrar o número de telefone de uma pessoa. Se a lista telefônica fosse uma lista encadeada, você teria que percorrer toda a lista até encontrar o nome da pessoa. Se fosse uma árvore binária, você teria que percorrer a árvore até encontrar o nome da pessoa. Mas, como a lista telefônica é uma tabela hash, você pode encontrar o número de telefone de uma pessoa em tempo constante, ou seja, em O(1). Vamos entender mais sobre isso. Ao adicionar um nome e um número de telefone à lista telefônica, a função hash é usada para gerar um índice para esse nome. Quando você quer encontrar o número de telefone de uma pessoa, a função hash é usada para gerar o índice correspondente ao nome da pessoa, e o número de telefone é retornado.
``` python
class TabelaHash:
    def __init__(self, tamanho=100):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
    
    def hash_func(self, chave):
        return sum(ord(char) for char in chave) % self.tamanho
    
    def inserir(self, nome, telefone):
        indice = self.hash_func(nome)
        if self.tabela[indice] is None:
            self.tabela[indice] = []
        self.tabela[indice].append((nome, telefone))
        print(f"Contato {nome} adicionado com sucesso!")
    
    def buscar(self, nome):
        indice = self.hash_func(nome)
        if self.tabela[indice] is not None:
            for contato in self.tabela[indice]:
                if contato[0] == nome:
                    return contato[1]
        return "Contato não encontrado."
    
    def remover(self, nome):
        indice = self.hash_func(nome)
        if self.tabela[indice] is not None:
            for i, contato in enumerate(self.tabela[indice]):
                if contato[0] == nome:
                    del self.tabela[indice][i]
                    print(f"Contato {nome} removido com sucesso!")
                    return
        print("Contato não encontrado.")
    
    def exibir(self):
        for i, lista in enumerate(self.tabela):
            if lista:
                print(f"Índice {i}: {lista}")

if __name__ == "__main__":
    lista_telefonica = TabelaHash()
    
    while True:
        print("\n1. Adicionar Contato")
        print("2. Buscar Contato")
        print("3. Remover Contato")
        print("4. Exibir Lista Telefônica")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            lista_telefonica.inserir(nome, telefone)
        elif opcao == "2":
            nome = input("Digite o nome a buscar: ")
            print("Telefone:", lista_telefonica.buscar(nome))
        elif opcao == "3":
            nome = input("Digite o nome a remover: ")
            lista_telefonica.remover(nome)
        elif opcao == "4":
            lista_telefonica.exibir()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

```
---

 ### Referencias
 Link | Tipo | Descrição | Autor 
------|--------|--------------| ------------|
https://panda.ime.usp.br/panda/static/pythonds_pt/03-EDBasicos/02-EstruturasLineares.html|Livro|Resolução de Problemas Usando Python|Brad Miller e David Ranum
https://www.alura.com.br/artigos/estruturas-de-dados-introducao|Artigo|Estruturas de dados: uma introdução| Juliana Amoasei
https://www.cin.ufpe.br/~aams/metodos_computacionais/aulaArvores.pdf|Artigo|Métodos Computacionais|UFPE: Universidade Federal de Pernambuco
https://www.dcc.fc.up.pt/~fds/aulas/EDados/2425/apontamentos/7_arvores_1a31.pdf|Artigo|Árvores Binárias|Fernando Silva
https://medium.com/@sschonss/tabelas-hash-1f1a85a83795|Blog|Tabelas Hash|Luiz Schons

1️⃣ Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. – Introduction to Algorithms (3rd Edition). The MIT Press, 2009.
2️⃣ Goodrich, M. T., & Tamassia, R. – Data Structures and Algorithms in Python. Wiley, 2013.
3️⃣ Sedgewick, R., & Wayne, K. – Algorithms (4th Edition). Addison-Wesley, 2011.



