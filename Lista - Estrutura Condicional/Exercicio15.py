a = float(input("Insira o primeiro lado do triângulo: "))
b = float(input("Insira o segundo lado do triângulo: "))
c = float(input("Insira o terceiro lado do triângulo: "))


if abs(b - c) < a < b + c:
  if a == b == c:
    print("É um triângulo equilátero")
  elif a == b or a == c:
    print("É um triângulo isóceles")
  else:
    print("É um triângulo escaleno")

elif abs(a - c) < b < a + c: 
  if a == b == c:
    print("É um triângulo equilátero")
  elif a == b or a == c:
    print("É um triângulo isóceles")
  else:
    print("É um triângulo escaleno")
elif abs(a - b) < c < a + b:
  if a == b == c:
    print("É um triângulo equilátero")
  elif a == b or a == c:
    print("É um triângulo isóceles")
  else:
    print("É um triângulo escaleno")
else:
  print("Os valores inseridos não formam um triângulo.")