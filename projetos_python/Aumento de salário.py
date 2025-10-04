salario = float(input('Digite o seu salário: '))
if salario < 1250:
  new = salario + (salario * 15) / 100
else:
  new = salario + (salario * 10) / 100  
print(new)