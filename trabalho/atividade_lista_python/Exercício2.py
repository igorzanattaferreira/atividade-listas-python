### Fatiamento (Slicing) de Listas ###
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

p1 = letras[:4]

p2 = letras[2:7]

p3 = letras[-3:]

p4 = letras[::-1]

p5 = letras[::2]

print(f"1. 4 primeiros: {p1}")
print(f"2. 3 ao 7: {p2}")
print(f"3. 3 ultimos: {p3}")
print(f"4. Invertida: {p4}")
print(f"5. indices pares: {p5}")
