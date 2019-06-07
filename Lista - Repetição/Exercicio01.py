min=1000
while min<2000:
    min=min+1
    resto=min%11
    if resto==5:
        print(f'{min} esse e numero divisivel por 11 e tem resto igual a 5')