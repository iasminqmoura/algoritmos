menor15 = 0
maior16menor30 = 0
maior31menor45 = 0
maior46menor60 = 0
mair61 = 0
for c in range(15):
        idade = int(input(f'{c + 1}º Idade:'))
        if idade > 0 and idade <= 15:
            menor15 = menor15 + 1
        elif idade > 15 and idade <= 30:
            maior16menor30 = maior16menor30 + 1
        elif idade > 30 and idade <= 45:
            maior31menor45 = maior31menor45 + 1
        elif idade > 45 and idade <= 60:
            maior46menor60 = maior46menor60 + 1
        elif idade > 60:
            mair61 = mair61 + 1
        else:
            print(f'{idade} de idade e um valor invalido')

total = menor15 + maior16menor30 + maior31menor45 + maior46menor60 + mair61

print('\n')
print('-' * 25)
print(f'Pessoas na faixa etaria ate 15 anos e de{menor15}')
print('-' * 25)
print(f'Pessoas na faixa etaria de 16 anos ate 30 anos e de{maior16menor30}')
print('-' * 25)
print(f'Pessoas na faixa etaria de 31 anos ate 45 anos e de{maior31menor45}')
print('-' * 25)
print(f'Pessoas na faixa etaria de 46 anos ate 60 anos e de{maior46menor60}')
print('-' * 25)
print(f'Pessoas na faixa etaria acima de 61 anos e de{mair61}')
print('-' * 25, '\n')

conta = (menor15 * 100) / total
print(conta)