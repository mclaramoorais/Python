class Node:
    def __init__(self, valor: int, prox: "Node | None" = None):
        # Atribuímos o valor ao atributo self.valor do objeto
        self.valor = valor
        # Atribuímos o ponteiro (próximo) ao atributo self.prox do objeto
        self.prox = prox

class LinkedList:
    def __init__(self):
      
        self.head = None  # cabeça (primeiro nó) começa como None

    def insert_first(self, valor: int) -> None:
        
        # 1) Criamos um Node que recebe:
        #    - valor: o inteiro que vamos armazenar
        #    - prox: a referência ao nó que antes era o head (pode ser None se a lista estava vazia)
        novo_no = Node(valor, self.head)

        # 2) Atualizamos self.head para apontar para o novo nó
        #    Assim, o novo nó passa a ser o primeiro da lista
        self.head = novo_no

    def insert_last(self, valor: int) -> None:
       
        # 1) Criamos o Node que vai ficar no final (prox = None)
        novo_no = Node(valor, None)

        # 2) Se a lista estiver vazia (não há nenhum nó):
        if self.head is None:
            # Basta apontar head para o novo nó
            self.head = novo_no
            return  # terminamos o método

        # 3) Senão, precisamos achar quem é o último nó atualmente.
        atual = self.head  # começamos do primeiro nó
        # Enquanto o campo 'prox' de 'atual' não for None, avançamos:
        while atual.prox is not None:
            atual = atual.prox  # passa para o próximo nó
        # Quando o while terminar, 'atual' é o último nó da lista

        # Agora, basta apontar atual.prox para o novo nó, ligando-o como último
        atual.prox = novo_no

    def remove_first(self) -> int:
        
        # 1) Se a lista estiver vazia, não há o que remover
        if self.head is None:
            raise IndexError("Empty list")

        # 2) Guardamos o valor que está no head (nó a ser removido)
        valor_removido = self.head.valor

        # 3) Atualizamos head para o próximo nó (pode ser None se só havia um elemento)
        self.head = self.head.prox

        # 4) Devolvemos o valor armazenado no nó que acabou de sair
        return valor_removido

    def remove_last(self) -> int:
        # 1) Lista vazia?
        if self.head is None:
            raise IndexError("Empty list")

        # 2) Se há apenas um elemento (head.prox é None), então ele é o último
        if self.head.prox is None:
            # Guardamos o valor
            valor_removido = self.head.valor
            # Removemos o único nó da lista, deixando head = None (lista vazia)
            self.head = None
            return valor_removido

        # 3) Mais de um nó: precisamos achar o penúltimo
        atual = self.head
        # Enquanto o destino de atual.prox (ou seja, atual.prox.prox) não for None,
        # continuamos andando. Quando atual.prox.prox for None, significa que atual.prox é o último.
        while atual.prox.prox is not None:
            atual = atual.prox  # avança para o próximo

        # Agora, atual.prox é o último nó
        # 4) Guardamos o valor do último
        valor_removido = atual.prox.valor
        # Desligamos o último nó: quem era penúltimo (atual) agora passa a ser último, com prox = None
        atual.prox = None
        # Devolvemos o valor do nó removido
        return valor_removido

    def print_list(self) -> None:
        # Começamos mirando no primeiro nó
        atual = self.head

        # Enquanto houver um nó válido em 'atual', imprimimos seu valor e avançamos
        valores = []  # vamos acumular os valores em uma lista de strings
        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.prox  # avança para o próximo nó

        # Imprimos todos os valores separados por espaço
        # Se valores estiver vazio, print("") imprimirá apenas uma linha em branco
        print(" ".join(valores))



#Programa-principal
#    Executa na ordem solicitada:
#    1. insert_first(10), insert_first(20), insert_first(30)  → lista: 30 -> 20 -> 10
#    2. remove_first() → retira 30 • lista: 20 -> 10
#    3. insert_last(40) → lista: 20 -> 10 -> 40
#    4. remove_last() → retira 40 • lista: 20 -> 10
#    5. print_list() → imprime “20 10”

if __name__ == "__main__":
    # Criamos uma lista vazia
    ll = LinkedList()

    # 1) Inserções no início em sequência
    # insert_first(10), insert_first(20), insert_first(30)
    ll.insert_first(10)
    # Depois dessa linha, a lista tem apenas um nó [10]
    ll.insert_first(20)
    # Agora: 20 -> 10
    ll.insert_first(30)
    # Agora: 30 -> 20 -> 10

    # 2) remove_first() -> retira 30
    # Após isso, lista: 20 -> 10
    valor1 = ll.remove_first()  # valor1 = 30 (não usaremos, mas mostramos para entendimento)
    # Se quiséssemos ver, poderíamos imprimir:
    # print("Removeu (primeiro):", valor1)

    # 3) insert_last(40) -> lista: 20 -> 10 -> 40
    ll.insert_last(40)

    # 4) remove_last() -> retira 40
    # Após isso, lista volta a ser: 20 -> 10
    valor2 = ll.remove_last()  # valor2 = 40

    # 5) print_list() -> deve exibir “20 10”
    ll.print_list()
