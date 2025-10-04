n = (1, 4, 8, 4, 5, 6, 7, 8, 9, 10)

maior = n[0]
menor = n[0]
soma = 0

for c in n:
    soma += c
    if c > maior:
        maior = c
    if c < menor:
        menor = c

print("Maior:", maior)
print("Menor:", menor)
print("Soma:", soma)
