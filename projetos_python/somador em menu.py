n1 = int(input('Digite o pirmeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

opcao = 0
while opcao != 5:
  print('''  [ 1 ] Somar 
  [ 2 ] Multiplicar 
  [ 3 ] maior 
  [ 4 ] novos números
  [ 5 ] sair do progama''')
  opcao = int(input('Digite a opção: '))
  if opcao == 1:
    s = n1 + n2
    print(f'A soma de {n1} + {n2} = {s}')
  elif opcao == 2:
    s = n1 * n2
    print(f'A soma de {n1} x {n2} = {s}')
  elif opcao == 3:
    if n1 > n2:
      print(f'{n1} é maior que {n2}')
    elif n1 < n2:
      print(f'{n2} é maior que {n1}')
    else:
      print(f'{n1} e {n2} são iguais.')
  elif opcao == 4:
    n1 = int(input('Digite o pirmeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
            
print('Fim do progama! volte sempre!')