cpf = '19067173703'
nove_digitos = cpf[:9]
print(nove_digitos)
contador_regressivo = 10
resultado = 0
for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo
    print(f'{resultado}', end=' ')
    contador_regressivo -= 1
print()
digito = (resultado * 10) % 11
digito = digito if digito <= 9 else 0
print(digito)