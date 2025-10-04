num = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'{num}') 
print(f'O maior número digitado foi: {max(num)}')
print(f'O menor número digitado foi: {min(num)}')
if 3 in num:
  print('O número 3 foi encontrado na posição: ', num.index(3)+1)
else:
  print('O número 3 não foi encontrado.')
print(f'O número nove foi digitado foi: {num.count(9)}')
for c in num:
  if c % 2 ==0:
    print(f'Os números pares são: {c} ')