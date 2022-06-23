import re

a = input("Unesite string: ")
reg1 = re.search("^(L|l).*(K|k)$", a)
reg2 = re.search("[0-5]+", a)
reg3 = re.search("\s", a)
if reg1 and reg2 and reg3:
    print("Uspješno!")
else:
    print("Pokušaj ponovno")