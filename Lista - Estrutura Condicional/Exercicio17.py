ano = float(input("Insira um ano para descobrir se ele � bissexto: "))

if ano % 4 == 0:
  if ano % 100 == 0:
    if ano % 400:
      print("O ano � bissexto.")
    else:
      print("N�o � um ano bissexto.")
  else:
    print("O ano � bissexto.")
else:
  print("N�o � um ano bissexto")