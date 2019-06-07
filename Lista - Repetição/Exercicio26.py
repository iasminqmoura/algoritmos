a = 0
c = 0
soma_dos_numeros = 0
media_dos_numeros = 0
while a != 'a':
        c = c + 1
        numero = int(input(f'digite o {c} numero:'))
        soma_dos_numeros = soma_dos_numeros + numero
        if numero == 0:
            print(f' while encerrado no {c} numero.')
            media_dos_numeros = soma_dos_numeros / (c - 1)
            print(media_dos_numeros)