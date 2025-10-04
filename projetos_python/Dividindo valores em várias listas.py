numlist = list()
impar = list()
par =  list()

while True: 
  numlist.append(int(input('Digite um valor: ')))
  resp = input('Quer continuar? [S/N] ').upper()
  if resp == 'N':
    break 

for i, v in enumerate(numlist):
  if v % 2 == 0:
    par.append(v)
  elif v % 2 == 1:
    impar.append(v)
print(f'Os números digitados foi: {numlist}')
print(f'Os número par: {par}')
print(f'Os número impar: {impar}')