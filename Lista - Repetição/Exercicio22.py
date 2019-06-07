ca = 0
cb = 0
cc = 0
cd = 0
idade_1_10_anos = 0
idade_11_20_anos = 0
idade_21_30_anos = 0
idade_mais_de_31_anos = 0
for c in range(5):

        idade = int(input(f'{c + 1}ª idade:'))
        peso = float(input(f'{c + 1}ª Peso:'))

        if idade >= 1 and idade <= 10:
            ca += 1

            idade_1_10_anos = idade_1_10_anos + peso

        if idade >= 11 and idade <= 20:
            cb += 1

            idade_11_20_anos = idade_11_20_anos + peso

        if idade >= 21 and idade <= 30:
            cc += 1

            idade_21_30_anos = idade_21_30_anos + peso

        if idade >= 31:
            cd += 1

            idade_mais_de_31_anos = idade_mais_de_31_anos + peso

if idade_1_10_anos >= 1:

        media_1_a_10_anos = idade_1_10_anos / ca

else:

        media_1_a_10_anos = 0

if idade_11_20_anos >= 11:

        media_11_a_20_anos = idade_11_20_anos / cb

else:
        media_11_a_20_anos = 0

if idade_21_30_anos >= 21:

        media_21_a_30_anos = idade_21_30_anos / cc

else:
        media_21_a_30_anos = 0

if idade_mais_de_31_anos >= 31:
        media_acima_de_31_anos = idade_mais_de_31_anos / cd

else:

        media_acima_de_31_anos = 0