opçao = 0

while (opçao != 4):
        print('1 - NOVO SALARIO')
        print('2 - FERIAS')
        print('3 - DECIMO TERCEIRO')
        print('4 - SAIR')

        opçao = int(input('DIGITE A OPÇÃO DESEJADA: '))

        if opçao == 1:
            print('=' * 20)
            print('1- NOVO SALARIO')
            print('=' * 20)
            salario = float(input('DIGITE O VALOR DO SALARIO: '))
            if salario <= 350:
                salario = salario * 1.15
                print('=' * 20)
                print(f'O NOVO SALARIO É R$ {salario :.2f}')
                print('=' * 20)
            elif salario > 350 and salario <= 600:
                salario = salario * 1.10
                print('=' * 20)
                print(f'NOVO SALARIO É R$ {salario :.2f}')
                print('=' * 20)
            else:
                salario = salario * 1.05
                print('=' * 20)
                print(f'O NOVO SALARIO É R$ {salario :.2f}')
                print('=' * 20)
        elif opçao == 2:
            print('=' * 20)
            print('2 - FERIAS')
            print('=' * 20)
            salario = float(input('DIGITE O VALOR DO SALARIO: '))
            salario = salario + salario / 3
            print(f'SALARIO + FERIAS R$: {salario :.2f}')
        elif opçao == 3:
            print('=' * 20)
            print('3 - DECIMO TERCEIRO')
            print('=' * 20)
            salario = float(input('DIGITE O VALOR DO SALARIO: '))
            meses = float(input('DIGITE A QUANTIDADE DE MESES TRABALHADOS: '))
            salario13 = (salario * meses / 12)
            print("Valor do décimo terceiro salário é: ", salario13)

        elif opçao == 4:
            print('=' * 20)
            print('4- SAIR')
            print('=' * 20)

        else:
            print('=' * 20)
            print('OPÇÃO INVALIDA')
            print('=' * 20)