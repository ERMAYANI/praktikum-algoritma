import math
#menghitung luas dan keliling lingkaran dengan jari-jari

#meminta input jari-jari
jari_jari =float(input("memasukkan jari_jari: "))

#menghitung luas lingkaran
luas =  (math.pi * jari-jari*2)

#menghitung keliling lingkaran
keliling = (2 * math.pi * jari-jari)

#membulatkan hasil ke bilangan
luas_bulat = round(luas,2)
keliling_bulat =round(keliling)

#menampilkan hasil perhitungan
print("luas lingkaran(dibulatkan):", luas_bulat)
print("keliling lingkaran(dibulatkan):",keliling_bulat)

