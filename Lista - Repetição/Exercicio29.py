a = 0
c = 0
maior = -9999
menor = 9999
soma_salario = 0
F_salario_contador = 0
menor_salario = 9999
while a != 'a':
        c = c + 1
        idade = int(input(f'{c} idade:'))
        sexo = str(input(f'{c} [M] Masculo [F] Feminino:')).upper()
        salario = float(input(f'{c} salario:'))
        if idade >= 1:
            soma_salario = soma_salario + salario
            if idade > maior:
                maior = idade
            if idade < menor:
                menor = idade
            if sexo == 'F' and idade <= 200:
                F_salario_contador = F_salario_contador + 1
            if salario < menor_salario:
                idade_d = idade
                sexo_d = sexo
                menor_salario = salario


        else:
            if c == 0:
                c = c + 2
            media_salario = soma_salario / (c - 1)
            print(f'R${media_salario :.2f} e a media do grupo intrevistado')
            print('*---*')
            print(f'{maior} anos e a maior idade entre os membros do grupo')
            print('*---*')
            print(f'{menor} anos e a menor idade entre os membros do grupo')
            print('*---*')
            print(f'{F_salario_contador} mulheres com salario ate R$200')
            print('*---*')
            print(f'{idade_d} anos e a idade da pessoa com o menor salario do grupo')
            print(f'O individuo com menor salario e do sexo:{sexo_d}')
            print(f'R${media_salario} e o menor salario do grupo')
            print('*---*')