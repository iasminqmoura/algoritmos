valor_total_a_vista = 0
valor_total_a_prazo = 0
c = 0
for c in range(3):
        c = c + 1
        forma_de_pagamento = str(input(f'Formas de pagamento\nV-A vista\nP-A prazo\nQual a forma de pagamento da {c}º compra:'))
        if forma_de_pagamento == 'V' or forma_de_pagamento == 'v':
            valor_da_compra_a_vista = float(input('Qual o valor da compra:'))
            valor_total_a_vista = valor_total_a_vista + valor_da_compra_a_vista
        elif forma_de_pagamento == 'P' or forma_de_pagamento == 'p':
            valor_da_compra_a_prazo = float(input('Qual o valor da compra:'))
            valor_total_a_prazo = valor_total_a_prazo + valor_da_compra_a_prazo
            parcelas = valor_da_compra_a_prazo / 3
            print(f'{parcelas :.2f}')
        else:
            print('!!! Forma de pagamento invalida !!!')

valor_total_das_compras_efetuadas = valor_total_a_vista + valor_total_a_prazo
print(valor_total_das_compras_efetuadas)