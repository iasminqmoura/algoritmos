a = 0
c = 0
contador_canal_quatro = 0
contador_canal_cinco = 0
contador_canal_sete = 0
contador_canal_doze = 0
porcentagem_contador_canal_quatro = 0
porcentagem_contador_canal_cinco = 0
porcentagem_contador_canal_sete = 0
porcentagem_contador_canal_doze = 0
total_pessoas = 0
print('*---*')
print('Tv desligada: 1\nCanal 1: 4\nCanal 2: 5\nCanal 3: 7\nCanal 4: 12')
print('*---*\n')
while a != 'a':
        c = c + 1
        canal = int(input(f'{c} Canal:'))
        pessoas_vendo = int(input(f'{c} Pessoas assistindo:'))
        if canal == 4:
            contador_canal_quatro = contador_canal_quatro + pessoas_vendo
            print('*---*')
        if canal == 5:
            contador_canal_cinco = contador_canal_cinco + pessoas_vendo
            print('*---*')
        if canal == 7:
            contador_canal_sete = contador_canal_sete + pessoas_vendo
            print('*---*')
        if canal == 12:
            contador_canal_doze = contador_canal_doze + pessoas_vendo
            print('*---*')
        if canal == 1:
            c = c - 1
            print('*---*')
        if canal == 0:
            print('*---*')
            c = c - 1
            total_pessoas = contador_canal_quatro + contador_canal_cinco + contador_canal_sete + contador_canal_doze
            if total_pessoas == 0:
                total_pessoas = 1
            porcentagem_contador_canal_quatro = (contador_canal_quatro * 100) / total_pessoas
            porcentagem_contador_canal_cinco = (contador_canal_cinco * 100) / total_pessoas
            porcentagem_contador_canal_sete = (contador_canal_sete * 100) / total_pessoas
            porcentagem_contador_canal_doze = (contador_canal_doze * 100) / total_pessoas
            print(f'{porcentagem_contador_canal_quatro}% das pessoas assintem o canal 4')
            print(f'{porcentagem_contador_canal_cinco}% das pessoas assintem o canal 5')
            print(f'{porcentagem_contador_canal_sete}% das pessoas assintem o canal 7')
            print(f'{porcentagem_contador_canal_doze}% das pessoas assintem o canal 12')
            print('*---*')