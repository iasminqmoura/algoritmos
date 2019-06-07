resp_sim = 0
resp_nao = 0
woman_sim = 0
men = 0
men_nao = 0
for c in range(3):
        c = c + 1
        sexo = int(input('[1] Mulher\n[2] Homem\nQual o sexo do intrevistado:'))
        gostou = str(input('[S] Sim\n[N] Nao\nEntrevistado gostou do produto?')).upper()
        if gostou == 'S':
            resp_sim = resp_sim + 1
        if gostou == 'N':
            resp_nao = resp_nao + 1
        if sexo == 1 and gostou == 'S':
            woman_sim = woman_sim + 1
        if sexo == 2:
            men = men + 1
        if sexo == 2 and gostou == 'N':
            men_nao = men_nao + 1

porcento_men_nao = (men_nao * 100) / men
print(f'{resp_sim} pessoas gostaram do produto')
print(f'{resp_nao} pessoas nao gostaram do produto')
print(f'{woman_sim} mulheres gostaram do produto')
print(f'{porcento_men_nao}% dos homens intrevistados nao gostaram do produto')