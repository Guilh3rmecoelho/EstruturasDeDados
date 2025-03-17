import time

# Código sem tratamento de estrutura de dados
# Utiliza uma lista, onde a busca por um elemento é O(n), pois percorre toda a lista
print("Executando código sem estrutura de dados otimizada...")
inicio = time.time()
lista = []
for i in range(100000):
    lista.append(i)
    if i in lista:  # Operação ineficiente O(n) para busca
        pass
fim = time.time()
print(f"Tempo de execução sem estrutura otimizada: {fim - inicio:.4f} segundos\n")


# Explicação:
# No primeiro caso, usamos uma lista, onde a busca por um elemento exige percorrer toda a lista em média O(n) tempo.
# No segundo caso, usamos um conjunto (set), que utiliza uma tabela hash, permitindo buscas em tempo O(1).
# Isso torna o segundo código muito mais eficiente para grandes volumes de dados.
