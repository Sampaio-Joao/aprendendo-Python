name = input('Qual o seu nome? ')
fat = input(f'Olá {name}! Qual o seu faturamento? \n(Exemplo: 13500 ou 13.5k): ')
fat = fat.lower().replace('r$', '').replace(' ', '')
multiplicador = 1
if 'mil' in fat or 'k' in fat:
    multiplicador = 1000
    fat = fat.replace('mil', '').replace('k','')
fat = float(fat) * multiplicador

custo = input('E o custo que você teve?\n(Exemplo: 10300 ou 10.3k): ')
custo = custo.lower().replace('r$', '').replace(' ', '')
multiplicador = 1
if 'mil' in custo or 'k' in custo:
    multiplicador = 1000
    custo = custo.replace('mil', '').replace('k', '')
custo = float(custo) * multiplicador

lucro = fat - custo
if lucro > 0:
    print(f" Seu lucro foi de {lucro} reais")
else:
    print(f"Você não teve lucro, seu prejuízo foi de {lucro} reais")
