# 📌 Pilhas

Uma **pilha** (stack) é uma estrutura de dados linear que segue o princípio **LIFO** (Last In, First Out), ou seja, o último elemento inserido é o primeiro a ser removido.

## 🔹 Operações Principais:
- **Empilhar (push)**: Adiciona um elemento ao topo da pilha.
- **Desempilhar (pop)**: Remove o último elemento da pilha.
- **Topo da pilha**: (`stack[-1]` para acessar o último elemento).

## 📝 Exemplo em Python:
```python
# Criando uma pilha
pilha = []

# Empilhando elementos
pilha.append("X")
pilha.append("Y")
pilha.append("Z")

# Desempilhando elementos
ultimo = pilha.pop()

# Exibindo a pilha
print("Pilha após remoção:", pilha)
