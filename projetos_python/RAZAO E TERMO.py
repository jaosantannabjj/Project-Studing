primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite o número da razão: '))
termo = primeiro 
cont = 1
mais = 10
while mais != 0:
  while cont <= 10: 
    print(f'{termo} =>', end= '')
    termo = termo + razao
    cont += 1
  print('Pausa...')
  mais = int(input('Quantos termos você quer digitar a mais: '))