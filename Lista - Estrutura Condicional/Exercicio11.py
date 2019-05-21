salario = float(input("Insira o salário: "))

antes = salario

if salario <= 280:
    salario = salario*1.2
    percentual = 20

elif salario > 280 and salario <= 700:
    salario = salario*1.15
    percentual = 15

elif salario > 700 and salario <= 1500:
    salario = salario*1.10
    percentual = 10

elif salario > 1500 :
    salario = salario *1.05
    percentual = 5

print("Salario antes do reajuste: R$", antes)
print("O percentual aplicado: ", percentual, '%')
print("O valor do aumento foi: R$", salario-antes)
print("O novo salário: R$", salario)