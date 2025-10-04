cont = som = num = 0
num = int(input('Digite um número [Digite 999 para parar]: '))
while num != 999: 
  cont +=1
  som += num
  num = int(input('Digite um número [Digite 999 para parar]: '))
print(f'O total de números de digitados foi {som} e a soma entre eles foi {som}')