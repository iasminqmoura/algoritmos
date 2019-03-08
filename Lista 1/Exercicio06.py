tempo = int(input("Insira o tempo em segundos: "))

horas = int(tempo / 3600)
minutos = int(tempo % 3600 / 60)
segundos = int(tempo % 3600) % 60

print("A hora inserida é: ", horas, " hora(s),", minutos, " minuto(s),", segundos, " segundo(s).")
