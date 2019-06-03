print('Responda as seguintes perguntas com : \n1 - Sim\n0 - Não')
result = 0
print('Telefonou para a vítima ? ')
resp = int(input(''))
result += resp
print('Esteve no local do crime ? ')
resp = int(input(''))
result += resp
print('Mora perto da vitima ? ')
resp = int(input(''))
result += resp
print('Devia para a vitima ? ')
resp = int(input(''))
result += resp
print('Já trabalhou com a vítima ? ')
resp = int(input(''))
result += resp
if result == 2:
    print('Suspeito , S-U-S-P-E-I-T-O')
elif result > 2 and result <= 4:
    print('Cumplice')
elif result == 5:
    print('Assassino')
else:
    print('Inocente')
