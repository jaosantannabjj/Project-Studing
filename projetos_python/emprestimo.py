casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salario: '))
ano = int(input('Em quantos anos você quer financiar: '))
minimo = (salario * 30) / 100
parcela = casa / (ano * 12) 
print(f'Valor da parcela é {parcela}')
if parcela <= minimo:
  print('emprestimo concedido!')
else: 
  print('emprestimo negado!')