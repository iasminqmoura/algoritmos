print("Insira a idade no formato de Anos/Meses/Dias. Ex: 20 anos, 2 meses e 7 dias")

ano = int(input("Anos: "))
mes = int(input("Meses: "))
dia = int(input("Dias: "))

if(mes < 0 or mes > 12):
    print("Um ano possui 12 meses, insira um valor entre 0 e 12")
else:
    mesDia = mes * 30

anoDia = ano * 365

totalDias = anoDia + mesDia + dia

print("A idade inserida expressa em dias é: ", totalDias)