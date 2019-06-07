a = 0
c = 0
soma_preco_original = 0
soma_novo_preco = 0
novo_preco = 0
while a != 'a':
        c = c + 1
        codigo = int(input(f'{c} codigo:'))
        if codigo > 0:
            preco = float(input(f'{c} preco:'))
            print(f'R${preco} e o preco original do produto')
            soma_preco_original = soma_preco_original + preco
            novo_preco = preco * 1.20
            print(f'R${novo_preco} e o preco com um aumento de 20%')
            soma_novo_preco = soma_novo_preco + novo_preco
        else:
            media_preco_original = soma_preco_original / (c - 1)
            print(f'R${media_preco_original} e a media dos precos originais dos produtos')
            media_preco_novo = soma_novo_preco / (c - 1)
            print(f'R${media_preco_novo} e a nova media dos precos dos produtos')
