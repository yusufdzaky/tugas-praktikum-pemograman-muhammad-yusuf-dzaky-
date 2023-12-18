nama    = 'Muhammad Yusuf Dzaky Jasman'
nim     = '231031050'
meet    = 'Praktikum 4'
prodi   = 'Sistem Informasi'
email   = 'muhyusufdzaky@gmail.com'
tanggal = '11 oktober 2023'
sp = 40

print()
#print(len(nama))
print('-'*sp)
print(nama.center(sp))
print(nim.center(sp))
print('\n'*2)
print(prodi.rjust(sp) + f'\r{meet}')
# print(prodi.rjus(sp))
print(email.rjust(sp) + f'\r{tanggal}')
print('-'*sp)

print('\n'*1)
paragraf = '''Halo selamat datang perkenalkan nama saya {} dengan nim {} dari prodi {} ini adalah file.'''

p = paragraf.format(nama,nim,prodi,meet)
print(p)

print()
print('#-------8+++++++')
x = 9
hasil = x>8
print(x,'hasilnya adalah',hasil )
print()
print('#+++++++8-------')
x = 9
hasil = x<8
print(x,'hasilnya adalah',hasil )
print()
print('----------4+++++++8----------')
x = 2
# cek1 = x>4 true
cek1 = x>4
# cek2 = x<8 true
cek2 = x<8
# hasil = cek1 and cek2 -->true
hasil = cek1 or cek2
# cetak hasil
print(x,'hasilnya adalah',hasil)
