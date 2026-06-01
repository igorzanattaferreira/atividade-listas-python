### Operações Básicas com Listas ###
frutas = ['maca', 'banana', 'laranja', 'uva', 'melancia']
numeros = [10, 25, 3, 47, 8, 15, 30]

print(f'Primeiro e ultimo (positivo): {frutas[0]} e {frutas[4]}')
print(f'Primeiro e ultimo (negativo): {frutas[-5]} e {frutas[-1]}')

frutas.append('morango')
frutas.insert(2, 'kiwi')

frutas.remove('banana')
print(f"Lista frutas modificada: {frutas}")

print("Números maiores que 15:")
for num in numeros:
    if num > 15:
        print(num, end=" ")
print()

print(f"Crescente: {sorted(numeros)}")
print(f"Decrescente: {sorted(numeros, reverse=True)}")
print(f"original: {numeros}")
