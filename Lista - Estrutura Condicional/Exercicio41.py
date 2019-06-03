print('...:: Cardapio ::...')
print('100 - Cachorro quente - R$1.10')
print('101 - Bauru simples - R$1.30')
print('102 - Bauru c/ovo - R$1.50')
print('103 - Hamburger - R$1.10')
print('104 - CheeseBurger - R$1.30')
print('105 - Refrigerante - R$1.00')

item = int(input('Qual o item do pedido : '))
quant = int(input('Quantidade : '))
valor : float = 0

if item == 100:
    valor = quant * 1.10
elif item == 101:
    valor = quant * 1.30
elif item == 102:
    valor = quant * 1.50
elif item == 103:
    valor = quant * 1.10
elif item == 104:
    valor = quant * 1.30
elif item == 105:
    valor = quant * 1.00

print('Valor a ser pago : R$',valor)
