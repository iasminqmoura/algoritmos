numero = int(input('Digite a quantia a ser retirada  : '))

unidade = numero % 10

numero = (numero - unidade)/10

dezena = numero % 10

numero = (numero - dezena)/10
centena = numero

dezena = int(dezena)
centena = int(centena)

print('Notas de 100 : ',centena)
if dezena >= 5:
    print('Notas de 50 : 1 ')
    dezena = dezena - 5
    if dezena > 0:
        print('Notas de 10 : ', dezena)

else:
    print('Notas de 10 : ',dezena)

if unidade >= 5:
    print('Notas de 5 : 1')
    unidade = unidade-5
    if unidade > 0:
        print('Notas de 1 : ', unidade)
else:
    print('Notas de 1 : ',unidade)

