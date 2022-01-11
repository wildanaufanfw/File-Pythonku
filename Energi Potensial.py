import os

def clear():
    os.system('cls')

def garis():
    print('-'*45)

def EP():
    clear()
    garis()
    print('''
    MENCARI ENERGI POTENSIAL SUATU BENDA
    ''')
    garis()
    print('')
    print('EP = m.g.h')
    print('')
    m = int(input('Masukkan Massa Suatu Benda : '))
    g = int(input('Masukkan Nilai Percepatan Gravitasi : '))
    h = int(input('Masukkan Ketinggian Suatu Benda : '))
    ep = m*g*h
    print('')
    print(f'Nilai Energi Potensial Benda Tersebut {ep}Joule dengan Massa {m}kg, Percepatan Gravitasi {g}m/s2, dan Ketinggian {h}m')
    print('')
    input('Tekan [Enter] Untuk Kembali Ke Menu ')
    menu()

def login():
    clear()
    garis()
    print('''
                SELAMAT DATANG 
          DI OPERASI FISIKA SEDERHANA
               ENERGI POTENSIAL
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
                menu()
            else : 
                print('')
                print('Password Yang Anda Masukkan Salah, Silahkan Login Kembali')
                print('')
                input('Tekan [Enter] Untuk Login Kembali')
                clear()
                login()
        else :
            print('')
            print('Username Yang Anda Masukkan Salah, Silahkan Login Kembali')
            print('')
            input('Tekan [Enter] Untuk Login Kembali')
            clear()
            login()

def menu():
    clear()
    garis()
    print('''
        MENU OPERASI FISIKA
          ENERGI POTENSIAL
    ''')
    garis()
    print('''       
1. Mencari Energi Potensial
2. Exit
    ''')
    pilih = int(input('Silahkan Pilih Salah Satu Menu Di Atas : '))
    if pilih == 1 :
        EP()
    elif pilih == 2 :
        exit()
    else :
        print('')
        input('Pilihan Menu Tidak Ada, Tekan [Enter] Untuk Memilih Kembali ')
        menu()

def exit():
    clear()
    garis()
    print('                TERIMA KASIH')
    garis()
    input()

login()

