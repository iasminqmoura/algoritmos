print("Em que turno você estuda?")
x = str(input("M - Matutino\nV - Vespertino\nN - Noturno\n"))

if x == 'M' or x == 'm':
    print("Bom Dia!")

elif x == 'V' or x == 'v':
    print("Boa Tarde!")

elif x == 'N' or x == 'n':
    print("Boa Noite!")

else:
    print("Valor Inválido!")