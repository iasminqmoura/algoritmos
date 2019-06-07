total_idade = 0
total_idade_m = 0
total_idade_f = 0
f = 0
m = 0
for c in range(4):
        c = c + 1
        idade = int(input(f'{c} idade:'))
        sexo = str(input(f'{c} sexo:'))
        if sexo != 'F' and sexo != 'f' and sexo != 'M' and sexo != 'm':
            print('ERRO')
        if idade > 0:
            total_idade = total_idade + idade
        if sexo == 'F' or sexo == 'f':
            f = f + 1
            total_idade_f = total_idade_f + idade
        else:
            m = m + 1
            total_idade_m = total_idade_m + idade

media_idade = total_idade / c
media_idade_m = total_idade_m / m
media_idade_f = total_idade_f / f
print(f'{media_idade :.0f} anos e a idade media do grupo')
print(f'{total_idade_f :.0f} anos e a idade media entre as mulheres')
print(f'{media_idade_m :.0f} anos e a idade media entre os homens')