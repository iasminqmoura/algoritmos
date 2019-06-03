valor = int(input('Qual o valor a ser pago : '))
pagamento = int(input('Quanto foi dado para pagar : '))

troco :int = pagamento-valor
troco50 = 0
troco20 = 0
troco10 = 0
troco5 = 0
troco2 = 0
troco1 = 0

while True:
    if troco>=50:
        while troco>=50:
            troco50 = troco50+1
            troco = troco-50

    elif troco>=20:
        while troco >= 20:
            troco20  = troco20+1
            troco = troco-20

    elif troco >=10:
        while troco >= 10:
            troco10  =troco10+ 1
            troco =troco -10

    elif troco >=5:
        while troco >= 5:
            troco5  = troco5+1
            troco = troco-5

    elif troco>=2:
        while troco >= 2:
            troco2 = troco2+1
            troco = troco-2

    elif troco>=1:
        while troco >= 1:
            troco1 = troco1+1
            troco = troco-1

    elif troco == 0:
        break;


if troco50 > 0:
    print('Notas de 50 : ',troco50)
if troco20 > 0:
    print('Notas de 20 : ',troco20)
if troco10 > 0:
    print('Notas de 10 : ',troco10)
if troco5 > 0:
    print('Notas de 5 : ',troco5)
if troco2 > 0:
    print('Notas de 2 : ',troco2)
if troco1 > 0:
    print('Notas de 1 : ',troco1)
