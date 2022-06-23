def poz(ime):
    print('Pozdrav', ime, '!')

dobro = lambda ime: print('Dobrodošao', ime, '!')

def treca(funk):
    funk('Leon')

treca(poz)
treca(dobro)