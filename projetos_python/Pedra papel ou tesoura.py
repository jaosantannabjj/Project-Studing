from random import randint
itens = ('pedra' , 'papel' , 'tesoura')
computador = randint(0,2)
print('''suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual vai ser sua jogada: '))
print(f'Jogador jogou: {itens[jogador]}')
print(f'Computador jogou: {itens[computador]}')

if computador == 0: #Comptador pedra
  if jogador == 0:
   print('Empatou!')
  elif jogador == 1:
    print('Jogador GANHOU!!')
  elif jogador == 2:
    print('Computador GANHOU!!')
  else:
    print('Jogada INVÁLIDA!')
elif computador == 1: #Computador papel
  if jogador == 1:
    print('empatou')
  elif jogador == 0:
    print('Computador GANHOU!!')
  elif jogador == 2:
    print('Jogador GANHOU!!')
  else:
    print('Jogada INVÁLIDA')
elif computador == 2: #Computador Tesoura
  if jogador == 0:
    print('Jogador GANHOU!!')
  elif jogador == 1:
    print('Computador GANHOU!!')
  elif jogador == 2:
    print('EMPATE!')
  else:
    print('Jogada INVÁlIDA')