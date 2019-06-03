nota = int(input('Digite a nota : '))
if nota<3:
    print('Conceito E')
elif (nota>=3)and(nota<=5):
    print('Conceito D')
elif (nota == 6) or (nota == 7):
    print('Conceito C')
elif (nota == 8) or (nota == 9):
    print('Conceito B')
elif (nota == 10):
    print('Conceito A')