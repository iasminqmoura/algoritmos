x = int(input('Digite qualquer número : '))

maior = x
menor = x

x = int(input('Digite qualquer número : '))

if x > maior:
    maior = x

if x < menor:
    menor = x

x = int(input('Digite qualquer número : '))

if x > maior:
    maior = x

if x < menor:
    menor = x

print('Maior é : ',maior)

print('Menor é : ',menor)
