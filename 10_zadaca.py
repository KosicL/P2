def obrni(a):
    if (len(a)==1):
        return a
    else:
        return a[-1] + obrni(a[:-1])

print(obrni("ana voli milovana"))