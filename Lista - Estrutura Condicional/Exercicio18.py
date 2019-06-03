dia = int(input("Insira o dia: "))
mes = int(input("Insira o mes: "))
ano = int(input("Insira o ano: "))

if dia > 0 and dia <= 31 and mes > 0 and mes <= 12 and ano > 1000:
  print(dia,"/",mes,"/",ano)
