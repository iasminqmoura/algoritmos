nota1 = float(input("Insira a nota da primeira prova: "))
nota2 = float(input("Insira a nota da segunda prova: "))
nota3 = float(input("Insira a nota da terceira prova: "))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
  print("Aprovado com distinção")
elif media >= 7 and media < 10:
  print("Aprovado")
elif media < 7:
  print("Reprovado")