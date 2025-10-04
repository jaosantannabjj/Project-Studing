velha = [['O','O','O'], ['O','O','O'], ['O','O','O']]
linha = int (input('Em qual linha você quer digitar(X) : '))
coluna = int (input('Em qual coluna você quer digitar(X) : '))
velha[linha-1][coluna-1] = 'X'
for l in range(0, 3):
  for c in range(0, 3):
    print(f'[{velha[l][c]:^5}]', end='')
  print()