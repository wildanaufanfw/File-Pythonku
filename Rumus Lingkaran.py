import os

def clear():
    os.system('cls')

def garis():
    print('-'*45)

def EP():
    clear()
    garis()
    print('''
    MENCARI LUAS LINGKARAN
    ''')
    garis()
    print('')
    print('L = phi X r**2')
    print('')
    pilihan = str(input('Mencari Luas Lingkaran Menggunakan Jari-jari [r] atau Diameter [d] : '))
    if pilihan == 'r':
        print('')
        r = int(input('Masukkan Jari-jari Lingkaran (cm) : '))
        L = 22/7*(r**2)
        print(f'Luas Lingkaran Tersebut {L}cm persegi dengan jari-jari {r}cm')
    elif pilihan == 'd' :
        print('')
        d1 = int(input('Masukkan Diameter Lingkaran (cm) : '))
        d2 = d1/2
        L = 22/7*(d2**2)
        print(f'Luas Lingkaran Tersebut {L}cm persegi dengan diameter {d1}cm')
    print('')
    input('Tekan [Enter] Untuk Kembali Ke Menu ')
    menu()

def login():
    clear()
    garis()
    print('''
                SELAMAT DATANG 
        DI OPERASI MATEMATIKA SEDERHANA
                LUAS LINGKARAN
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
            LUAS LINGKARAN
    ''')
    garis()
    print('''       
1. Mencari Luas Lingkaran
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

