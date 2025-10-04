peso = float(input('Qual é o seu peso: (Kg) '))
alt = float(input('Qual é sua altura: (M) '))
imc = peso / (alt ** 2)
print(f'O IMC dessa pessoa é de: {imc:.1f}')
if imc < 18:
  print('Você esta abaixo do peso!')
elif 18.5 <= imc <= 25:
  print('Você está com o peso ideal!')
elif 25 <= imc < 30:
  print('Você está sobrepeso!')
elif imc >= 40:
  print('Você está em obsidade mórbida')