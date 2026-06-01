### Operações Básicas com Listas ###
turma = [
    ['Zanatta', 8.0, 7.5, 9.0],
    ['Bruno', 6.7, 6.7, 6.7],
    ['Neymar', 9.5, 9.0, 9.5],
    ['Caio_fedido', 5.0, 6.0, 5.5],
    ['Dolisnki', 7.0, 8.5, 7.5],
]

def obter_media(aluno):
    return sum(aluno[1:4]) / 3

print("--- MEDIA DE CADA ALUNO ---")
for aluno in turma:
    print(f"Aluno(a): {aluno[0]} | Media: {obter_media(aluno):.2f}")

melhor_aluno = max(turma, key=obter_media)
print(f"\nMaior media: {melhor_aluno[0]} ({obter_media(melhor_aluno):.2f})")

aprovados = [aluno[0] for aluno in turma if obter_media(aluno) >= 6.0]
reprovados = [aluno[0] for aluno in turma if obter_media(aluno) < 6.0]
print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")

media_geral = sum(obter_media(aluno) for aluno in turma) / len(turma)
print(f"Media geral da turma: {media_geral:.2f}\n")

turma.append(['Felipe', 8.0, 7.5, 8.5])
ranking = sorted(turma, key=obter_media, reverse=True)

print("--- Ranking da Turma (Decrescente) ---")
for posicao, aluno in enumerate(ranking, 1):
    print(f"{posicao} lugar. {aluno[0]} - Media: {obter_media(aluno):.2f}")
