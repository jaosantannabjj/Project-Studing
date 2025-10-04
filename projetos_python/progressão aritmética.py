n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
decimo = n1 + (10 - 1) * n2
for c in range(n1 , decimo + n2, n2):
  print(f'{c} =>' , end=' ')
print('Acabou!')