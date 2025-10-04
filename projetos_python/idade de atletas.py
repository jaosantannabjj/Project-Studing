from datetime import date

ano = date.today().year
nasc = int(input('Em que ano você nasceu: '))
idade = ano - nasc

if idade <= 13:
  print(f'''O atleta tem {idade} anos.
Classificação: Mirim''')
elif idade <= 14:
  print(f'''O atleta tem {idade} anos.
Classificação: Infantil ''')
elif idade <= 19: 
  print(f'''O atleta tem {idade} anos.
Classificação: Junior ''')
elif idade <= 25:
  print(f'''O atleta tem {idade} anos.
Classificação: Sênior''')
else:
  print(f'''O atleta tem {idade} anos.
Classificação: MASTER''')