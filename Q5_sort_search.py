def bubble_sort(lista: list[int]) -> None:
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def selection_sort(lista: list[int]) -> None:
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

def linear_search(lista: list[int], alvo: int) -> int:
    for idx, valor in enumerate(lista):
        if valor == alvo:
            return idx
    return -1

def binary_search(lista: list[int], alvo: int) -> int:
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

def main():
    lista = []
    print("Digite 10 números inteiros:")
    while len(lista) < 10:
        try:
            num = int(input(f"{len(lista)+1}/10: "))
            lista.append(num)
        except ValueError:
            print("Valor inválido. Tente novamente.")

    print("Escolha o método de ordenação:")
    print("1 - Bubble Sort")
    print("2 - Selection Sort")
    escolha = input("Opção: ")

    if escolha == '1':
        bubble_sort(lista)
        print("Lista ordenada (Bubble Sort):", lista)
    elif escolha == '2':
        selection_sort(lista)
        print("Lista ordenada (Selection Sort):", lista)
    else:
        print("Opção inválida. Encerrando.")
        return

    try:
        alvo = int(input("Digite o valor a buscar: "))
    except ValueError:
        print("Valor inválido. Encerrando.")
        return

    idx_linear = linear_search(lista, alvo)
    if idx_linear != -1:
        print(f"Busca Linear: encontrado na posição {idx_linear}")
    else:
        print("Busca Linear: não encontrado")

    idx_binaria = binary_search(lista, alvo)
    if idx_binaria != -1:
        print(f"Busca Binária: encontrado na posição {idx_binaria}")
    else:
        print("Busca Binária: não encontrado")

    input("Clique enter para sair")

if __name__ == "__main__":
    main()
