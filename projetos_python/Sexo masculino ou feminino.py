sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while sexo not in 'MF': 
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]

if sexo == 'M':
    sexo = 'Masculino'
elif sexo == 'F':
    sexo = 'Feminino'

print(f'O sexo {sexo} foi registrado com sucesso.')