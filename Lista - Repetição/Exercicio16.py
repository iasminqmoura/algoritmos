total_idade = 0
pessoas_mais_De_90_kg_menos_de_150_cm = 0
pessoa_com_idade_entre_10_e_30_e_altura_maior_q_190 = 0
porcentagem_de_pessoa_com_idade_entre_10_e_30_e_altura_maior_q_190 = 0
for c in range(2):
        c = c + 1
        idade = int(input(f'{c} idade:'))
        peso = float(input(f'{c} peso:'))
        altura = float(input(f'{c} altura:'))
        print('*---*')
        if idade > 0:
            total_idade = total_idade + idade
        if peso > 90 and altura < 150:
            pessoas_mais_De_90_kg_menos_de_150_cm = pessoas_mais_De_90_kg_menos_de_150_cm + 1
        if (idade > 10 and idade < 30) and (altura > 190):
            pessoa_com_idade_entre_10_e_30_e_altura_maior_q_190 = pessoa_com_idade_entre_10_e_30_e_altura_maior_q_190 + 1

porcentagem_de_pessoa_com_idade_entre_10_e_30_e_altura_maior_q_190 = (pessoa_com_idade_entre_10_e_30_e_altura_maior_q_190 * 100) / c
media_idade = total_idade / c
print(f'A idade media entre as {c} pessoas analisadas e {media_idade :.0f} anos ')
print(f'{pessoas_mais_De_90_kg_menos_de_150_cm} pessoas tem peso superior a 90 kilos e altura inferios a 1,50 de altura')