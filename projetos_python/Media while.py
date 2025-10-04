maior = menor = soma = media = cont =  0

resp = 'S'
while resp != 'N':
  num = int(input('Digite um número: '))
  resp = str(input('Quer continuar? [S/N] ')).upper().strip()
  cont += 1
  soma += num
  media = soma / cont
  if cont == 1:
    maior = num
    menor = num
  else:
    if num > maior:
      maior = num
    if num < menor:
      menor = num
print(f'''Você digitou {cont} números e a média entre eles foi {media}
O maior número digitado foi {maior} e o menor foi {menor}''')
