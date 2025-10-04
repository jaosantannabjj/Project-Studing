somadoridade = 0
nome = ''
Homem_v = 0
men20 = 0
for p in range(1, 3+1):
  print(f'----- {p}° PESSOA -----')
  nome = str(input('Nome: '))
  idade = int(input('Idade: '))
  Sexo = str(input('Sexo [M/F]: ')).strip().upper()
  if p == 1 and Sexo == 'M':
    Homem_v = idade
    nome_v = nome
  else:
    if idade > Homem_v and Sexo == 'M':
     Homem_v = idade 
     nome_v = nome
  if idade < 20 and Sexo in 'Ff':
    men20 = men20 +1
  somadoridade += idade
somador = somadoridade / 4
print(f'A media das idade está entre {somador}')
if Homem_v > 0:
  print(f'O homem mais velho tem {Homem_v} e ele se chama {nome_v}.')
else:
  print('Não foi cadastrado nenhum homem')
print(f'Ao todo são {men20} mulheres com menos de 20 anos')