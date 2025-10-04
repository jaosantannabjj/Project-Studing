frase = str(input('Digite uma frase: ')).upper().split()
juntar = ''.join(frase)
palvra = juntar[::-1]
print(juntar)
if juntar == palvra:
  print('é um palindromo')
else:
  print('Não é um palindromo')
