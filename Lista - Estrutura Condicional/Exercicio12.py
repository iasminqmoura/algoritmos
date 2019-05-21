horas = float(input("Insira o valor das horas: "))
quantidadeHoras = int(input("Insira a quantidade de horas mensais: "))

salarioBruto = horas * quantidadeHoras

fgts = salarioBruto * 0.11
sindicato = salarioBruto * 0.03
inss = salarioBruto * 0.10

if salarioBruto <= 900:
    descontos = sindicato + inss

elif salarioBruto > 900 and salarioBruto <= 1500:
    imposto = salarioBruto * 0.05
    descontos = sindicato + inss + imposto

elif salarioBruto > 1500 and salarioBruto <= 2500:
    imposto = salarioBruto * 0.10
    descontos = sindicato + inss + imposto

elif salarioBruto > 2500:
    imposto = salarioBruto * 0.20
    descontos = sindicato + inss + imposto

print("Salário bruto: ", salarioBruto)
print("Sindicato: ", sindicato)
print("IR: ", imposto)
print("INSS: ", inss)
print("FGTS: ", fgts)
print("Total de descontos: ", descontos)
print("Salário líquido: ", salarioBruto - descontos)