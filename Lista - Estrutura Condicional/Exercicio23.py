print('Digite dois números : ')
x =int(input(""))
y = int(input(""))
print('Qual operação deseja realizar entre eles : ')
op = int(input('1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n'))
if op==1:
    resultado = x+y
    print('Resultado : ',resultado)
elif op==2:
    resultado = x-y
    print('Resultado : ',resultado)
elif op==3:
    resultado = x/y
    print('Resultado : ',resultado)
elif op==4:
    resultado = x*y
    print('Resultado : ',resultado)
else:
    print('Opção inválida')