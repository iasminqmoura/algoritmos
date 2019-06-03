cargo = str(input('Qual o cargo do funcionario : '))
salario = float(input('Digite seu salario : '))

diferenca : float = 0

if cargo=='Gerente':
    diferenca = salario*0.10

elif cargo=='Engenheiro':
    diferenca = salario*0.20

elif cargo=='Tecnico':
    diferenca = salario*0.30

else:
    diferenca = salario*0.40

print('Antigo salario : R$',salario)
print('Novo : R$',salario+diferenca)
print('Diferença : R$',diferenca)