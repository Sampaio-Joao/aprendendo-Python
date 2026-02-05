name = input('Qual o seu nome?')

fat = input(f'Bem vindo, {name}! Qual o faturamento da sua loja?')
fat = fat.lower()
fat = fat.replace("r$", "")
fat = fat.replace(" ", "")
multiplicador = 1
if "mil" in fat or "k" in fat:
    multiplicador = 1000
    fat = fat.replace("mil", "")
    fat = fat.replace("k", "")
fat = int(fat) * multiplicador

custo = input('E qual o seu custo?')
custo = custo.lower()
custo = custo.replace("r$", "")
custo = custo.replace(" ", "")
multiplicador = 1
if "mil" in custo or "k" in custo:
    multiplicador = 1000
    custo = custo.replace("mil", "")
    custo = custo.replace("k", "")
custo = int(custo)*multiplicador

lucro = fat - custo

if lucro > 0:
    print(f"Parabéns! Você teve lucro. Seu lucro foi de {lucro} reais")
else:
    print(f'Você não teve lucro... Seu prejuízo foi de {lucro} reais')
