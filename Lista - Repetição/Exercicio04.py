n = 0
ordem_lida = list()  # lista onde estão "armazenados" os números recebidos
for n in range(0, 4):  # Delimita as 4 entradas de cada grupo
        num = int(input(f'{n + 1}º número: '))  # Aqui vc lê os 4 números referentes ao respectivo grupo
        ordem_lida.append(num)  # Aqui vc adiciona o número à lista "ordem_lida"
print(f'Essa foi a ordem lida:{ordem_lida}')

ordem_lida2 = list()  # lista onde estão "armazenados" os números recebidos
for n in range(0, 4):  # Delimita as 4 entradas de cada grupo
        num = int(input(f'{n + 1}º número: '))  # Aqui vc lê os 4 números referentes ao respectivo grupo
        ordem_lida2.append(num)  # Aqui vc adiciona o número à lista "ordem_lida"
print(f'Essa foi a ordem lida:{ordem_lida2}')

ordem_lida3 = list()  # lista onde estão "armazenados" os números recebidos
for n in range(0, 4):  # Delimita as 4 entradas de cada grupo
        num = int(input(f'{n + 1}º número: '))  # Aqui vc lê os 4 números referentes ao respectivo grupo
        ordem_lida3.append(num)  # Aqui vc adiciona o número à lista "ordem_lida"
print(f'Essa foi a ordem lida:{ordem_lida3}')

ordem_lida4 = list()  # lista onde estão "armazenados" os números recebidos
for n in range(0, 4):  # Delimita as 4 entradas de cada grupo
        num = int(input(f'{n + 1}º número: '))  # Aqui vc lê os 4 números referentes ao respectivo grupo
        ordem_lida4.append(num)  # Aqui vc adiciona o número à lista "ordem_lida"
print(f'Essa foi a ordem lida:{ordem_lida4}')

ordem_lida5 = list()  # lista onde estão "armazenados" os números recebidos
for n in range(0, 4):  # Delimita as 4 entradas de cada grupo
        num = int(input(f'{n + 1}º número: '))  # Aqui vc lê os 4 números referentes ao respectivo grupo
        ordem_lida5.append(num)  # Aqui vc adiciona o número à lista "ordem_lida"
print(f'Essa foi a ordem lida:{ordem_lida5}')
print('\n')

print('Grupo 1')
print(f'Essa foi a ordem lida:{ordem_lida}')
ordem_lida.sort()
print(f'Essa e a ordem crescente:{ordem_lida}')
ordem_lida.sort(reverse=True)
print(f'Essa e a ordem decrescente:{ordem_lida}')
print('\n')
print('Grupo 2')
print(f'Essa foi a ordem lida:{ordem_lida2}')
ordem_lida2.sort()
print(f'Essa e a ordem crescente:{ordem_lida2}')
ordem_lida2.sort(reverse=True)
print(f'Essa e a ordem decrescente:{ordem_lida2}')
print('\n')
print('Grupo3')
print(f'Essa foi a ordem lida:{ordem_lida3}')
ordem_lida3.sort()
print(f'Essa e a ordem crescente:{ordem_lida3}')
ordem_lida3.sort(reverse=True)
print(f'Essa e a ordem decrescente:{ordem_lida3}')
print('\n')
print('Grupo 4')
print(f'Essa foi a ordem lida:{ordem_lida4}')
ordem_lida4.sort()
print(f'Essa e a ordem crescente:{ordem_lida4}')
ordem_lida4.sort(reverse=True)
print(f'Essa e a ordem decrescente:{ordem_lida4}')
print('\n')
print('Grupo5')
print(f'Essa foi a ordem lida:{ordem_lida5}')
ordem_lida5.sort()
print(f'Essa e a ordem crescente:{ordem_lida5}')
ordem_lida5.sort(reverse=True)
print(f'Essa e a ordem decrescente:{ordem_lida5}')