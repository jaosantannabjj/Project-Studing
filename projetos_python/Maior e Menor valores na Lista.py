p = []
for c in range(0, 5):
  n = int(input(f'Digite um valor {c}: '))
  p.append(n)

maior = max(p)
menor = min(p)

print(f'O MAIOR valor digitado foi: {maior} ele está presente nas posições', end='')
for a, valor in enumerate(p):
  if maior == p[a]:
    print(f' {a}...', end='')
print()
print(f'''O menor valor digitado foi: {menor} ele está presente nas posições''', end='')
for a, valor in enumerate(p):
  if menor == p[a]:
    print(f' {a}...', end='')
