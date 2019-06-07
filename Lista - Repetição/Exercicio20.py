c = 0
valor_total = 0
menor = 9999
maior = -9999
while 1 != 0:
        c = c + 1
        numero = int(input(f'{c} numero do conjunto:'))
        if numero < 0:
            print(f'{numero} e um numero do conjuto e nao entra no calculo')
        if numero == 0:
            print(f'O numero 0 foi detectado no {c} termo do conjunto. Encerrada estrutura de repeticao')
            print(f'{valor_total} e o valor da soma dos conjuntos')
            print(f'{maior} e o maior numero')
            print(f'{menor} e o menor numero')
        if numero > 0:
            valor_total = valor_total + numero
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero