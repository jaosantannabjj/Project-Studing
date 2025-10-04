passagem = float(input('Qual é a distância de sua viagem: '))
if passagem < 200:
  km = passagem * 0.50
  print (f'O valor a ser pago será {km}')
else:
  km = passagem * 0.45
  print (f'O valor a ser pago será {km}')