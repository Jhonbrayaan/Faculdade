letra = input('Digite um caractere alfabético: ')
vogais = ['a','e','i','o','u','A','E','I','O','U']
if ord(letra) >= 69 and ord(letra) <= 90 or ord(letra) >= 97 and ord(letra) <= 122:

if letra in vogais:
    print('Vogal')
else:
    print('Consoante')    