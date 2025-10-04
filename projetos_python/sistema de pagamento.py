saldo = float(input('Preço das compras: '))
print('FORMAS DE PAGAMENTO')
print('''[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é sua opção: '))
if opcao == 1:
  desconto = saldo - (saldo * 10) / 100
  print(f'Sua compra de R${saldo} vai custar R${desconto} no final.')
elif opcao == 2:
  desconto = saldo - (saldo * 10) / 100
  print(f'Sia compra de R${saldo} vai custar R${desconto} no final.')
elif opcao == 3:
  print(f'O valor da compra é de R${saldo} a parcela será {saldo / 2} ')
elif opcao == 4:
  parcelas = int(input('Quantas parcelas: '))
  juros = (saldo / parcelas) + (saldo * 2 / 100)
  valor_tot = juros * parcelas
  print(f'''o valor das parcelas em {parcelas}x de R${juros} com JUROS
Sua compra de R${saldo} vai custar R${valor_tot} ''')