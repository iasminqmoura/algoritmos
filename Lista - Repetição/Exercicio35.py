a = 0
c = 0
soma_dos_positivos = 0
soma_dos_negativos = 0
soma_dos_grupos = 0
while a != 'a':
        numero = int(input('numero='))
        if numero >= 1:
            soma_dos_positivos = soma_dos_positivos + numero
            print(f'{soma_dos_positivos} resultado parcial')
        if numero <= -1:
            soma_dos_negativos = soma_dos_negativos + numero
            print(f'{soma_dos_negativos} resultado parcial')
        if numero == 0:
            soma_dos_grupos = soma_dos_positivos + (soma_dos_negativos)
            print(f'{soma_dos_positivos} resultado final')
            print(f'{soma_dos_negativos} resultado final')
            print(f'{soma_dos_grupos} resultado da soma dos dois grupos')