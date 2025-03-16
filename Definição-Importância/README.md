# 📌 Estruturas de Dados: Definição e Importância  

As **estruturas de dados** desempenham um papel crucial no desenvolvimento de software, impactando diretamente a **eficiência, escalabilidade e desempenho** de um programa.  

---

## 🔵 **Estruturas de Dados Lineares vs. Não Lineares**  

### ✔️ **Estruturas Lineares**  
Os elementos são organizados **sequencialmente**, facilitando o acesso e manipulação de dados.  

🔵 **Exemplos:**  
- **Listas (Arrays):** `lista = [1, 2, 3, 4]`  
- **Filas (Queue):** `from collections import deque; fila = deque([1, 2, 3])`  
- **Pilhas (Stack):** `pilha = [1, 2, 3]; pilha.append(4)`  

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

