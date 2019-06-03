gasolina : float = 2.50
alcool : float = 1.90
print('G - Gasolina\nA - Álcool')
tipo = str(input('Qual tipo de combustivel : '))
x = 0
if tipo == 'A':
    x = alcool
elif tipo == 'G':
    x = gasolina
else:
    print('Tipo errado')

y = int(input('Quantos litros ? '))

valor:float
valor_final:float

if x==alcool and y <= 20:
     valor = x*0.03
     valor_final = ((x-valor)*y)
elif x==alcool and y > 20:
    valor = x*0.05
    valor_final = ((x - valor) * y)
elif x==gasolina and y <= 20:
    valor =  x*0.04
    valor_final = ((x - valor) * y)
elif x==gasolina and y > 20:
    valor =  x*0.06
    valor_final = ((x - valor) * y)


print('Valor a ser pago : R$',valor_final)



