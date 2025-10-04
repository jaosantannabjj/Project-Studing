def ano_atu(nasc):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - nasc
    if idade < 16 :
        return f'user tem {idade} anos, NÃO VOTA!'
    elif 16 <= idade > 18 or idade > 65:
        return f'user tem {idade} anos, VOTO OPICIONAL!'
    else:
        return f'user tem {idade} anos, VOTO OBRIAGATÓRIO!'
nascimento = int(input('Digite o ano que você nasceu: '))
print(ano_atu(nascimento))