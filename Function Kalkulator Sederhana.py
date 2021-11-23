import os
os.system ('cls')

def garis():
    print('='*25)

def tambah(a, b) :
    tambah = int(a) + int(b)
    return tambah

def kurang(a, b) :
    kurang = int(a) - int(b)
    return kurang

def kali(a, b) :
    kali = int(a) * int(b)
    return kali

def bagi(a, b) :
    bagi = int(a) / int(b)
    return bagi

while True :
    print('[Operasi Perhitungan Matematika]')
    garis()
    a = int(input('Masukkan Angka 1 : '))
    b = int(input('Masukkan Angka 2 : '))
    print('[Silahkan Pilih Operasi Dibawah Ini]')
    print('1. Operasi Penjumlahan\n2. Operasi Pengurangan\n3. Operasi Perkalian\n4. Operasi Pembagian\n5. Exit ')
    garis()
    pilihan = int(input('Pilih Operasi Perhitungan : '))
    if pilihan == 1 :
        print('Operasi Penjumlahan')
        garis()
        print('Hasil Penjumlahannya Adalah', tambah(a, b))
        garis()
    elif pilihan == 2 :
        print('Operasi Pengurangan')
        garis()
        print('Hasil Pengurangannya Adalah', kurang(a, b))
        garis()
    elif pilihan == 3 :
        print('Operasi Penjumlahan')
        garis()
        print('Hasil Perkaliannya Adalah', kali(a, b))
        garis()
    elif pilihan == 4 :
        print('Operasi Penjumlahan')
        garis()
        print('Hasil Pembagiannnya Adalah', bagi(a, b))
        garis()
    elif pilihan == 5 :
        print('Berhenti')
        garis()
        break
    else :
        print('Eror')
        garis()
