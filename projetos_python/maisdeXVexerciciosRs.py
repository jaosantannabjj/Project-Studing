# 16 exercício
name = 'João Victor'
print('Analisando...')
print(f'Seu nome em letras minusculas é {name.lower()}')
print(f'Seu nome em letras maiúsculas é {name.upper()}')
print(f'Seu nome ao todo tem {len(name.replace(" ", ""))}')
print(f'Seu primeiro nome é {name.split()[0]}')


# 15 exercício
import random
lista = ['Rafael', 'Juliano', 'Macherano', 'João']
random.shuffle(lista)
print(lista)


# 14 exercício
import random
p1 = 'João Victor'
p2 = 'Adriana Vieira'
p3 = 'Lorena Tamara'
p4 = 'Ygor Alexandre'
lista = [p1, p2, p3, p4]
escolhido = random.choice(lista)
print(f'A pessoa escolhida foi: {escolhido}')


# 13 exercício
from math import sqrt
x  = float(input('Comprimento do cateto opsoto: '))
y = float(input('Comprimento do cateto adjascente: '))
c = (x**2) + (y**2)
print(f'A hipotenusa vai medir: {sqrt(c):.2f}')


# 12 exercício
valor = float(input('Digite um valor: '))
print(f'O valor digitado foi {valor} ele arredondado é {valor:.0f}')


# 11° exercício
days = int(input('Quantos dias alugados? '))
kms = float(input('Quantos Km rodados? '))
d = days * 60
k = kms * 0.15
print(f'O total a pagar é de R${d+k}')


# 10° exercício
c = float(input('Informe a temperatura em °C: '))
print(f'A temperatura de {c}°C corresponde a {(c * 9/5) + 32}°F')


# 9° exercício
sal = float(input('Qual o salário do funcionário? R$'))
print(f'O funcionário que ganhava {sal}, agora com 15% vai ganhar {sal + ((sal * 15) / 100):.2f}')
 

# 8° exercício
p = float(input('Qual é o preço do produto? R$'))
print(f'O produto que custava R${p} com 5% de desconta vai ficar { p - ((p * 5) / 100):.2f}')


# 7° exercício
altura = float(input('Altura: '))
largura = float(input('Largura: '))
print(f'''sua parade tem dimensão de {largura}x{altura} e sua área é de {largura * altura}m²
Para pintar essa parede, você precisará de {(altura * largura) / 2}L de tinta.''')


# 6° exercício
n1 = float(input('Quanto dinheiro você tem na carteira R$: '))
print(f'com R${n1} você pode comprar U$:{n1 / 5.35:.2f}')


# 5° exercício
n1 = int(input('Digite n°: '))
print(f'{n1} x {1} = {n1 * 1}')
print(f'{n1} x {2} = {n1 * 2}')
print(f'{n1} x {3} = {n1 * 3}')
print(f'{n1} x {4} = {n1 * 4}')
print(f'{n1} x {5} = {n1 * 5}')
print(f'{n1} x {6} = {n1 * 6}')
print(f'{n1} x {7} = {n1 * 7}')
print(f'{n1} x {8} = {n1 * 8}')
print(f'{n1} x {9} = {n1 * 9}')
print(f'{n1} x {10} = {n1 * 10}')


# 4° exercício
medida = float(input('Digite uma medida: '))
print(f'A medida de {medida} em cm é {medida * 100}')
print(f'A medida de {medida} em mm é {medida * 1000}')


# 3° exercício
from math import sqrt
n1 = int(input('Digite um número: '))
print(f'O dobro de {n1} é igual a {n1 * 2}')
print(f'O triplo de {n1} é igual a {n1 * 3}')
print(f'A raiz quadrade de {n1} é igual a {sqrt(n1):.2f}')


# 2° exercício
n1 =  int(input('Digite um valor: '))
print(f'Analisando o valor {n1}, seu antecessor é {n1-1} e o sucessor é {n1+1}')


# 1° exercício
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
print(f'O A soma de de {n1} e {n2} é: {n1+n2}')