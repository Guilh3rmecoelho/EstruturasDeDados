# Alocação Estática

A alocação estática ocorre com variáveis globais (alocadas fora de funções) ou quando variáveis locais (internas a uma função) são alocadas usando o modificador ''static''. Uma variável alocada estaticamente mantém seu valor durante toda a vida do programa, exceto quando explicitamente modificada.## 🔹 Características

## 🔵 Características
- O tamanho da memória é determinado **antes da execução**.
- A memória **não pode ser alterada** dinamicamente.
- Mais eficiente em termos de velocidade, pois não requer realocação.

### 📝 Exemplo em Python
```python
# Lista com tamanho fixo (Alocação Estática)
lista_estatica = [0] * 5  # Criando uma lista com 5 elementos fixos
print("Lista Estática:", lista_estatica)
```
