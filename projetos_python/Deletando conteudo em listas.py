lista = []
while True:
  lista.append(int(input('Digite um valor: ')))
  resp = input('Quer continuar: [S/N] ')
  if resp in 'Nn':
    break
print(f'Os números adicionados foram: {lista}')
res = input('Você deseja apagar algum número? [S/N] ')
if res == 'S':
  ps = int(input('Informe a posição: '))
  del lista[ps]
print(f'Sua lista ficou: {lista}')