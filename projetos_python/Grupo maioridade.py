from datetime import datetime
ano_atual = datetime.now().year
maior = 0
menor = 0
for c in range(1, 7+1):
  n = int(input(f'Em que ano a {c}° você nasceu: '))
  if ano_atual - n >=18:
    maior = maior +1
  else:
    menor = menor +1
print(f'''Ao todo tivemos {maior} pessoas maiores de idade
E também {menor} pessoas menores de idade ''')