from random import randint
computador = randint(0, 5)
num = int(input('Digite um número: '))
if num == computador:
  print('Você acertou!')
else: 
  print('Você errou!')