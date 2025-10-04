princ = []
maior = menor = 0
while True:
   temp = [(input('nome: ')), float(input('peso: '))]
   if len(princ) == 0:
      maior = menor = temp[1]
   else:
      if temp[1] > maior:
         maior = temp[1]
      if temp[1] < menor:
         menor = temp[1]
   resp = input('Quer continuar S/N: ')
   princ.append(temp[:])
   temp.clear()
   if resp in 'Nn':
      break
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}kg peso de: ', end='')
for c in princ:
   if c[1] == maior:
      print(f' {c[0]} ', end='')
print()
print(f'O menor peso foi de {menor}kg peso de:', end='')
for c in princ:
   if c[1] == menor:
      print(f' {c[0]} ', end='')
print()