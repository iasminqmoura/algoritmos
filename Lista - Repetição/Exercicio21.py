numero = int(input("Fatorial de:"))
c = numero
farotial = 1
if numero >= 0:
        print(f'O resultado de {numero}!=', end='')
        while c > 0:
            print(f'{c}', end='')
            print(f'x' if c > 1 else '=', end='')
            farotial *= c  # farotial=farotial*c
            c -= 1  # c=c-1
        print(f'{farotial}')
else:
        print(f'O fatorial de {numero} nao pode ser calculado')