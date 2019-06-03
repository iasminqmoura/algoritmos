nota1 = float(input("Insira a nota da prova 1: "))
nota2 = float(input("Insira a nota da prova 2: "))

media = (nota1 + nota2) / 2

if media > 9 and media <= 10:
  print("Aprovado")
elif media > 7.5 and media <= 9:
  print("Aprovado")
elif media > 6 and media <= 7.5:
  print("Aprovado")
elif media > 4 and media <= 6:
  print("Reprovado")
elif media >= 0 and media <= 4:
  print("Reprovado")
else:
  print("Valores inseridos inválidos, tente novamente.")