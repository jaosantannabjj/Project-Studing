numlist = []
while True:
  n = int(input('Digite um número: '))
  numlist.append(n)
  resp = str(input('Quer continuar [S/N]: '))
  if resp == 'N':
    break
numlist.sort(reverse=True)
print(f'Você digitou {len(numlist)} elementos.')
print(f'Os valores em ordem decrescente são {numlist}')
if 5 not in numlist:
  print('O número 5 não foi encontrado.')
else:
  print('O número 5 faz parte da lista.')