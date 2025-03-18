# Alocação Dinâmica

Na alocação dinâmica, o programa solicita explicitamente áreas de memória ao sistema operacional, as utiliza e depois as libera quando não forem mais necessárias, ou quando o programa encerrar. As requisições de memória dinâmica são geralmente alocadas na área de memória denominada heap.

## 🔵 Características
- O tamanho da memória é determinado **durante a execução**.
- A memória **pode ser expandida ou reduzida** dinamicamente.
- Mais flexível, mas pode impactar o desempenho se não for bem gerenciada.

## 📝 Exemplo em Python
```python
# Lista dinâmica (cresce conforme necessário)
lista_dinamica = []
for i in range(5):
    lista_dinamica.append(i * 2)  # Adicionando elementos dinamicamente

print("Lista Dinâmica:", lista_dinamica)
```
