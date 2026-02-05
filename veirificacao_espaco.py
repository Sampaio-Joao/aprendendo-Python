algo = input('Escreva algo: ')

if algo == '':
    print('Você não escreveu nada')
elif algo != algo.strip():
    print('Você deixou espaço no início ou no final')
elif '  ' in algo:
    print('Você deixou espaço duplo')
else:
    print('Pode proseguir')
