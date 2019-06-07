c = 0
todas_as_idades = 0
c_reg = 0
c_bom = 0
c_otimo = 0
media_otima = 0
toda_otima = 0
print('*---*')
for c in range(3):
        c = c + 1
        idade = int(input(f'{c} idade:'))
        opiniao = int(input(f'[1] Regular\n[2] Bom\n[3] Otimo\n{c} Qual sua opiniao:'))
        print('*---*')
        if opiniao == 3:
            c_otimo = c_otimo + 1
            toda_otima = toda_otima + idade
        if opiniao == 1:
            c_reg = c_reg + 1
        if opiniao == 2:
            c_bom = c_bom + 1

media_otima = toda_otima / c_otimo
porc_bom = (c_bom * 100) / c
print(f'{media_otima :.0f} anos e a media das pessoas que responderam Otimo')
print(f'{c_reg} pessoas responderam regular')
print(f'{porc_bom :.2f}% das pessoas respondeu Bom a pessoa entre todas as {c} pessoas analisadas')