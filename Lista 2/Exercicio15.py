tempoViagem = float(input("Insira o tempo de viagem: "))
velocidadeMedia = float(input("Insira a velocidade média durante a viagem: "))

distancia = tempoViagem * velocidadeMedia

litros_usados = distancia / 12

print("Velocidade média: ", velocidadeMedia)
print("Tempo gasto: ", tempoViagem)
print("Distância percorrida: ", distancia)
print("Litros utilizados na viagem: ", litros_usados)