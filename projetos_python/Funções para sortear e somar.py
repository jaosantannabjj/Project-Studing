from random import randint
def somador(lst):
  print('Os números sorteados foram: ', end='')
  for c in range(0, 5):
    c = randint(0, 10)
    lista.append(c)
  print(lista)
def somaPar(lst):
  cont = 0
  for a in lst:
    if a % 2 == 0:
      cont += a
  print(f'A somando os valor {lst} a soma de pares foi: {cont}')

lista = []
somador(lista)
somaPar(lista)