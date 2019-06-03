
File : float = 4.9
Alcatra : float = 5.9
Picanha : float = 6.9

tipo = str(input('Qual tipo de carne vai levar ?\nF - File Duplo\nA - Alcatra\nP - Picanha\n'))

if tipo == 'F':
    quant = int(input('Quantos quilos vai levar ?'))
    if quant > 5:
        File = 5.8
        preco = File*quant
    else:
        preco = File*quant

elif tipo == 'A':
    quant = int(input('Quantos quilos vai levar ?'))
    if quant > 5:
        Alcatra = 6.8
        preco = Alcatra*quant
    else:
        preco = Alcatra*quant

elif tipo == 'P':
    quant = int(input('Quantos quilos vai levar ?'))
    if quant > 5:
        Picanha = 7.8
        preco = Picanha*quant
    else:
        preco =Picanha*quant

else:
    print('Erro de seleção')

resp = str(input('Vai pagar com o cartão Tabajara ?\nS - Sim\nN - Não '))
if resp == 'S':
    preco2 = preco*0.95

elif resp == 'N':
    preco2 = preco

else:
    print('Resposta incorreta')

print('   Nota Fiscal')
if tipo == 'A':
    print('Alcatra / ',quant,' KG  / Preço : R$',preco)
elif tipo == 'F':
    print('File Duplo / ', quant, ' KG  / Preço : R$', preco)
elif tipo == 'P':
    print('Picanha / ', quant, ' KG  / Preço : R$', preco)

if resp == 'S':
    print('Método de Pagamento : Cartão Tabajara')
    print('Desconto de 5% = R$',preco2)

else:
    print('Método de Pagamento : Normal')

print('Valor total : R$',preco2)

