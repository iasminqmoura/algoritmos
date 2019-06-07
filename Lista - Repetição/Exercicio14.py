pessoas_more_50_y_e_60_k = 0
media_do_topico_dois = 0
total_150_altura = 0
total_150_altura_soma_dos_anos = 0
olho_de_agua = 0
porcentagem_de_olho_de_agua = 0
ruivo_sem_olhos_azuis = 0
for c in range(2):
        c = c + 1
        idade = int(input(f'{c}º idade:'))
        peso = float(input(f'{c}º peso:'))
        altura = float(input(f'{c}º altura:'))
        cor_dos_olhos = str(input('A para Azul\nP para Preto\nV para Verde\nC para Castanho\nQual a cor dos olhos'))
        if cor_dos_olhos != 'A' and cor_dos_olhos != 'a' and cor_dos_olhos != 'P' and cor_dos_olhos != 'p' and cor_dos_olhos != 'V' and cor_dos_olhos != 'v' and cor_dos_olhos != 'C' and cor_dos_olhos != 'c':
            print('ERRO')
        cor_do_cabelo = str(input('P para Preto\nC para Castanho\nL para Loiro\nR para Ruivo\nQual a cor do cabelo'))
        if cor_do_cabelo != 'P' and cor_do_cabelo != 'p' and cor_do_cabelo != 'C' and cor_do_cabelo != 'c' and cor_do_cabelo != 'L' and cor_do_cabelo != 'l' and cor_do_cabelo != 'R' and cor_do_cabelo != 'r':
            print('ERRO')
        if idade > 50 and peso < 60:
            pessoas_more_50_y_e_60_k = pessoas_more_50_y_e_60_k + 1
        if altura < 150:
            total_150_altura = total_150_altura + 1
            total_150_altura_soma_dos_anos = total_150_altura_soma_dos_anos + idade
        if cor_dos_olhos != 'P' and cor_dos_olhos != 'p' and cor_dos_olhos != 'V' and cor_dos_olhos != 'v' and cor_dos_olhos != 'C' and cor_dos_olhos != 'c':
            olho_de_agua = olho_de_agua + 1
        if cor_do_cabelo == 'R' or cor_do_cabelo == 'r' and cor_dos_olhos != 'A' and cor_dos_olhos != 'a':
            ruivo_sem_olhos_azuis = ruivo_sem_olhos_azuis + 1

media_do_topico_dois = total_150_altura_soma_dos_anos / total_150_altura
porcentagem_de_olho_de_agua = (olho_de_agua * 100) / c

print(f'Tem {pessoas_more_50_y_e_60_k} pessoas com mais de 50 anos e com peso inferior a 60 Kilos')
print(f'{media_do_topico_dois} anos e a media de idade entre pessoas com menos de 150 cm de altura')
print(f'{porcentagem_de_olho_de_agua}% e a porcentagem de pessoas de olhos azuis entre todas as {c} pessoas analisadas')
print(f'{ruivo_sem_olhos_azuis} e o numero de pessoas ruivas que nao tem olhos azuis')