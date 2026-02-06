name = input('Qual o seu nome?')

fat = input(f'Bem vindo, {name}! Qual o faturamento da sua loja?')
fat = fat.lower().replace("r$", "").replace(" ", "")
multiplicador = 1
if "mil" in fat or "k" in fat:
    multiplicador = 1000
    fat = fat.replace("mil", "").replace("k", "")
fat = ''.join(caractere for caractere in fat if caractere.isdigit() or caractere == '.')
fat = float(fat) * multiplicador

custo = input('E qual o seu custo?')
custo = custo.lower().replace("r$", "").replace(" ", "")
multiplicador = 1
if "mil" in custo or "k" in custo:
    multiplicador = 1000
    custo = custo.replace("mil", "").replace("k", "")
#.join junta tudo na nova string ou na atual. isdigit() ve se é número ou não
custo = ''.join(caractere for caractere in custo if caractere.isdigit() or caractere == '.')
custo = float(custo)*multiplicador

lucro = fat - custo

if lucro > 0:
    print(f"Parabéns! Você teve lucro. Seu lucro foi de {lucro} reais")
else:
    print(f'Você não teve lucro... Seu prejuízo foi de {lucro} reais')

#calculando a porcentagem dos lucros
lucro2 = ((fat - custo) / custo) * 100

if lucro2 > 20:
    print(f"Sua porcentagem de lucro foi de {lucro2:.1f}%") # o 1f é para 1 casa depois do ponto (10.5) se for 2f seria 10.50 e assim por diante
elif 10 <= lucro2 <= 20:
    print(f"sua porcentagem de lucro está OK. {lucro2:.1f}%")
else:
    print(f'Sua margem de lucro está baixa. {lucro2:.1f}%')

