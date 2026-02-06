nickname = input('Digite seu nickname: ')
nickname = ''.join(caractere for caractere in nickname if caractere.isalpha()) #isdigit para deixar somente números
print(f'Olá {nickname}! Bem vindo')