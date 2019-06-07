c = 0
total_idade = 0
while 1 != 0:
        c = c + 1
        idade = int(input(f'{c} idade:'))
        if idade == 0:
            print('Estrutura de Repeticao finalizada')
            print(c)
            print(total_idade)
            media_idades = total_idade / (c - 1)
            print(media_idades)

total_idade = total_idade + idade
print(total_idade)