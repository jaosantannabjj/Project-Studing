while True:
  n = int(input('Qual valor da tabuada: '))
  if n < 0:
    break
  for c in range(0 , 10+1):
    print(f'{n} x {c} = {n * c}')
print('PROGAMA TABUADA ENCERRADO, Volte sempre!')