class Stack:
    def __init__(self):
        # Cria a lista fixa com 10 posições (todas inicialmente None)
        self._data = [None] * 10
        # Quando a pilha estiver vazia, definimos topo = -1
        self._topo = -1

    def push(self, value: int) -> None:
        # Se topo >= 9, significa que já temos 10 elementos (índices 0..9) → overflow
        if self._topo >= 9:
            raise IndexError("Stack overflow")
        self._topo += 1
        self._data[self._topo] = value

    def pop(self) -> int:
        # Se topo == -1, a pilha está vazia → underflow
        if self._topo == -1:
            raise IndexError("Stack underflow")
        value = self._data[self._topo]
        # Limpa a posição, colocando None
        self._data[self._topo] = None
        self._topo -= 1
        return value

    def top(self) -> int:
        # Se topo == -1, não há elemento para retornar → underflow
        if self._topo == -1:
            raise IndexError("Stack underflow")
        return self._data[self._topo]

    def is_empty(self) -> bool:
        # Retorna True se topo == -1 (pilha vazia)
        return self._topo == -1


if __name__ == "__main__":
    pila = Stack()
    print("Digite 10 números inteiros para empilhar:")

    for i in range(10):
        while True:  # Loop para garantir que o usuário insira um número válido
            entrada = input(f"Valor {i + 1}/10: ")
            try:
                numero = int(entrada)  # Tenta converter a entrada para inteiro
                pila.push(numero)  # Salva o número na pilha
                break  # Sai do loop se a entrada for válida
            except ValueError:
                print("Erro: Por favor, insira um número inteiro válido.")
            except IndexError as e:
                print("Erro ao empilhar:", e)
                raise SystemExit(1)

    print("\nDesempilhando todos os elementos:")
    while not pila.is_empty():
        try:
            valor_removido = pila.pop()
            print("Valor removido:", valor_removido)
        except IndexError as e:
            print("Erro ao desempilhar:", e)
            break
    print("Todos os elementos foram desempilhados.")
    input("\nPressione Enter para sair...")
