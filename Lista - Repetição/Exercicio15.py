quantidade = 0
for c in range(3):
        c = c + 1
        numero = int(input(f'Digite o {c}º numero:'))
        if numero >= 30 and numero <= 90:
            quantidade = quantidade + 1

print(f'Dos numeros analisados {quantidade} estao entre 30 e 90')