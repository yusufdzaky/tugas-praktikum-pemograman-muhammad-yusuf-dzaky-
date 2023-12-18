import os
def judul():
    print('program menghitung volume dan luas permukaan balok'.center(45))
    print('bangun ruang balok'.center(45))
    print()

def inputan():
    panjang = float(input('masukan panjang :'))
    lebar   = float(input('masukkan lebar  :'))
    tinggi  = float(input('masukkan tinggi :'))
    return panjang,lebar,tinggi

def hitung(panjang,lebar,tinggi):
    vol = panjang*lebar*tinggi
    luas_surf = 2*(panjang*lebar + panjang*tinggi + lebar*tinggi)
    luas_non_tutup = luas_surf - panjang*lebar
    return vol,luas_surf,luas_non_tutup

def tampilan(pesan,nilai):
    print(f'nilai {pesan} : {nilai}')


def pilihan():
    pilih = input('apakah lanjutkan?[y/n]')
    if pilih == 'y':
        a = True
    else:
        a = False
        print('terima kasih!')
    return a

def main():
    os.system('clear')    
    judul()#judul
    panjang,lebar,tinggi = inputan()#inputan
    vol,luas_surf,luas_non_tutup = hitung(panjang,lebar,tinggi)#inputan
    #tampilan
    tampilan('volume',vol)
    tampilan('luas permukaan',luas_surf)
    tampilan('luas permukaan tanpa tutup',luas_non_tutup)
    a = pilihan()#pilihan
    return a

a = True
while a:
   a = main()
    
    
