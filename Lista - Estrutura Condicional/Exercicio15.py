a = float(input("Insira o primeiro lado do tri�ngulo: "))
b = float(input("Insira o segundo lado do tri�ngulo: "))
c = float(input("Insira o terceiro lado do tri�ngulo: "))


if abs(b - c) < a < b + c:
  if a == b == c:
    print("� um tri�ngulo equil�tero")
  elif a == b or a == c:
    print("� um tri�ngulo is�celes")
  else:
    print("� um tri�ngulo escaleno")

elif abs(a - c) < b < a + c: 
  if a == b == c:
    print("� um tri�ngulo equil�tero")
  elif a == b or a == c:
    print("� um tri�ngulo is�celes")
  else:
    print("� um tri�ngulo escaleno")
elif abs(a - b) < c < a + b:
  if a == b == c:
    print("� um tri�ngulo equil�tero")
  elif a == b or a == c:
    print("� um tri�ngulo is�celes")
  else:
    print("� um tri�ngulo escaleno")
else:
  print("Os valores inseridos n�o formam um tri�ngulo.")