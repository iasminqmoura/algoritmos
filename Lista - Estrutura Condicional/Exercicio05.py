nota1 = float(input("Insira a nota da primeira prova: "))
nota2 = float(input("Insira a nota da segunda prova: "))

media = (nota1 + nota2) / 2

if media == 10:
  print("Aprovado com distinção")
elif media >= 7:
  print("Aprovado")
if media < 7:
  print("Reprovado")
