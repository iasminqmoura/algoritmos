morango : float = 2.50
maca :float = 1.80

fruta = int(input('Quantos KG de morango irá comprar ? '))

preco:float = 0

if fruta <= 5:
    preco += morango*fruta

elif fruta>5:
    preco += (morango-0.30) * fruta

fruta2 = int(input('Quantos KG de maçã irá comprar ? '))

if fruta2 <= 5:
    preco += maca * fruta2

elif fruta2 > 5:
    preco += (maca - 0.30) * fruta2

if (fruta+fruta2)>8 or preco > 25:
    desc = preco*0.10
    preco = preco-desc

print('O valor total da compra é de : R$',preco)


