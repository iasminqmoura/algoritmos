saldo_med = float(input('Digite o saldo médio : '))
credt : float = 0
if (saldo_med>=0)and(saldo_med<=200):
    credt = saldo_med*0
elif(saldo_med>=201)and(saldo_med<=400):
    credt = saldo_med*0.20
elif(saldo_med>=401)and(saldo_med<=600):
    credt = saldo_med*0.30
elif (saldo_med>=601):
    credt = saldo_med*0.40

print('Saldo Médio : R$',saldo_med)
print('Crédito : R$',credt)
print('Novo Saldo : R$',saldo_med+credt)