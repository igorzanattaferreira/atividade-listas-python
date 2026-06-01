###List Comprehension ###
palavras = ['python', 'lista', 'programacao', 'codigo', 'loop', 'funcao']
numeros = list(range(1, 21))

quadrados = [x**2 for x in range(1, 11)]

pares = [x for x in numeros if x % 2 == 0]

tamanhos = [len(p) for p in palavras]

longas_maiusculas = [p.upper() for p in palavras if len(p) > 5]

tuplas_quadrados = [(x, x**2) for x in range(1, 6)]

print(f"1. Quadrados: {quadrados}")
print(f"2. Pares: {pares}")
print(f"3. Tamanhos: {tamanhos}")
print(f"4. Longas em maiusculas: {longas_maiusculas}")
print(f"5. Tuplas: {tuplas_quadrados}")
