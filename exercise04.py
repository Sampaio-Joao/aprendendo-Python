algo = input('Digite algo: ')

print('O tipo primitivo é: ', type(algo))
print('É númerico?', algo.isnumeric())
print('Só tem espaços?', algo.isspace())
print('é em letra minúscula?', algo.islower())
print('É em letra maiúscula?', algo.isupper())
print('É Alpha?', algo.isalpha())
print('é alphanúmerico?', algo.isalnum())
print('é titulo?', algo.istitle())

