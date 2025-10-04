def ajuda(com):
    help(com)

comando = ''
while True:
    comando = input('Função ou biblioteca > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)