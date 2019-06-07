pessoas_com_mais_de_50_anos = 0
total_de_pessoas_com_idade_entre_10_e_20_anos = 0
total_das_idades_de_pessoas_com_idade_entre_10_e_20_anos = 0
media_das_alturas_de_10_a_20_anos = 0
pessoas_que_tem_menos_de_40_quilos = 0
porcentagem_de_pessoas_com_peso_inferior_a_40_kilos = 0
print('*----------------------------------------------------------------------------*')
for c in range(25):
        c = c + 1
        idade = int(input(f'{c}º idade='))
        if idade > 50:
            pessoas_com_mais_de_50_anos = pessoas_com_mais_de_50_anos + 1
        altura = float(input(f'{c}º altura='))
        if idade >= 10 and idade <= 20:
            total_de_pessoas_com_idade_entre_10_e_20_anos = total_de_pessoas_com_idade_entre_10_e_20_anos + 1
            total_das_idades_de_pessoas_com_idade_entre_10_e_20_anos = total_das_idades_de_pessoas_com_idade_entre_10_e_20_anos + idade
            media_das_alturas_de_10_a_20_anos = total_das_idades_de_pessoas_com_idade_entre_10_e_20_anos / total_de_pessoas_com_idade_entre_10_e_20_anos
        peso = float(input(f'{c}º peso='))
        if peso < 40:
            pessoas_que_tem_menos_de_40_quilos = pessoas_que_tem_menos_de_40_quilos + 1
            print('*----------------------------------------------------------------------------*')
porcentagem_de_pessoas_com_peso_inferior_a_40_kilos = (pessoas_que_tem_menos_de_40_quilos * 100) / c
print(f'{pessoas_com_mais_de_50_anos} com mais de 50 anos')
print('*----------------------------------------------------------------------------*')
print(f'{total_de_pessoas_com_idade_entre_10_e_20_anos} com idades entre 10 e 20 anos')
print('*----------------------------------------------------------------------------*')
print(f'{media_das_alturas_de_10_a_20_anos :.2f} essa e a media das alturas entre pessoas de 10 a 20 anos')
print('*----------------------------------------------------------------------------*')
print(f'{porcentagem_de_pessoas_com_peso_inferior_a_40_kilos :.2f}% dos individuos tem peso inferior a 40 Kilos')
print('*----------------------------------------------------------------------------*')