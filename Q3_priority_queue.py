
class Item:
    def __init__(self, valor, prioridade):
        """Cada Item guarda dois números:
          - valor: um número inteiro que representa o “conteúdo” do item
          - prioridade: 1 (alta), 2 (média) ou 3 (baixa)
        """
        # Guardamos os valores dentro do próprio objeto com "self."
        self.valor = valor
        self.prioridade = prioridade


class PriorityQueue:
    def __init__(self):
        # Criamos uma lista com exatamente 10 posições, todas começando vazias (None)
        self._data = [None] * 10
        
        # Quando a fila está vazia:
        # front = 0 significa que o primeiro item está na posição 0
        self._front = 0
        self._rear = -1
        
        # count = 0 significa “não há itens na fila”
        self._count = 0

    def is_empty(self):
      #verifica se a fila está vazia (count == 0)
        return self._count == 0

    def is_full(self):
        #Retorna True se a fila já tiver 10 itens (count == 10).
        #Retorna False se houver espaço para pelo menos mais 1 item.
        # Se count for 10, significa que não cabe mais nada
        return self._count == 10

    def enqueue(self, valor, prioridade):
        #Adiciona um novo Item(valor, prioridade) no fim da fila.
        # Se a fila já tiver 10 itens, não dá para enfileirar mais
        if self.is_full():
            raise IndexError("Fila cheia")

        # Atualiza rear (fim) de forma circular
        self._rear = (self._rear + 1) % 10

        # Insere nosso novo objeto Item na posição calculada
        self._data[self._rear] = Item(valor, prioridade)

        # Agora temos mais um item
        self._count += 1

    def dequeue(self):
       # Remove e retorna o Item de maior prioridade (1 > 2 > 3).
        #Se houver empate de prioridade, retorna o mais antigo (o que estiver mais próximo de front).
        """
               melhor_prio = menor valor de prioridade encontrado (1, 2 ou 3)
               melhor_offset = deslocamento menor (para desempatar quem entrou antes)
               melhor_idx = índice real no array onde vive o Item “vencedor”
        """
        # 1) Se não houver nada para tirar, underflow
        if self.is_empty():
            raise IndexError("Fila vazia")

        # Inicializa variáveis para achar o Item de maior prioridade
        melhor_prio = 4       # 4 é “maior que qualquer prioridade válida” (1,2,3)
        melhor_offset = None  # deslocamento (0,1,2...) relativo a front
        melhor_idx = None     # índice real no array (0 a 9)

        # 2) Percorre todos os itens ativos (de offset=0 até offset=count-1)
        for offset in range(self._count):
            # calcula índice real no array, caminhando circularmente a partir de front
            idx = (self._front + offset) % 10
            item_atual = self._data[idx]

            # Se este item tiver prioridade menor (= mais importante),
            # gravamos ele como “melhor candidato”
            if item_atual.prioridade < melhor_prio:
                melhor_prio = item_atual.prioridade
                melhor_offset = offset
                melhor_idx = idx
            # Se der empate de prioridade (item_atual.prioridade == melhor_prio),
            # não fazemos nada de novo, porque o primeiro que apareceu (menor offset)
            # já é o mais antigo (quem entrou primeiro). Então ignoramos.

        # 3) Agora temos melhor_idx apontando onde está o Item que vai sair
        item_removido = self._data[melhor_idx]

        # 4) Precisamos “fechar o buraco” deixado em melhor_idx:
        #    Movemos todos os elementos à direita de melhor_idx (até rear) uma casa para trás,
        #    preservando a ordem de entrada.
        atual_idx = melhor_idx
        # Vaĺor de loop: count-1, porque após remover um, sobra count-1 elementos para deslocar
        for _ in range(self._count - 1):
            proximo_idx = (atual_idx + 1) % 10
            # copia o item que estava em proximo_idx para a posição atual
            self._data[atual_idx] = self._data[proximo_idx]
            # avança atual_idx
            atual_idx = proximo_idx

        # 5) Limpamos a última posição (onde estava rear),
        #    porque tudo foi movido para trás
        self._data[self._rear] = None

        # 6) Ajustamos rear para a posição anterior, circularmente
        self._rear = (self._rear - 1) % 10

        # 7) Agora há um item a menos
        self._count -= 1

        # Se a fila ficou vazia, resetamos front e rear
        if self._count == 0:
            self._front = 0
            self._rear = -1

        # 8) Devolvemos o Item removido
        return item_removido

    def print_queue(self):
        """Mostra o estado atual da fila, do mais antigo ao mais novo."""
        if self.is_empty():
            print("Fila vazia.")
            return

        print("Fila atual (do mais antigo ao mais novo):")
        # Percorremos todos os itens ativos de offset=0 até offset=count-1
        for offset in range(self._count):
            idx = (self._front + offset) % 10
            item_atual = self._data[idx]
            print(f"  [{offset}] Valor = {item_atual.valor}, Prioridade = {item_atual.prioridade}")


# Ponto de entrada do programa
if __name__ == "__main__":
    pq = PriorityQueue()

    print("=== ENFILEIRAR 10 ITENS COM PRIORIDADE ===")
    i = 0
    # solicitar exatamente 10 itens do usuário
    while i < 10:
        # input() traz uma string com o que o usuário digitou
        texto = input(f"Digite o valor e a prioridade (1=alta,2=média,3=baixa) para o {i+1}° item, separados por espaço:\n> ")
        partes = texto.split()  # divide em pedaços separados por espaço

        # Se não vierem exatamente 2 pedaços, pedimos de novo (valor e prioridade)
        if len(partes) != 2:
            print("Entrada inválida. Digite dois números separados por espaço.")
            continue  # volta ao while sem incrementar i

        # Converte as duas partes em inteiros
        valor = int(partes[0])
        prioridade = int(partes[1])

        # Verifica se a prioridade é 1, 2 ou 3
        if prioridade not in (1, 2, 3):
            print("Prioridade inválida. Use 1, 2 ou 3.")
            continue  # volta ao while sem incrementar i

        # Tenta enfileirar; se der erro de “fila cheia”, aborta o programa
        try:
            pq.enqueue(valor, prioridade)
        except IndexError as e:
            print("Erro ao enfileirar:", e)
            # Encerra o programa com falha (código 1)
            raise SystemExit(1)

        # Se tudo deu certo, incrementa i para contar este item como lido
        i += 1

    # Depois dos 10 itens, mostramos como a fila ficou por dentro
    print("\nEstado final da fila antes de desenfileirar:")
    pq.print_queue()

    print("\n=== DESEMPILHAR TODOS OS ITENS (DEQUEUE) ===")
    # Enquanto não estiver vazia, vamos tirar um item por vez
    while not pq.is_empty():
        try:
            item = pq.dequeue()
            print(f"Item removido → Valor: {item.valor}, Prioridade: {item.prioridade}")
        except IndexError as e:
            # Isso não deveria ocorrer, pois chequeamos is_empty() antes
            print("Erro ao desenfileirar:", e)
            break

    input("\nFila vazia. Aperte Enter para fechar o programa.")
