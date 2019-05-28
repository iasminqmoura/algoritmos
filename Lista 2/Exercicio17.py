a = float(input("Insira o valor de A: "))
b = float(input("Insira o valor de B: "))
c = float(input("Insira o valor de C: "))
d = float(input("Insira o valor de D: "))

soma = (a + b) + (a + b) + (a + d) + (b + c) + (b + d) + (c + d)
mult = (a * b) + (a * b) + (a * d) + (b * c) + (b * d) + (c * d)

print("Adição: ", soma)
print("Multiplicação: ", mult)
