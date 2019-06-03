min : float = 999999
max : float = -999999

for x in range(3):
    y = int(input('Digite um número : '))
    if y > max:
        max = y
    elif y < min:
        min = y


print('Maior : ',max,'\nMenor : ',min)
