codigo = int(input('Digite o codigo do produto ? '))
if codigo==1:
    print('Alimento não perecivel')
elif (codigo >= 2) and (codigo <= 4):
    print('Alimento perecivel')
elif (codigo == 5) or (codigo == 6):
    print('Vestuario')
elif codigo == 7:
    print('WTF')
elif (codigo >= 8)and(codigo <=15):
    print('Higiene pessoal')
else:
    print('Inválido')