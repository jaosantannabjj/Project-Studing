frase = str(input('Digite uma frase: ')).upper().strip
print(f'A letra A aprece {frase.count('A')} vezes na frase')
print(f'A primeira letra a aparece na posição {frase.find('A') + 1}')
print(f'A ultima letra de a aparece na posição {frase.rfind('A') + 1}')