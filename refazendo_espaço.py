name = input('Digite seu nome: ')
if name == '':
    print('Você não escreveu nada')
elif name != name.strip():
    print('Você deixou espaço no início ou no final')
elif '  ' in name:
    print('Você deixou espaço duplo')
else:
    print('Pode proseguir')
          
