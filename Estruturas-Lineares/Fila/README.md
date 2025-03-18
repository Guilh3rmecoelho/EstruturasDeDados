# 📌 Filas

Uma **fila** (queue) é uma estrutura de dados linear que segue o princípio **FIFO** (First In, First Out), ou seja, o primeiro elemento inserido é o primeiro a ser removido.

## 🔵 Operações Principais:
- **Enfileirar (enqueue)**: Adiciona um elemento ao final da fila.
- **Desenfileirar (dequeue)**: Remove o primeiro elemento da fila.
- **Acesso ao primeiro elemento**: (`frente_da_fila`).

## 📝 Exemplo em Python:
```python
from collections import deque

# Criando uma fila
fila = deque()

# Enfileirando elementos
fila.append("A")
fila.append("B")
fila.append("C")

# Desenfileirando elementos
primeiro = fila.popleft()

# Exibindo a fila
print("Fila após remoção:", list(fila))
```
