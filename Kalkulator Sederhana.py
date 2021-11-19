import os
os.system('cls')
def garis():
    print('='*30)
while True :
    print('[Program Kalkulator Sederhana]')
    garis()
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Perkalian')
    print('4. Pembagian')
    print('5. Exit')
    w = int(input('Masukkan Pilihan : '))
    if w == 1 :
        garis()
        print('[Operasi Penjumlahan]')
        garis()
        a = int(input('Masukkan Bilangan Pertama : '))
        b = int(input('Masukkan Bilangan Kedua : '))
        c= a + b
        print(a, '+', b, '=', c)
        print('Hasil dari penjumlahan di atas adalah', c, 'silahkan menghitung kembali')
    elif w == 2 :
        garis()
        print('[Operasi Pengurangan]')
        garis()
        a = int(input('Masukkan Bilangan Pertama : '))
        b = int(input('Masukkan Bilangan Kedua : '))
        c = a - b
        print(a, '-', b, '=', c)
        print('Hasil dari pengurangan di atas adalah', c, 'silahkan menghitung kembali')
    elif w == 3 :
        garis()
        print('[Operasi Perkalian]')
        garis()
        a = int(input('Masukkan Bilangan Pertama : '))
        b = int(input('Masukkan Bilangan Kedua : '))
        c = a * b
        print(a, 'x', b, '=', c)
        print('Hasil dari perkalian di atas adalah', c, 'silahkan menghitung kembali')
    elif w == 4 :
        garis()
        print('[Operasi Pembagian]')
        garis()
        a = int(input('Masukkan Bilangan Pertama : '))
        b = int(input('Masukkan Bilangan Kedua : '))
        c = a / b
        print(a, '/', b, '=', c)
        print('Hasil dari pembagian di atas adalah', c, 'silahkan menghitung kembali')
    else :
        break
print('Thank You Guys')