dias_letivos = 100
c = 0
maior = -9999
menor = 9999
reprovado = 0
reprovado_falta = 0
total_reprovados = 0
print('*---*')
for c in range(2):
        c = c + 1
        n_matricula = (random.randint(10000000, 90000000))
        print(f'Numero da matricula:{n_matricula}')
        nota1 = float(input(f'{c} nota:'))
        if nota1 >= 11:
            print(f'{nota1 :.1f} pontos e uma nota invalida o valor maximo permitido e 10')
            sys.exit()
        nota2 = float(input(f'{c} nota2:'))
        if nota2 >= 11:
            print(f'{nota2 :.1f} pontos e uma nota invalida o valor maximo permitido e 10')
            sys.exit()
        nota3 = float(input(f'{c} nota3:'))
        if nota3 >= 11:
            print(f'{nota3 :.1f} pontos e uma nota invalida o valor maximo permitido e 10')
            sys.exit()
        presenca = int(input(f'presenca em sala de aula:'))
        media_notas = (nota1 + nota2 + nota3) / 3

        if media_notas > maior:
            maior = media_notas
        if media_notas < menor:
            menor = media_notas

        if media_notas >= 6 and presenca >= 40:
            print(f'{media_notas :.2f} pontos.Aluno foi aprovado')
        if media_notas <= 5 and presenca >= 40:
            reprovado = reprovado + 1
            print(f'{media_notas :.2f} pontos.Aluno foi reprovado')
        if media_notas >= 5 and presenca < 40:
            reprovado_falta = reprovado_falta + 1
            print(f'{media_notas :.2f} pontos.Aluno foi reprovado por falta')
        elif presenca <= 39:
            reprovado_falta = reprovado_falta + 1
            print(f'Aluno reprovado por falta')
        print('*---*')