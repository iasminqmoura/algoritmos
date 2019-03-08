print("Para calcular o valor de X e Y insira os valores: ")

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
d = float(input("D: "))
e = float(input("E: "))
f = float(input("F: "))

x = float(((c*e) - (b*f)) / ((a*e) - (b*d)))
y = float(((a*f) - (c*d)) / ((a*e) - (b*d)))

print("X = ", x, "\nY = ", y)

