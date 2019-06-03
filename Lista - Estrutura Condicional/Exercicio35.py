peso = float(input('Digite o peso : '))

if peso <= 50:
    print('Sem multa')
else:
    quant : float = peso-50
    multa : float = quant*4
    print('O peso excedeu o permitido em ',quant,' KG \nMulta de R$',multa)

