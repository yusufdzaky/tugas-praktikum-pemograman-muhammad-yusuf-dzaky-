nim = [2,3,1,0,3,1,0,5,0]
print(nim)
#akses

print()
print('item ideks 0:',nim[0])
print('item ideks 3:',nim[3])
print('item ideks terakhiir:',nim[len(nim)-1])
#akses negatif

print()
print('item ideks terakhir:',nim[-1])
print('item ideks pertama:',nim[-len(nim)])
print('item ideks 3: [-6]',nim[-6])
print('item ideks 5: [-4]',nim[-4])
print('item ideks -7: [2]',nim[2])
print('item ideks 2: [-7]',nim[-7])
#akses indeks batas

print()
print(f'item ideks 1,2.....:,{nim[1:]}')
print(f'item ideks 3,4.....:,{nim[3:]}')
print(f'item ideks 0,1,2,3.....:,{nim[:4]}')
print(f'item ideks 0:,{nim[:1]}')
print(f'item ideks semuanya:,{nim[:]}')
print(f'item ideks [:8]:,{nim[:-1]}')
print(f'item ideks [:4]:,{nim[:-5]}')
#pengirisan

print()
print(f'item ideks 1,2:,{nim[1:3]}')
print(f'item ideks []:,{nim[3:3]}')
print(f'item ideks 2,3,4:,{nim[2:5]}')
print(f'item ideks [1:8],{nim[1:-1]}')
print(f'item ideks [2:7],{nim[2:-2]}')
#nested list

print()
kelas = [('Matkul',1),
         ('Matkul',2)]
print(kelas)
kelas.append(('Matkul',3))
print(kelas)
#tambahakan matkul 4 dan 5 dan sksnya

#mata kuliah 1: matkul 1 dengan 2 sks
#mata kuliah 2: matkul 2 dengan 3 sks
#mata kuliah 3: matkul 3 dengan 2 sks
#mata kuliah 4: matkul 4 dengan .. sks
#mata kuliah 5: matkul 5 dengan .. sks

data = [('frankel',2023,'aktif'),
        (76,98,89,97,99),
        [2,3,2,2,2],
        ('s-1reguler','sistem informasi B','ganjil')]

#nama mahasiswa : frankel
#inisial frankel : f
#nim frankel : 231031050
#program frankel : si-reguler sistem informasi B
#angkatan frankel : ganjil-2023
#nilai tertinggi frankel : 99
#nilai terendah frankel : 76
#rata-rata nilai frankel : 92.25
