ano = float(input("Insira um ano para descobrir se ele é bissexto: "))

if ano % 4 == 0:
  if ano % 100 == 0:
    if ano % 400:
      print("O ano é bissexto.")
    else:
      print("Não é um ano bissexto.")
  else:
    print("O ano é bissexto.")
else:
  print("Não é um ano bissexto")