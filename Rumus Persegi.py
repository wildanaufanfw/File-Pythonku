import os

def clear():
    os.system('cls')

def garis():
    print('-'*45)

def EP():
    clear()
    garis()
    print('''
    MENCARI LUAS SUATU PERSEGI
    ''')
    garis()
    print('')
    print('L = Sisi X Sisi')
    print('')
    s = int(input('Masukkan Panjang Sisi Persegi (cm) : '))
    l = s*s
    print('')
    print(f'Luas Persegi Tersebut {l}cm persegi dengan sisi {s}cm')
    print('')
    input('Tekan [Enter] Untuk Kembali Ke Menu ')
    menu()

def login():
    clear()
    garis()
    print('''
                SELAMAT DATANG 
        DI OPERASI MATEMATIKA SEDERHANA
                 LUAS PERSEGI
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
        MENU OPERASI MATEMATIKA
            LUAS PERSEGI
    ''')
    garis()
    print('''       
1. Mencari Luas Persegi
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

