a = 0
c = 0
while a != 'a':
        c = c + 1
        num1 = int(input('numero:'))
        num2 = int(input('numero:'))
        escolha = int(input('opcoes\n[1] soma\n[2] subtracao\n[3] multiplicar\n[4] divisao\n[5] sair\nqual operacao:'))
        if escolha == 1:
            mais = num1 + num2
            print(mais)
        if escolha == 2:
            menos = num1 - num2
            print(menos)
            # fazer o teste e diminuir o maior pelo menor ou perguntar a forma da subtracao ao usuario
        if escolha == 3:
            vezes = num1 * num2
            print(vezes)
        if escolha == 4:
            dividir = num1 / num2
            print(dividir)
            # fazer o teste e dividir o maior pelo menor ou perguntar a forma da divisa0 ao usuario
        if escolha == 5:
            print('fim')
            break