import PySimpleGUI as sg

# Tema
sg.theme('Reddit')

# Layout
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('Tela de Login', layout)

# Ler Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'JOÃO' and valores['senha'] == '123456':
            sg.popup('Bem vindo, meu amor.')
        else:
            sg.popup('Usuário ou senha incorretos!')

# Fechar janela
janela.close()
