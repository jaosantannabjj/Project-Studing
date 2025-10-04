valores = [100, 50, 20, 10, 5, 2]
saque = int(input('Digite um valor: '))

for notas in valores:
  c = saque // notas 
  print(f'O total de {notas}R$: {c}')
  saque = saque % notas