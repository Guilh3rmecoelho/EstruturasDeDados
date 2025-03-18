📌 Impacto das Estruturas de Dados no Desempenho de um Programa

As estruturas de dados desempenham um papel fundamental no desempenho dos programas, pois influenciam diretamente a eficiência da manipulação e acesso aos dados. A escolha da estrutura certa pode reduzir o consumo de memória e melhorar o tempo de execução, enquanto uma escolha inadequada pode tornar um programa ineficiente.
🚀 Principais Fatores que Afetam o Desempenho
1️⃣ Complexidade de Tempo (Big-O Notation)

A eficiência de uma estrutura de dados é geralmente medida usando a notação Big-O, que descreve como o tempo de execução cresce com o tamanho dos dados.
Estrutura de Dados | Inserção |	Remoção | Busca
------|--------|--------------|------|
Lista Simples (Array)|O(1) no final, O(n) no início|O(n)|O(n)
Fila (Queue)|O(1)|O(1)|O(n)
Pilha (Stack)|O(1)|O(1)|O(n)
Lista Encadeada|O(1)| O(1) (se no início)|O(n)
Dicionário (Hash Table)|O(1)|O(1)|O(1)
Árvore de Busca Binária (BST)|O(log n)|O(log n)|O(log n)

🔹 Uma estrutura como uma hash table é muito eficiente para buscas rápidas (O(1)), enquanto uma lista encadeada é útil quando precisamos de inserção e remoção frequentes sem realocação.
2️⃣ Consumo de Memória

Cada estrutura de dados consome memória de maneira diferente:

  Listas e Arrays armazenam elementos de forma contígua na memória, o que pode exigir realocações.
  Filas e Pilhas podem ser implementadas com arrays ou listas encadeadas, impactando o uso de memória.
  Dicionários (Hash Tables) usam mais espaço para armazenar índices (hashes), mas oferecem buscas rápidas.
  Árvores equilibradas (como AVL ou Red-Black) exigem mais memória devido aos ponteiros adicionais, mas garantem eficiência na busca.

  3️⃣ Casos de Uso e Escolha Certa
  Link | Tipo | Descrição 
------|--------|--------------|
Precisa armazenar e acessar elementos rapidamente pelo índice?|Array/Listas
Precisa processar dados em ordem FIFO?|Fila (Queue)
Precisa processar dados em ordem LIFO?|Pilha (Stack)
Precisa de buscas rápidas e flexíveis?|Dicionário (Hash Table)
Precisa de busca ordenada e eficiente?|Árvore de Busca Binária (BST)

---

📚 Referências
1️⃣ Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. – Introduction to Algorithms (3rd Edition). The MIT Press, 2009.
2️⃣ Goodrich, M. T., & Tamassia, R. – Data Structures and Algorithms in Python. Wiley, 2013.
3️⃣ Sedgewick, R., & Wayne, K. – Algorithms (4th Edition). Addison-Wesley, 2011.



