valor = float(input('Digite o valor da compra: '))
frase = str(input('Digite o tipo de cliente (comum/vip/premium): ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
if junto == 'COMUM':
  desconto = (valor * 5) / 100
elif junto == 'VIP':
  desconto = (valor * 5) / 100
elif junto == 'PREMIUM':
  desconto = (valor * 20) / 100
print(f'''Valor original da compra: {valor} 
Valor do desconto: {desconto}
Valor a pagar: {valor - desconto}''')