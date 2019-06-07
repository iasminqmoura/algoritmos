a = 0
c = 0
investimento_total = 0
juros_total = 0
renda_mensal = 0
while a != 'a':
        c = c + 1
        codigo_cliente = int(input('codigo:'))
        if codigo_cliente >= 1:
            valor = float(input('valor:'))
            escolha = int(input('[1] poupacao\n[2] poupanca plus\n[3] fundo de renda fixa\nescolha:'))
            if escolha == 1:
                investimento_total = investimento_total + valor
                renda_mensal = valor * 1.015
                juros_total = juros_total + (renda_mensal - valor)
                print('Tipo de conta:Poupanca')
                print(f'valor investido:{valor :.2f}')
                print(f'Renda mensal:{renda_mensal :.2f}')
            if escolha == 2:
                investimento_total = investimento_total + valor
                renda_mensal = valor * 1.020
                juros_total = juros_total + (renda_mensal - valor)
                print('Tipo de conta:Poupanca Plus')
                print(f'valor investido:{valor :.2f}')
                print(f'Renda mensal:{renda_mensal :.2f}')
            if escolha == 3:
                investimento_total = investimento_total + valor
                renda_mensal = valor * 1.040
                juros_total = juros_total + (renda_mensal - valor)
                print('Tipo de conta:Fundo de investimento fixo')
                print(f'valor investido:{valor :.2f}')
                print(f'Renda mensal:{renda_mensal :.2f}')
        if codigo_cliente <= 0:
            print(f'Total investidos: R${investimento_total :.2f}')
            print(f'Total de juros pagos:{juros_total :.2f}')
            # criar uma variavel de cada um dos if e somar ela no if final