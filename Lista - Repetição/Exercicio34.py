a = 0
c = 0
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_candidato4 = 0
votos_nulo = 0
votos_branco = 0
porcento_voto_nulo = 0
porcento_voto_branco = 0
while a != 1:
        c = c + 1
        voto = int(input(
            '[1] Candidato 1\n[2] Candidato 2\n[3] Candidato 1\n[4] Candidato 1\n[5] Voto Nulo\n[6] voto Branco\nescolha:'))
        if voto == 1:
            votos_candidato1 = votos_candidato1 + 1
        if voto == 2:
            votos_candidato2 = votos_candidato2 + 1
        if voto == 3:
            votos_candidato3 = votos_candidato3 + 1
        if voto == 4:
            votos_candidato4 = votos_candidato4 + 1
        if voto == 5:
            votos_nulo = votos_nulo + 1
        if voto == 6:
            votos_branco = votos_branco + 1
        if voto == 0:
            print(f'{votos_candidato1} total de votos para o candidato 1')
            print(f'{votos_candidato2} total de votos para o candidato 2')
            print(f'{votos_candidato3} total de votos para o candidato 3')
            print(f'{votos_candidato4} total de votos para o candidato 4')
            porcento_voto_nulo = (votos_nulo * 100) / (c - 1)
            print(f'{porcento_voto_nulo :.2f}% de votos foi nulo')
            porcento_voto_branco = (votos_branco * 100) / (c - 1)
            print(f'{porcento_voto_branco}% de votos foi branco')