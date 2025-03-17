# 📌 Estruturas de Dados: Definição e Importância  

As **estruturas de dados** desempenham um papel crucial no desenvolvimento de software, impactando diretamente a **eficiência, escalabilidade e desempenho** de um programa.  

---

## 🔵 **Estruturas de Dados Lineares e Não Lineares**  

###  **O que são estruturas Lineares**  
Começaremos nosso estudo de estruturas de dados considerando quatro estruturas simples, mas muito uteis. Pilhas, filas, deques e listas são exemplos de coleções de dados cujos itens são ordenados de acordo com ordem que são inseridos ou removidos da estrutura. Uma vez que um item é inserido, fica em uma mesma posição em relação aos demais itens que foram inseridos antes ou que serão inseridos depois.Estruturas lineares podem ser consideradas como tendo duas extremidades,de frente e traseira por exemplo.O que distingue uma estrutura linear de outra é a maneira em que itens são inseridos e removidos, em particular a extremidade onde estes inserções e remoções ocorrem. Por exemplo, uma estrutura pode permitir que novos itens sejam inseridos em apenas uma das extremidades (pilhas e filas). Algumas estruturas podem permitir que itens sejam removidos de ambas as extremidades


## 🟢 **Principais Estruturas Lineares**  

### ✔️ **Pilhas (Stacks)**  
 Uma pilha (stack) é uma coleção ordenada de itens onde a inserção de novos itens e a remoção de itens existentes sempre ocorrem na mesma extremidade. Este extremidade é comumente chamada de topo. A extremidade oposta ao topo é conhecida como base, seguem o princípio **LIFO** (*Last In, First Out*), onde o último elemento inserido é o primeiro a ser removido.  

**Exemplo de uso:**  **Exemplo de uso:** Histórico de navegação em navegadores, desfazer/refazer em editores de texto.  

<div align="center">


(<img src= "https://assets-prod.sumo.prod.webservices.mozgcp.net/media/uploads/gallery/images/2021-07-12-03-10-14-83e595.png" width="30%" alt="Texto Alternativo">

</div>


### ✔️ **Filas (Queues)**  
 Uma fila (queue) é uma coleção ordenada de itens em que a inserção de novos itens acontece em uma extremidade, chamado de “fim” (rear), e a remoção de itens existente ocorre no outro extremo, comumente chamado de “início” (front). Um elemento é inserido no fim da fila e faz o seu caminho em direção ao início, esperando até aquele momento em que é o próximo elemento seja removido. O item inserido mais recentemente na fila deve aguardar no final do coleção. O item que está na coleção há mais tempo está mais próximo do início. Este princípio de ordenação é às vezes chamado de FIFO, primeiro a entrar, primeiro a sair (first-in first-out). Também é conhecido como “primeiro a chegar, primeiro a ser servido” (first-come first-serverd).

 **Exemplo de uso:** Uma fila de supermercado, onde o primeiro a chegar será o primeiro a ser atendido.  
<div align="center">

(<img src="https://img.freepik.com/vetores-gratis/pessoas-que-estao-na-fila-de-supermercado-longa-alinhando-a-ilustracao-de-composicao-plana-horizontal-do-servico-de-atendimento-ao-cliente_1284-29302.jpg" width="50%" alt="Texto Alternativo">



</div>

 


### ✔️ **Deques (Double-ended Queues)**  
 Permitem inserção e remoção de elementos em ambas as extremidades.  
 **Exemplo de uso:** Agendamento de tarefas, algoritmos de backtracking.  

### ✔️ **Listas**  
 Estruturas flexíveis que permitem inserção e remoção de elementos em qualquer posição.  
 **Exemplo de uso:** Representação de menus, armazenamento dinâmico de dados.  

---

📌 **Uso comum:** Implementação de listas de tarefas, sistemas de atendimento (ex: filas de banco).  

---

### ✔️ **Estruturas Não Lineares**  
Os elementos **não seguem uma sequência fixa** e podem ter múltiplas conexões.  

🔵 **Exemplos:**  
- **Árvores (Trees):** `class No: def __init__(self, valor): self.valor = valor; self.esquerda = None`  
- **Grafos (Graphs):** `grafo = {"A": ["B", "C"], "B": ["D"]}`  
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

