ingresso_vendido = 26
valor_ingresso = 5
vezes = 1
vendainicial = 120
aux = 0
pontoI = ((5 * 120) - 200)
while valor_ingresso > 0.50:
        valor_ingresso = (valor_ingresso - 0.50)
        print(f'valor do ingrasso:{valor_ingresso}')
        vezes = vezes + 1
        aux = (vezes * ingresso_vendido) + 120
        print(f'ingressos vendidodo:{aux}')
        lucro = (valor_ingresso * aux) - 200
        print(f'o lucro foi de:{lucro}')
        if lucro > pontoI:  # maior lucro possivel
            pontoI = lucro
            print(pontoI,'--->Maoir Lucro:Parcial')
            aux2 = valor_ingresso
            print(aux2,'--->Melhor Preco de Ingresso:Parcial')
        #if lucro < 200 and lucro > 0:  # para mostrar o maior prejuizo superior a 0 e inferior ao valor das despesas
            #preju = lucro
            #print(f'{preju}')
            #print(f'{valor_ingresso}')
        if lucro < 200 and lucro < 0:  # para mostrar o maior prejuizo inferior a 0 e inferior ao valor das despesas
            preju = lucro
            print(f'O maior prejuizo fio de R${preju}')
            print(f'O ingresso estava sendo vendido a R${valor_ingresso} ')
print(f'Melhor valor de venda {pontoI}')
print(f'Melhor valor de ingresso {aux2}')