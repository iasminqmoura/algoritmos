x = int(input("Insira o primeiro número: "))
y = int(input("Insira o segundo número: "))
z = int(input("Insira o terceiro número: "))

if x > y and x > z:
    if y > z:
        print(z, y, x)
    else:
        print(y, z, x)

if y > x and y > z:
    if x > z:
        print(z, x, y)
    else:
        print(x, z, y)

if z > x and z > y:
    if y > x:
        print(x, y, z)
    else:
        print(y, x, z)