while True:
  nomeus = str(input('Nome de usuário: '))
  email = input('Digite seu email: ')
  senha = input('Crie uma senha: ')
  senhaco = input('Confirme a senha: ')
  if senha == senhaco:
    print('Login criado com sucesso!')
    break
  else:
    print('As senhas não se corrspodem!')

while True:
  uss = input('Digite o usuário ou email: ')
  senhaus = input('Sua senha: ')
  if senhaus == senha and uss == nomeus or uss == email :
    break
print('Login concedido!')
