# Fatorial Recursivo com Tratamento de Erros 
def fatorial(n: int) -> int:
    if n < 0:
        raise ValueError("n deve ser maior ou igual a zero.")
    if n > 998:
        print("Aviso: valores acima de 998 podem exceder o limite de recursão do Python.")
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

# Programa principal para calcular o fatorial
if __name__ == "__main__":
    try:
        n = int(input("Digite um valor para n: "))
        resultado = fatorial(n)
        print(f"{n}! = {resultado}")
    except ValueError as e:
        print(f"Erro: {e}")
    input("Pressione Enter para sair...")
