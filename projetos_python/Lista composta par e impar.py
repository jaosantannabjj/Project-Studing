num = [[], []]
valor = 0
for c in range(0, 5):
  valor = int(input(f'Digite um valor {c}x: '))
  if valor % 2 == 0:
    num[0].append(valor)
  else:
    num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados são: {num[0]}')
print(f'Os valores impares digitados são: {num[1]}')