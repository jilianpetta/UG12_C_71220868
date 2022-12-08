def angkahuruf(b) :
    c = []
    penghitung = len(b)
    a = 1
    while a <= penghitung :
        d= a*(-1)
        c.append(b[d])
        a =a+1
    cetak = ''
    for i in range (len(c)) :
        cetak += c[i]
    return cetak
hasil=(input('Masukkan kata untuk dibalik : '))
print(angkahuruf(hasil))
                                                                                                                                                                                                                             
