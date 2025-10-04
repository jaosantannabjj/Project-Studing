matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
spar = 0
sc3 = 0
for l in range(0, 3):
  for c in range(0, 3):
    print(f'Valor digitado {l, c}: {matriz[l][c]}')
for l in range(0, 3):
  for c in range(0, 3):
    print(f'[{matriz[l][c]:^5}] ', end='')
    if matriz[l][c] % 2 == 0:
      spar += matriz[l][c]
  print()
for l in range(len(matriz)):
  if matriz[l][2] >= 0:
    sc3 += matriz[l][2]
print(spar)
print(sc3)