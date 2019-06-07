a = 0
c = 0
numero_positivo = 0
numero_menor_q_35 = 0
porc_de_numero_entre_50_e_100 = 0
numero_ate_50 = 0
media_positivos = 0
numero_menor_10_ate_20 = 0
porc_numero_menor_10_ate_20 = 0
calculo_porcento_menor_que_50 = 0
while a != 1:
        c = c + 1
        numero = float(input('numero:'))
        if numero <= 35:
            numero_menor_q_35 = numero_menor_q_35 + 1
        if numero >= 1:
            numero_positivo = numero_positivo + numero
        if numero >= 50 and numero <= 100:
            porc_de_numero_entre_50_e_100 = porc_de_numero_entre_50_e_100 + 1
        if numero > 0 and numero <= 50:
            numero_ate_50 = numero_ate_50 + 1
            if numero >= 10 and numero <= 20:
                numero_menor_10_ate_20 = numero_menor_10_ate_20 + 1
        if c == 5:
            calculo_porcento = (porc_de_numero_entre_50_e_100 * 100) / c
            media_positivos = numero_positivo / c
            calculo_porcento_menor_que_50 = (numero_menor_10_ate_20 * 100) / numero_ate_50

            print(f'{numero_menor_q_35} numeros menores que 35')
            print(f'{media_positivos} e a media dos numeros positivos')
            print(f'{calculo_porcento}% dos numeoros estao entre 50 e 100')
            print(f'{calculo_porcento_menor_que_50}% dos numeros ate 50 estao entre 10 e 20')