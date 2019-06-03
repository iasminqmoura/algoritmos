salario = float(input('Digite o seu salario : '))
financiamento = float(input('Digite o financiamento : '))

if financiamento <= 5*salario:
    print('Financiamento Concedido')
else:
    print('Financiamento Negado')

print('\nObrigado por nos consultar!')