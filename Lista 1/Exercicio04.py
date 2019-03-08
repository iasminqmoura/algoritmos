idade = int(input("Insira a idade em dias: "))

anos = int(idade / 365)
meses = int(idade % 365 / 30)
dias = int(idade % 30)

print("A idade inserida é: ", anos, " anos ", meses, " meses e ", dias, " dias")

