### Funções Úteis de Listas ###

notas = [7.5, 8.0, 6.0, 9.5, 5.5, 8.5, 7.0, 9.0, 6.5, 8.0]
nomes = ['Carlos', 'Ana', 'Bruno', 'Ana', 'Diego', 'Ana', 'Bruno']

media = sum(notas) / len(notas)
print(f"Média das notas: {media:.2f}")

maior_nota = max(notas)
menor_nota = min(notas)
acima_da_media = sum(1 for n in notas if n > media)
print(f"Maior nota: {maior_nota} | Menor nota: {menor_nota}")
print(f"Alunos acima da media: {acima_da_media}")

print(f"'Ana' aparece: {nomes.count('Ana')} vezes")

print(f"Primeiro índice de 'Bruno': {nomes.index('Bruno')}")

nomes_unicos = []
for nome in nomes:
    if nome not in nomes_unicos:
        nomes_unicos.append(nome)
print(f"Nomes sem repetição: {nomes_unicos}")