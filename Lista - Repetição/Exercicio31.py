a = 0
c = 0
calculo_d_lucro = 0
lucro_maior_q_mil = 0
lucro_inferior_a_duzentos = 0
lucro_total = 0
while a != 'a':
        tipo_de_acao = str(input('tipo de acao:')).upper()
        if tipo_de_acao != 'F':
            preco_compra = float(input('preco de compra:'))
            preco_venda = float(input('preco de venda:'))
            calculo_d_lucro = preco_venda - preco_compra
            lucro_total = lucro_total + (calculo_d_lucro)
            if calculo_d_lucro >= 1000:
                lucro_maior_q_mil = lucro_maior_q_mil + 1
            elif calculo_d_lucro < 200 and calculo_d_lucro >= 1:
                lucro_inferior_a_duzentos = lucro_inferior_a_duzentos + 1
        else:
            print(f'{lucro_maior_q_mil :.2f} acoes com lucro superior a R$1000')
            print(f'{lucro_inferior_a_duzentos :.2f} acoes com lucro inferior a R$200')
            if lucro_total > 0:
                print(f'A empresa teve um lucro de R${lucro_total :.2f}')
            else:
                print(f'A empresa teve um prejuizo de R${lucro_total :.2f}')