print("Equação do segundo grau: ax^2 + bx + c")
a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

if a == 0:
  print("a = 0, não é uma equação de segundo grau.")
  
else:
  delta = (b ** 2) + (-4)*(a)*(c)
  print("Delta: ", delta)

  if delta < 0:
    print("Delta não possui raízes reais.")
  else:
    x1 = ((-1 * b) + (delta ** (1/2))) / (2 * a)
    x2 = ((-1 * b) - (delta ** (1/2))) / (2 * a)

    print("Resultado 1: ", x1)
    print("Resultado 2: ", x2)