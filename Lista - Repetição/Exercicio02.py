esc_num = int(input('Eu escolho o numero '))
num_aux = 0
soma = 0
i = 1
while i <= esc_num:
    num_aux = 1 / i
    soma = soma + num_aux
    print(1, '/', i, '=', num_aux)
    i = i + 1
    print(f'Soma={soma}')
if esc_num < 0:
    print('Numero menor que Zero')