a = True

while a:
    jawab = input('Apakah ingin Lanjutkan? (y/n)')
    if jawab == 'y':
        print('Selamat Datan Lagi!')
    elif jawab == 'n':
        print('Sampai Ketemu Lagi :D')
        a = False
    else:
        print('Jangan aneh-aneh deh :.)')
        a = True

    
