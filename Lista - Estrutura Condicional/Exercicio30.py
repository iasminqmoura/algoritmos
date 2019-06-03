not1= float(input('Digite a nota 1 : '))
not2= float(input('Digite a nota 2 : '))
not3= float(input('Digite a nota 3 : '))
not4= float(input('Digite a nota 4 : '))

nota : float = (not1+not2+not3+not4)/4

if nota >= 7:
    print('Aprovado : ',nota,' pontos')
else:
    exam = float(input('Digite a nota do exame : '))
    nota2 : float = (exam+nota)/2


if nota2 >= 5:
    print('Aprovado em exame :',nota2,'pontos')
else:
    print('Reprovado, nota final : ',nota2,' pontos')





