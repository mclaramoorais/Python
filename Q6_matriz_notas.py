notas = [[0.0]*4 for _ in range(5)]

# Leitura das notas
for i in range(5):
    print(f"Aluno {i+1}:")
    for j in range(4):
        notas[i][j] = float(input(f"  Nota {j+1}: "))

# Média de cada aluno
medias_alunos = []
for i in range(5):
    media = sum(notas[i]) / 4
    medias_alunos.append(media)
    print(f"Média do aluno {i+1}: {media:.2f}")

# Aluno com maior média
maior_media = max(medias_alunos)
indice_maior = medias_alunos.index(maior_media)
print(f"Aluno com maior média: {indice_maior+1} (Média: {maior_media:.2f})")

# Média da turma em cada prova
for j in range(4):
    media_prova = sum(notas[i][j] for i in range(5)) / 5
    print(f"Média da turma na prova {j+1}: {media_prova:.2f}")

# Imprime a matriz completa
print("\nMatriz de notas:")
for i in range(5):
    print(f"Aluno {i+1}: {notas[i]}")
input("\nPressione Enter para sair...")
