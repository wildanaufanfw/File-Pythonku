import os

def clearData():
    os.system('cls')

def garis():
    print('='*29)

def cover():
    clearData()
    garis()
    print('''
      SELAMAT DATANG Di   
     OPERASI PERHITUNGAN  
    GERAK LURUS BERATURAN 
    ''')
    garis()
    input("Tekan [Enter] Untuk Melanjutkan")
    loginData()

def loginData():
    clearData()
    garis()
    print(''' 
     OPERASI PERHITUNGAN  
    GERAK LURUS BERATURAN 
    ''')
    garis()
    print('')
    username = input('Masukkan Username : ')
    password = input('Masukkan Password : ')
    print('')
    if username == "admin" :
        if password == "admin" :
            clearData()
            print('='*35)
            print(' Selamat Anda Telah Berhasil Login')
            print('='*35)
            print('')
            input('Tekan [Enter] Untuk Masuk ke Menu')
            menuData()
        else:
            input('Username atau Password Salah, Silahkan login Kembali')
            loginData()
    else:
        input('Username atau Password Salah Silahkan Login Kembali')
        loginData()
     
def menuData():
    clearData()
    garis()
    print('''
    MENU OPERASI PERHITUNGAN
    GERAK LURUS BERATURAN
    ''')
    garis()
    input('Tekan [enter] Untuk Melanjutkan')
    clearData()
    garis()
    print('''
1. Menghitungan Kecepatan Suatu Benda
2. Menghitung Jarak Suatu Benda
3. Menghitung Waktu
    ''')
    garis()
    inputan = int(input('Pilih Menu : '))
    if inputan == 1 :
        kecepatanBenda()
    elif inputan == 2 :
        jarakBenda()        
    elif inputan== 3 :
        waktuBenda()
    else :
        input("Operasi Tidak Ada, Silahkan Pilih Menu yang Sesuai")
        menuData()

def kecepatanBenda():
    clearData()
    garis()
    print('[Menu Mencari Kecepatan Benda]')
    garis()
    print('')
    s = int(input('Masukkan Jarak (m) : '))
    t = int(input('Masukkan Selang Waktu (s) : '))
    v = s/t
    print('')
    print(f'Kecepatan Benda Tersebut adalah {v} m/s dengan jarak {s} meter dan selang waktu {t} sekon')
    print('')
    pilihan = str(input('Ingin Menghitung Kembali? Tekan [y] untuk ya atau [t] untuk tidak: '))
    if pilihan == "y":
        menuData()
    elif pilihan == 't':
        exitData()
    else :
        input('Program Eror, Tekan [Enter] Untuk Kembali Ke Menu ')
        menuData()

def jarakBenda():
    clearData()
    garis()
    print('[Menu Mencari Jarak Suatu Benda]')
    garis()
    print('')
    v = int(input('Masukkan Kecepatan Suatu Benda (m/s) : '))
    t = int(input('Masukkan Selang Waktu (s) : '))
    s = v*t
    print('')
    print(f'Jarak yang ditempuh benda tersebut {s} meter dengan kecepatan {v} m/s dan selang waktu {t} sekon ')
    print('')
    pilihan = str(input('Ingin Menghitung Kembali? Tekan [y] untuk ya atau [t] untuk tidak: '))
    if pilihan == 'y':
        menuData()
    elif pilihan == 't':
        exitData()
    else:
        input('Program Eror, Tekan [Enter] Untuk Kembali Ke Menu ')
        menuData()

def waktuBenda():
    clearData()
    garis()
    print('[Menu Mencari Selang Waktu]')
    garis()    
    print('')
    s = int(input('Masukkan Jarak (m) : '))
    v = int(input('Masukkan Kecepatan Suatu Benda (m/s) : '))
    print('')
    t = s/v
    print(f'Waktu yang ditempuh benda tersebut bergerak selama {t} sekon dengan kecepatan {v} m/s dan jarak {s} meter')
    print('')
    pilihan = str(input('Ingin Menghitung Kembali? Tekan [y] untuk ya atau [t] untuk tidak: '))
    if pilihan == 'y':
        menuData()
    elif pilihan == 't':
        exitData()
    else:
        input('Program Eror, Tekan [Enter] Untuk Kembali Ke Menu ')
        menuData()

def exitData():
    clearData()
    garis()
    print('     [Terimakasih Guys')
    garis()

cover()