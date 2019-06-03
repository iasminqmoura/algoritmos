nome = str(input('Informe o nome do funcionario : '))
atual_sal = float(input('Informe seu atual salario : '))
new_sal : float = 0
acrescimo : float = 0

if atual_sal <= 400:
    acrescimo = atual_sal*0.15
    new_sal = atual_sal+acrescimo
elif (atual_sal >= 401)and(atual_sal <= 700) :
    acrescimo = atual_sal*0.12
    new_sal = atual_sal+acrescimo
elif (atual_sal >= 701)and(atual_sal <= 1000) :
    acrescimo = atual_sal*0.10
    new_sal = atual_sal+acrescimo
elif (atual_sal >= 1001)and(atual_sal <= 1800) :
    acrescimo = atual_sal*0.07
    new_sal = atual_sal+acrescimo
elif (atual_sal >= 1801)and(atual_sal <= 2500) :
    acrescimo = atual_sal*0.04
    new_sal = atual_sal+acrescimo
elif atual_sal >= 2501 :
    acrescimo = atual_sal*0
    new_sal = atual_sal+acrescimo


print('\n\n\nNome : ',nome)
print('Atual Salário : R$',atual_sal)
print('Acrescimo : R$',acrescimo)
print('Novo Salário : R$',new_sal)
