from time import sleep
def maior(* num):
    maior = cont = 0
    print('\nAnalisando números passados...')
    for c in num:
      print(f'{c}', end='', flush=True)
      sleep(0.5)
      cont +=1
      if cont == 0:
         maior = c
      else:
         if c > maior:
            maior = c
    print(f' tem o total de números ditados: {cont}')
    print(f'O maior número digitado foi de: {maior}')
maior(1, 2, 7)
maior(4, 5, 8)
maior(1, 3)
maior(4)