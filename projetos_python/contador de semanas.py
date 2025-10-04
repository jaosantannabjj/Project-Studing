semana = 'Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-feira', 'Sexta-Feira', 'Sábado'
n = int(input('Escolha um número da semana: '))
while True:
  if 1 <= n <= 7:
    break
  n = int(input('Tente novamente, Escolha um número da semana: '))
print(semana[n-1])