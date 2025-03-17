# 📌 Estruturas de Dados: Definição e Importância  

As **estruturas de dados** desempenham um papel crucial no desenvolvimento de software, impactando diretamente a **eficiência, escalabilidade e desempenho** de um programa.  

---

## 🔵 **Estruturas de Dados Lineares e Não Lineares**  

###  **O que são estruturas Lineares**  
Começaremos nosso estudo de estruturas de dados considerando quatro estruturas simples, mas muito uteis. Pilhas, filas, deques e listas são exemplos de coleções de dados cujos itens são ordenados de acordo com ordem que são inseridos ou removidos da estrutura. Uma vez que um item é inserido, fica em uma mesma posição em relação aos demais itens que foram inseridos antes ou que serão inseridos depois.Estruturas lineares podem ser consideradas como tendo duas extremidades,de frente e traseira por exemplo.O que distingue uma estrutura linear de outra é a maneira em que itens são inseridos e removidos, em particular a extremidade onde estes inserções e remoções ocorrem. Por exemplo, uma estrutura pode permitir que novos itens sejam inseridos em apenas uma das extremidades (pilhas e filas). Algumas estruturas podem permitir que itens sejam removidos de ambas as extremidades


## 🟢 **Principais Estruturas Lineares**  

### ✔️ **Pilhas (Stacks)**  
 Uma pilha (stack) é uma coleção ordenada de itens onde a inserção de novos itens e a remoção de itens existentes sempre ocorrem na mesma extremidade. Este extremidade é comumente chamada de topo. A extremidade oposta ao topo é conhecida como base, seguem o princípio **LIFO** (*Last In, First Out*), onde o último elemento inserido é o primeiro a ser removido.  

**Exemplo de uso:**  **Exemplo de uso:** Histórico de navegação em navegadores
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

 **Exemplo de uso:** **Exemplo de uso:** Sistemas de atendimento (suporte técnico, filas de impressão).
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
 
 **Exemplo de uso:** Agendamento de tarefas, algoritmos de backtracking.  
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
 **Exemplo de uso:**Lista de números  
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


- **Tabelas Hash (Hash Tables):** `tabela = {"nome": "Ana", "idade": 25}`  

📌 **Uso comum:** Sistemas de recomendação, algoritmos de busca, redes sociais.  

---

## 🚀 **Impacto no Desempenho do Programa**  

Escolher a estrutura de dados errada pode impactar negativamente o desempenho do software.  

### **🔴 Código sem otimização (usando lista ao invés de dicionário):**
```python
# Buscando um item em uma lista (O(n) - Ineficiente para grandes volumes)
usuarios = [("Ana", 25), ("Carlos", 30), ("Bruno", 40)]

def buscar_idade(nome):
    for usuario in usuarios:
        if usuario[0] == nome:
            return usuario[1]
    return None

print(buscar_idade("Carlos"))  # Saída: 30

