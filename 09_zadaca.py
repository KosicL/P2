def funk(a):
    print("Parni:")
    for i in range(0, a, 2):
        yield i
    print("Neparni:")
    for i in range(1, a, 2):
        yield i

a=int(input("Broj: "))
for i in funk(a):
    print(i)