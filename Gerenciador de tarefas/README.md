# **Gerenciamento de Tarefas com uma Pilha**

## **Descrição do Problema:**

Imagine que você está desenvolvendo um aplicativo simples de gerenciamento de tarefas, onde os usuários podem adicionar tarefas, marcar como concluídas e desfazer a conclusão de tarefas. A tarefa de "desfazer" deve ser tratada de maneira eficiente, ou seja, a tarefa mais recentemente concluída deve ser desfeita primeiro.

A solução ideal para esse tipo de situação é o uso de uma Pilha (Stack), pois ela segue o princípio LIFO (Last In, First Out), ou seja, o último elemento a ser inserido na pilha é o primeiro a ser removido.
Como a Pilha pode ser Usada para Resolver o Problema:

  🔹Adição de Tarefas: Quando uma tarefa é adicionada, ela é empurrada para o topo da pilha.  
  🔹Marcar Tarefa como Concluída: Quando o usuário marca uma tarefa como concluída, ela é também empurrada para a pilha.  
  🔹Desfazer a Conclusão da Última Tarefa: Quando o usuário decide desfazer a conclusão de uma tarefa, basta remover a tarefa do topo da pilha, ou seja, a última tarefa concluída será a primeira a ser desfeita.  

### **Arquitetura do Sistema:**

  🔹Adicionar Tarefa: Adiciona uma tarefa na pilha.  
  🔹Concluir Tarefa: Marca uma tarefa como concluída, empurrando-a para o topo da pilha.  
  🔹Desfazer Conclusão: Remove a tarefa mais recentemente concluída, ou seja, a do topo da pilha.  

### **Passos para Implementação:**

  🔹Criar a estrutura de dados Pilha (Stack) com os métodos básicos: push (adicionar), pop (remover) e peek (verificar o topo da pilha).  
  🔹Criar funções específicas para gerenciar as tarefas.  
  🔹Implementar um menu para que o usuário possa interagir com o aplicativo.  

  ``` python
class Pilha:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.is_empty():
            return self.itens.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.itens[-1]
        else:
            return None

class GerenciadorDeTarefas:
    def __init__(self):
        self.pilha_tarefas = Pilha()

    def adicionar_tarefa(self, tarefa):
        self.pilha_tarefas.push(tarefa)
        print(f"Tarefa '{tarefa}' adicionada.")

    def concluir_tarefa(self):
        if not self.pilha_tarefas.is_empty():
            tarefa = self.pilha_tarefas.pop()
            print(f"Tarefa '{tarefa}' concluída.")
        else:
            print("Não há tarefas para concluir.")

    def desfazer_conclusao(self):
        if not self.pilha_tarefas.is_empty():
            tarefa = self.pilha_tarefas.peek()
            print(f"Desfez a conclusão da tarefa '{tarefa}'.")
        else:
            print("Não há tarefas para desfazer.")

# Exemplo de uso
gerenciador = GerenciadorDeTarefas()

gerenciador.adicionar_tarefa("Comprar leite")
gerenciador.adicionar_tarefa("Estudar Python")
gerenciador.concluir_tarefa()
gerenciador.desfazer_conclusao()
```
### 🔵 **Explicação do Código:**

  1️⃣ Classe Pilha: A classe Pilha contém os métodos básicos de uma pilha, como push, pop, peek e is_empty.  
  2️⃣ Classe GerenciadorDeTarefas: Essa classe usa a pilha para gerenciar as tarefas, permitindo adicionar, concluir e desfazer tarefas.  
  3️⃣ Fluxo de Trabalho: 
  
   🔹O método adicionar_tarefa empurra a tarefa para a pilha.  
   🔹O método concluir_tarefa remove a tarefa mais recente da pilha (marcando-a como concluída).  
   🔹O método desfazer_conclusao reverte a conclusão da última tarefa empurrada para a pilha.  
