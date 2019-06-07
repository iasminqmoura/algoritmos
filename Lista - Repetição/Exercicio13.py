pessoas_com_mais_de_90_kilos = 0
idades = 0
for c in range(7):
        c = c + 1
        print('*-------------------------------------------*')
        idade = int(input(f'{c}º Idade='))
        peso = float(input(f'{c}º Peso='))
        idades = idades + idade
        media = idades / c
        if peso > 90:
            pessoas_com_mais_de_90_kilos = pessoas_com_mais_de_90_kilos + 1
            print('*-------------------------------------------*')

print('*-------------------------------------------*')
print(f'{pessoas_com_mais_de_90_kilos} pessoas com mais de 90 Kilos')
print('*-------------------------------------------*')
print(f'{media :.0f} anos e a idade media entre os individuos ')
print('*-------------------------------------------*')