import os

def clearData():
    os.system('cls')

def garis():
    print('='*45)

def login():
    garis()
    print('''
                SELAMAT DATANG 
            DI OPERASI MATEMATIKA
                  PYTHAGORAS
    ''')
    garis()
    while True:
        user = 'admin'
        pas = 'admin'
        
        username = input('Masukkan Username : ')
        password = input('Masukkan Password : ')
        
        if username == user :
            if password == pas :
                garis()
                input('Selamat Anda Telah Berhasil Login, Tekan [Enter] Untuk Melanjutkan ')
                menuData()
            else : 
                print('')
                print('Password Yang Anda Masukkan Salah, Silahkan Login Kembali')
                print('')
                input('Tekan [Enter] Untuk Login Kembali')
                clearData()
                login()
        else :
            print('')
            print('Username Yang Anda Masukkan Salah, Silahkan Login Kembali')
            print('')
            input('Tekan [Enter] Untuk Login Kembali')
            clearData()
            login()
        
def menuData():
    clearData()
    garis()
    print('''
        MENU OPERASI MATEMATIKA
              PYTHAGORAS
    ''')
    garis()
    print('''       
1. Mencari Sisi Miring
2. Mencari Sisi Tegak
3. Exit
    ''')
    pilih = int(input('Silahkan Pilih Salah Satu Menu Di Atas : '))
    if pilih == 1 :
        sisiMiring()
    elif pilih == 2 :
        sisiTegak()
    elif pilih == 3 :
        exitData()
    else :
        print('')
        input('Pilihan Menu Tidak Ada, Tekan [Enter] Untuk Memilih Kembali ')
        menuData()

def sisiMiring():
    clearData()
    garis()
    print('''
          MENU MENCARI SISI MIRING
    ''')
    garis()
    print('')
    sisitegak1 = int(input('Masukkan Nilai Sisi Tegak 1 : '))
    print('')
    sisitegak2 = int(input('Masukkan Nilai Sisi Tegak 2 : '))
    print('')
    sisimiring = (sisitegak1*sisitegak1 + sisitegak2*sisitegak2)**0.5
    print(f'Sisi Miring Dari Segitiga Tersebut Adalah {sisimiring} dengan Sisi Tegak1 = {sisitegak1} dan Sisi Tegak2 = {sisitegak2}')
    print('')
    input('Tekan [enter] Untuk Melanjutkan')
    print('')
    pilihan = input('Tekan [y] jika ingin menghitung kembali atau [t] untuk exit : ')
    if pilihan == 'y' :
        menuData()
    elif pilihan == 't' :
        exitData()

def sisiTegak():
    clearData()
    garis()
    print('''
          MENU MENCARI SISI TEGAK
    ''')
    garis()
    print('')
    sisimiring1 = int(input('Masukkan Nilai Sisi Miring  : '))
    print('')
    sisitegak1 = int(input('Masukkan Nilai Sisi Tegak  : '))
    print('')
    sisitegak = (sisimiring1*sisimiring1 - sisitegak1*sisitegak1)**0.5
    print(f'Sisi Tegak Dari Segitiga Tersebut Adalah {sisitegak} dengan Sisi Tegak = {sisitegak1} dan Sisi Miring = {sisimiring1}')
    print('')
    input('Tekan [enter] Untuk Melanjutkan')
    print('')
    pilihan = input('Tekan [y] jika ingin menghitung kembali atau [t] untuk exit : ')
    if pilihan == 'y' :
        menuData()
    elif pilihan == 't' :
        exitData()

def exitData():
    clearData()
    garis()
    print('                 TERIMAKASIH')
    garis()
    input()

login()