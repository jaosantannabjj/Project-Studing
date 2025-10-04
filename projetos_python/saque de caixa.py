valores = [100, 50, 20, 10, 5, 2]
seq = 0
saque = int(input('digite o saque: '))
if saque < 2:
  print('Valor inválido!')
else:
  print('Valor sacado foi de:', saque )

for nota in valores:
  print(f'''total de notas de R${nota}: {saque//nota}''')
  saque = saque % nota