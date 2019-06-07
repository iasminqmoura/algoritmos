a = 0
c = 0
maior = -9999
soma_salarios = 0
soma_filhos = 0
media = 0
salario_menor_q = 0
while a != 'a':
        c = c + 1
        salario = float(input(f'{c} salario:'))
        numero_de_filhos = int(input(f'{c} filhos:'))
        if salario >= 0:
            soma_salarios = soma_salarios + salario
            soma_filhos = soma_filhos + numero_de_filhos
            if salario > maior:
                maior = salario
            if salario <= 150:
                salario_menor_q = salario_menor_q + 1
        else:
            media_salarios = soma_salarios / (c - 1)
            print(f'R${media_salarios :.2f} e a  media dos salarios')
            media_filhos = soma_filhos / (c - 1)
            print(f'{media_filhos :.0f} e a media de filhos')
            print(f'R${maior} e o maior salario')
            porcentagem_salario_menor_q = (salario_menor_q * 100) / (c - 1)
            print(f'{porcentagem_salario_menor_q :.2f}% da populacao recebe menos de R$150 por mes')