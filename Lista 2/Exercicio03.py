paes = float(input("Insira quantos pães foram comprados: "))
broas = float(input("Insira quantas broas foram compradas: "))

vendas = (paes * 0.12) + (broas * 1.50)

poupanca = vendas * 0.1

print("Foi arrecadado ", vendas, " reais das vendas.")
print("O valor a ser depositado na poupança é de: ", poupanca)
