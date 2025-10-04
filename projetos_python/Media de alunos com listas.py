lista = [[]]
resp =  'S'
situacao = ''
alunos = int(input('Quantos alunos você quer cadastrar: '))
for c in range(0, alunos):
  nome = str(input('Qual nome do aluno: '))
  not1 = float(input('Primeira nota: '))
  not2 = float(input('Segunda nota: '))
  soma = (not1 + not2) / 2
  if soma >= 10:
    situacao = 'Aprovado com 100%!'
  elif soma >= 7:
    situacao = 'Aprovado!'
  elif soma >= 5:
    situacao = 'Recuperação!'
  else:
    situacao = 'reprovado!'
  lista2 = [f'\nnome: {nome}', f'\nPrimeira nota: {not1}', f'\nSegunda nota: {not2}', f'\nSoma: {soma}', f'\nSituação: {situacao}']
  lista.append(lista2)
for aluno in lista:
  print('=============================')
  print(*aluno)