import time

# Código com tratamento correto de estrutura de dados
# Utiliza um conjunto (set), onde a busca por um elemento é O(1), pois utiliza tabelas hash
print("Executando código com estrutura de dados otimizada...")
inicio = time.time()
conjunto = set()
for i in range(100000):
    conjunto.add(i)
    if i in conjunto:  # Operação eficiente O(1) para busca
        pass
fim = time.time()
print(f"Tempo de execução com estrutura otimizada: {fim - inicio:.4f} segundos")