# Questão 2 - Fila Circular
class CircularQueue:
    # Classe para implementar uma fila circular
    def __init__(self):
        self.size = 5
        self.queue = [None] * self.size
        self.front_idx = 0
        self.rear_idx = 0
        self.count = 0

#Procedimento para  criar fila circular
#inicia fila com tamanho 5
    def enqueue(self, nome: str) -> None:
        if self.is_full():
            raise Exception("Queue is full")
        self.queue[self.rear_idx] = nome
        self.rear_idx = (self.rear_idx + 1) % self.size
        self.count += 1
#Procedimento para inserir nome na fila
#verifica se a fila está cheia, se não estiver, insere o nome na posição rear_idx
    def dequeue(self) -> str:
        if self.is_empty():
            raise Exception("Queue is empty")
        nome = self.queue[self.front_idx]
        self.queue[self.front_idx] = None
        self.front_idx = (self.front_idx + 1) % self.size
        self.count -= 1
        return nome
#Procedimento para remover nome da fila
#verifica se a fila está vazia, se não estiver, remove o nome da posição front_idx
    def front(self) -> str:
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front_idx]
# Método para obter o nome na frente da fila sem removê-lo 
    def is_empty(self) -> bool:
        return self.count == 0
# Método para verificar se a fila está vazia 
    def is_full(self) -> bool:
        return self.count == self.size
# Método para verificar se a fila está cheia
    def __str__(self):
        items = []
        idx = self.front_idx
        for _ in range(self.count):
            items.append(self.queue[idx])
            idx = (idx + 1) % self.size
        return str(items)

# Programa principal
def main():
    q = CircularQueue()
    print("Insira 5 nomes:")
    for i in range(5):
        print(f"\nEstado antes da operação {i+1}:")
        print(f"Fila: {q}")
        print(f"Front: {q.front() if not q.is_empty() else 'None'}")
        print(f"Vazia? {q.is_empty()}")
        print(f"Cheia? {q.is_full()}")
        nome = input(f"Nome {i+1}: ")
        q.enqueue(nome)
        print(f"Fila após inserção: {q}")
        
# Inicia o ciclo de atendimento
    while True:
        print("\nNovo ciclo de atendimento:")
        print(f"Fila: {q}")
        print(f"Front: {q.front()}")
        print(f"Vazia? {q.is_empty()}")
        print(f"Cheia? {q.is_full()}")
        novo_nome = input("Novo nome (ou ENTER para sair): ")
        if not novo_nome:
            break
        atendido = q.dequeue()
        print(f"Atendido: {atendido}")
        q.enqueue(novo_nome)
        print(f"Fila após inserção: {q}")

if __name__ == "__main__":
    main()
