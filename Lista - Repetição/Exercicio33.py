a = 0
c = 0
while a != 1:
        c = c + 1
        print(f'{c} MENU DE OPCOES')
        print('[1] Media Aritimetica')
        print('[2] Meida Ponderada')
        print('[3] Sair')
        escolha = int(input('Opcao:'))
        if escolha != 1 and escolha != 2 and escolha != 3:
            print('Essa escolha nao e uma das escolhas validas. programa \nENCERRADO')
        if escolha == 1:
            num1 = int(input('valor 1:'))
            num2 = int(input('Valor 2:'))
            media = (num1 + num2) / 2
            print(f'A media dos dois numeros e {media :.1f}')
        if escolha == 2:
            num1 = int(input('valor 1:'))
            peso1 = int(input('Peso 1 vale:'))
            num2 = int(input('valor 2:'))
            peso2 = int(input('Peso 2 vale:'))
            num3 = int(input('valor 3:'))
            peso3 = int(input('Peso 3 vale:'))
            media = (num1 + num2 + num3) / peso1 + peso2 + peso3
            print(f'A media dos tres numeros e {media :.1f}')
        if escolha == 3:
            print('Fim programa')
            break