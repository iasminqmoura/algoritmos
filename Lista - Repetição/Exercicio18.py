c = 0
while c != 1:
        c = c + 1
        valor_do_carro = float(input('Valor do carro:'))
        a_vista = (valor_do_carro * 0.80)
        seis_parcelas = (valor_do_carro * 1.03)
        valor_De_seis_parcelas=seis_parcelas/6
        doze_parcelas = (valor_do_carro * 1.06)
        valor_De_doze_parcelas=doze_parcelas/12
        dezoito_parcelas = (valor_do_carro * 1.09)
        valor_De_dezoito_parcelas=dezoito_parcelas/18
        vinte_quatro_parcelas = (valor_do_carro * 1.12)
        valor_De_vinte_quatro_parcelas=vinte_quatro_parcelas/24
        trinta_parcelas = (valor_do_carro * 1.15)
        valor_De_trinta_parcelas=trinta_parcelas/30
        trinta_seis_parcelas = (valor_do_carro * 1.18)
        valor_De_trinta_seis_parcelas=trinta_seis_parcelas/36
        quarenta_dois_parcelas = (valor_do_carro * 1.21)
        valor_De_quarenta_dois_parcelas=quarenta_dois_parcelas/42
        quarenta_oito_parcelas = (valor_do_carro * 1.24)
        valor_De_quarenta_oito_parcelas=quarenta_oito_parcelas/48
        cinquenta_quatro_parcelas = (valor_do_carro * 1.27)
        valor_De_cinquenta_quatro_parcelas=cinquenta_quatro_parcelas/54
        sesenta_parcelas = (valor_do_carro * 1.30)
        valor_De_sesenta_parcelas=sesenta_parcelas/60

        print(['a vista', "%.2f" % a_vista, "-"])
        print(['6', "%.2f" % seis_parcelas, "%.2f" % valor_De_seis_parcelas])
        print(['12', "%.2f" % doze_parcelas, "%.2f" % valor_De_doze_parcelas])
        print(['18', "%.2f" % dezoito_parcelas, "%.2f" % valor_De_dezoito_parcelas])
        print(['24', "%.2f" % vinte_quatro_parcelas, "%.2f" % valor_De_vinte_quatro_parcelas])
        print(['30', "%.2f" % trinta_parcelas, "%.2f" % valor_De_trinta_parcelas])
        print(['36', "%.2f" % trinta_seis_parcelas, "%.2f" % valor_De_trinta_seis_parcelas])
        print(['42', "%.2f" % quarenta_dois_parcelas, "%.2f" % valor_De_quarenta_dois_parcelas])
        print(['48', "%.2f" % quarenta_oito_parcelas, "%.2f" % valor_De_quarenta_oito_parcelas])
        print(['54', "%.2f" % cinquenta_quatro_parcelas, "%.2f" % valor_De_cinquenta_quatro_parcelas])
        print(['60', "%.2f" % sesenta_parcelas, "%.2f" % valor_De_sesenta_parcelas])
