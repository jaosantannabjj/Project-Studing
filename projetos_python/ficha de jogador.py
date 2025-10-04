def ficha(jog='<Jogador desconhecido>', gols=0):
    print(f'O {jog} fez {gols} GOLS.')

n  = input('Nome do Jogador: ')
g = input('Número de GOLS: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else: 
    ficha(n, g)