p = 0
maisd = 0
mumai = 0
homi = 0
while True:
  idade = int(input('idade: '))
  if idade > 18:
    maisd += 1
  sexo = str(input('Sexo: [M/F] ')).upper().strip()
  if sexo == 'F' and idade > 20:
    mumai +=1
  if sexo == 'M':
    homi += 1
  if sexo != 'M' or sexo != 'F':
    while sexo != 'M' and sexo != 'F':
      sexo = str(input('Sexo: [M/F] ')).upper().strip()
  resp = str(input('Quer continuar: [S/N]'))
  if resp == 'N':
    break
  if resp != 'S' or resp != 'N':
    while resp != 'S' and 'N':
      resp = str(input('Quer continuar: [S/N]'))
print(f'''Ao todo de pessoa com mais de 18 anos : {maisd}
ao todo temos {homi} cadastrados
E temos {mumai} mulheres com mais de 20 anos.''')
