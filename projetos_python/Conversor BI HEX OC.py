num =  int(input('digite um número: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para HEXADECIMAL
[ 3 ] converter para OCTAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
  print(f'{num} convertido para binario é igual {bin(num)[2:]}')
elif opcao ==2:
  print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
elif opcao == 3:
  print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
else:
  print('É 1 , 2 ou 3 mega idiota!')