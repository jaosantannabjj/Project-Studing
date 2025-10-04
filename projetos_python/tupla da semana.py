semana = 'Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira','Sexta-Feira', 'Sábado'
n = int(input('Escolha um número de um 1 a 7: '))
if 1 <= n <= 7:
  print(semana[n-1])
else:
  print('Número Inválido digite um número de 1 a 7')