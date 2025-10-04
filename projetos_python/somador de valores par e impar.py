soma = 0
cont = 0
for c in range(1, 501, 1):
  if c % 2 == 0:
    soma = soma + c
    cont = cont +1
print(f'a soma de {cont} todos os valores solicitados é de: {soma}')
