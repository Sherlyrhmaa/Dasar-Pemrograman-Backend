#Contoh 1
def tambah(var1 = 5, var2 = 2):
    return var1 + var2
print( tambah() )
print( tambah(1) )
print( tambah(1,2) )
print( tambah(5,4) )

#Contoh 2
def pangkat(angka, pangkat = 2):
    hasil = 1
    for i in range(0,pangkat):
        hasil = hasil * angka
    return hasil;

print( pangkat(3) )     # 9
print( pangkat(5) )     # 25
print( pangkat(10) )    # 100
print( pangkat(3,3) )   # 27
print( pangkat(5,4) )   # 625
print( pangkat(6,6) )   # 46656