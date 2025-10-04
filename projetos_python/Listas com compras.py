lst = []
while True:
  try:
    if opc == 'L':
      if lst == []:
        print('Não encotrado.')
      else:
        for c, p in enumerate(lst):
          print(f'{c} {p}')
  except:
      print('Selecione uma opção.')
  opc = input('[i] inserir [a] apagar [l] listar: ').upper()
  if opc == 'I':
    lst.append(input('valor: '))
  elif opc =='A':
    ps = input('Escolha a posição: ')
    try:
      indice = int(ps)
      del lst[indice]
    except:
      print('Contúdo não encotrado.')