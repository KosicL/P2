import re

while 1:
    email = input('Unesite E-mail: ')
    eduid = input('Unesite eduid: ')

    reg1 = re.search('^([a-zA-Z]+)[.]([a-zA-Z]+)(@fpmoz.sum.ba)$', email)
    reg2 = re.search('^([a-zA-Z]+)(\d*)(@sum.ba)$', eduid)
    prezime = email[email.index(".")+1:email.index("@")]

    if not reg1:
        print('E-mail mora biti formata ime.prezime@fpmoz.sum.ba')
    elif (not reg2) or (prezime not in eduid[1:len(prezime)+1]) or (not eduid[0]==email[0]):
        print('eduid mora biti formata iprezimeX@sum.ba gdje je i prvo slovo imena + prezime') 
    else:
        print('Uspješna prijava')
        break