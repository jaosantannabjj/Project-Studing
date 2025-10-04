num = (int(input('Digite o 1° número: ')), int(input('Digite o 2° número: ')), int(input('Digite o 3° número: ')), int(input('Digite o 4° número: ')), int(input('Digite o 5° número: ')))
print(f'Você digitou {num}')
print(f'O maior número digitado foi: {max(num)}')
print(f'O menor número digitado foi: {min(num)}')
if 9 in num:
  print(f'O número 9 foi digitado: {num.count(9)}x')
else:
  print('Não foi encontrado nenhum 9')
if 3 in num:
    print(f'O número 3 está na posição: {num.index(3)+1}')
else:
    print('O número 3 não foi encotrado')
for c in num:
  if c % 2 == 0:
    print('Os números pares digitados são:', c, end=' ')