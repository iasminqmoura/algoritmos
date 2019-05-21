prodt1 = float(input("Digite o preço do primeiro produto : "))
prodt2 = float(input("Digite o preço do segundo produto : "))
prodt3 = float(input("Digite o preço do terceiro produto : "))

if prodt1 < prodt2 and prodt1 < prodt3:
    print("Você deve comprar o primeiro produto")

if prodt2 < prodt1 and prodt2 < prodt3:
    print("Você deve comprar o segundo produto")

if prodt3 < prodt2 and prodt3 < prodt1:
    print("Você deve comprar o terceiro produto")

if prodt3 == prodt1 and prodt1 == prodt2:
    print("Preços iguais.")