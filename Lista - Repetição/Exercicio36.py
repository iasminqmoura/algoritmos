a = 0
c = 0
media = 0
soma_Atura = 0
while a != 'a':
        idade = int(input('idade:'))
        altuta = float(input('altura:'))
        if idade > 50:
            altuta = float(input('altura:'))
            c = c + 1
            soma_Atura = soma_Atura + altuta
        if idade <= 0:
            if c == 0:
                c = 1
        media = soma_Atura / c
        print(media)