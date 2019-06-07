for c in range(15):
    print('-' * 90)
    name_cliente = str(input('O nome do cliente e:')).upper()
    valor = float(input('O valor de compras dele foi de:'))
    if valor > 0 and valor < 1000:
        bonus = print(
            f'O Cliente {name_cliente} teve um valor total de compras de R${valor} e tem um bonus de R${valor * 0.10 :.2f}')
        print('-' * 90, '\n')
    else:
        bonus = print(
            f'O Cliente {name_cliente} teve um valor total de compras de R${valor} e tem um bonus de R${valor * 0.15 :.2f}')
        print('-' * 90, '\n')