horasTrabalhadas = float(input("Insira a quantidade de horas trabalhadas: "))
valorHoras = float(input("Insira o valor da hora de trabalho: "))
percentualDesconto = float(input("Insira o valor para o percentual de desconto: "))

salarioBruto = horasTrabalhadas * valorHoras
totalDesconto = (percentualDesconto/100) * salarioBruto
salarioLiquido = salarioBruto - totalDesconto

print("Horas trabalhadas: ", horasTrabalhadas)
print("Salário bruto: ", salarioBruto)
print("Descontos: ", totalDesconto)
print("Salário líquido: ", salarioLiquido)
