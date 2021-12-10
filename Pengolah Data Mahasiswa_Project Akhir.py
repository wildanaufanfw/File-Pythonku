import csv
import os

def clearData():
    os.system('cls') #mengclear terminal yang ada diatasnya

def garis():
    print('='*45) #membuat garis

def cover():
    garis() #memanggil garis
    print("""
    Selamat Datang di Data Mahasiswa TI
            Silahkan Login""",'\n')
    garis() #memanggil garis

def exitData():
    while True :
        clearData() #memanggil function clearData
        garis() #memanggil function garis
        print('             [Terimakasih Guys]') #menampilkan kalimat disamping
        garis() #memanggil function garis
        input() #inputan
        break #program berhenti
        
def tampilData():
    clearData() #memanggil function clearData
    garis() #memanggil function garis
    print('      Menu Menampilkan Data Mahasiswa') #menampilkan kalimat disamping
    garis() #memanggil function garis

    data = [] #list kosong

    with open('project.csv') as csv_file : #membuka file project.csv
        csv_reader = csv.reader(csv_file, delimiter=',') #membaca file dan disimpan dalam variabel csv_reader dan dipisahkan dengan tanda koma (,)
        for i in csv_reader : #menampilkan isi yang berada dalam file csv_reader
            data.append(i) #file yang sudah terbaca terdapat pada i kemudian ditambahkan kedalam list kosng (data)
        data.pop(0) #isi dengan indexs ke 0 diskip
        for q in data : #menampilkan isi yang berada dalam file data
            if len(data) == 0 : #jika isi data 0
                print('            [Data Masih Kosong]') #menampilkan kalimat
            else : #pengecualian
                # print(f'{q[0]}\t{q[1]}\t{q[2]}\t{q[3]}')
                print(f'Nama     : {q[0]}') #menampilkan Nama : isi dari indeks ke 0
                print(f'NIM      : {q[1]}') #menampilkan NIM : isi dari indeks ke 1
                print(f'Angkatan : {q[2]}') ##menampilkan Angkatan : isi dari indeks ke 2
                print(f'Asal     : {q[3]}') #menampilkan Asal : isi dari indeks ke 3
                print('') #enter / string kosong
    input('Tekan [enter] Untuk Melanjutkan ') #inputan tekan enter untuk melanjutkan
    clearData() #memanggil function clearData
    menu() #memanggil function menu

def cariData() :
    clearData() #memanggil function clearData
    print('='*45) #membuat garis
    print('       [Menu Mencari Data Mahasiswa]') #menampilkan kalimat disamping
    print('='*45) #membuat garis
    print('') #string kosong untuk memberikan jarak
    while True : #perulangan ketika benar
        f = open('project.csv') #membaca file csv kemudian disimpan dalam variabel f
        nama = input('Masukkan Nama Mahasiswa : ') #inputan nama yang disimpan dalam variabel nama
        isi = f.readlines() #membaca file yang terdapat dalam variabel f kemudian disimpan dalam variabel isi
        
        idx = 0 
        urut = 1
        for a in isi : #menampilkan file yang ada dalam variabel isi 
            x = a.split(',') #per indeks dipisahkan dengan tanda koma (,) disimpan dalam variabel x
            if x[0] == nama : #jika indeks ke 0 dari variabel x sama dengan inputan(nama) maka
                print('') #string kosong untuk jarak
                print('[Data Ditemukan]') #menampilkan kalimat disamping
                print('') #string kosong untuk jarak
                print('Nama     : '+x[0]) #menampilkan Nama : x indeks ke 0
                print('NIM      : '+x[1]) #menampilkan NIM : x indeks ke 1
                print('Angkatan : '+x[2]) #menampilkan Angkatan : x indeks ke 2
                print('Asal     : '+x[3]) #menampilkan Asal : x indeks ke 3
                print('') #string kosong untuk jarak
                urut += 1 
                continue
            idx += 1
            if idx == len(isi) : #jika isi sama dengan 0 maka
                print('') #string kosong untuk jarak
                print('[Data Tidak Ditemukan]') #menampilkan kalimat disamping
                print('') #string kosong untuk jarak
        inputan = input('tekan [y] untuk mencari kembali atau tekan [t] untuk kembali ke menu : ') #inputan yang disimpan dalam variabel inputan
        if inputan == 'y' : #jika inputan sama dengan y maka
            cariData() #memanggil function cariData
        elif inputan == 't' : #jika inputan sama dengan t maka
            print('') #strimg kosong untuk jarak
            input('tekan [enter] untuk kembali ke menu') #inputan
            f.close() #menutup file
            clearData() #memanggil function clearData
            menu() #memanggil function menu

def tambahData():
    clearData() #memanggil function clearData
    garis() #memanggil function garis
    print('       [Menu Menambahkan Data Mahasiswa]') #menampilkan kalimat disamping
    garis() #memanggil function garis
    print('') #membuat string kosong untuk jarak
    with open('project.csv',mode='a',newline='\n') as csv_file : #membuka file dengan mode append (menambahkan) dengan newline'\n' dan disimpan dalam csv_file
        field = ['Nama','NIM','Angkatan','Asal'] #string yang berisi Nama, NIM, Angkatan,Asal dan disimpan dalam variabel field
        writer = csv.DictWriter(csv_file, fieldnames=field) #menulis dan diesuaikan dengan variavel field

        nama = input('Masukkan Nama : ') #inputan nama
        nim = input('Masukkan NIM  : ') #inputan NIM
        angkatan = input('Angkatan      : ') #inputan angkatan
        asal = input('Asal Kota     : ') #inputan asal

        writer.writerow({'Nama' : nama, 'NIM' : nim, 'Angkatan' : angkatan, 'Asal' : asal}) #menulis teks dengan memanfaatkan inputan diatas
        print('') #string kosong untuk jarak
        print('Data Mahasiswa Berhasil Disimpan') #menampilkan kalimat disamping
        print('') #string kosong untuk jarak
    lagi = str(input('Apakah Ingin Menambahkan Data Lagi ? tekan ya [y] or tidak [t] : ')) #inputan dan disimpan dalam variabel lagi
    print('') #string kosong
    if lagi == 'y' : #jika inputan lagi sama dengan y
        tambahData() #memanggil function tambahData
    else: #pengecualian
        input('Tekan [enter] untuk melanjutkan ') #inputan
        clearData() #memanggil function clearData
        menu() #memanggil function menu

def hapusData():
    clearData() #memanggil function clearData
    garis() #memanggil function garis
    print('       [Menu Menghapus Data Mahasiswa]') #menampilkan kalimat disamping
    garis() #menampilkan garis
    hapus = input('Masukkan Nama Mahasiswa yang Ingin Dihapus : ') #inputan dan disimpan dalam variabel hapus
    f = open('project.csv') #membuka file project.csv
    isi = f.readlines() #membaca file kemudian disimpan dalam variabel isi
    idx = 0 
    for i in isi : #membuka file dalam isi disimpan dalam variabel i
        h = i.split(',')  #dipisah dengan tanda koma kemudian disimpan dalam variabel h
        if h[0] == hapus : #jika h indeks ke 0 sama dengan inputan hapus maka
            del(isi[idx]) #hapus data yang sesuai dengan inputan hapus dan isi
            print('') #string kosong untuk jarak
            print('Data Berhasil Dihapus') #menampilkan kalimat disamping
            print('') #string kosong untuk jarak
        idx += 1 
    f.close() #menutup file
    f = open('project.csv','w') #membuka file project.csv disimpan dalam variabel f
    isi = f.writelines(isi) #menulis 
    inputan = input('Apakah Ingin Menghapus Data Lagi ? tekan ya [y] or tidak [t] : ') #inputan disimpan dalam variabel inputan
    if inputan == 'y' : #jika inputan sama dengan y maka
        hapusData() #memanggil function hapusData
    else : #pengecualian
        print('') #string kosong untuk jarak
        input('Tekan [enter] untuk kembali ke menu') #menampilkan kalimat disamping
        f.close() #menutup file
        clearData() #memanggil function clearData
        menu() #memanggil function menu
        
def menu():
    clearData() #memanggil function clearData
    while True : #perulangan ketika benar
        print('='*40) #membuat garis
        print('         [Menu Data Mahasiswa]') #menampilkan kalimat disamping
        print('='*40) #membuat garis
        print(""" 
    Silahkan Pilih Salah Satu :

    1. Menampilkan Data Mahasiswa
    2. Mencari Data Mahasiswa
    3. Menambahkan Data Mahasiswa
    4. Menghapus Data Mahasiswa
    5. Exit""","\n") #menampilkan kalimat disamping
        inputan = int(input('Pilih Menu (angka) : ')) #inputan angka/integer disimpan dalam variabel inputan
        if inputan == 1 : #jika inputan sama dengan 1 maka
            tampilData() #memanggil function tampilData
        elif inputan == 2 : #jika inputan sama dengan 2 maka
            cariData() #memanggil function clearData
        elif inputan == 3 : #jika inputan sama dengan 3 maka
            tambahData() #memanggil function tambahData
        elif inputan == 4 : #jika inputan sama dengan 4 maka
            hapusData() #memanggil function hapusData
        elif inputan == 5 : #jika inputan sama dengan 5 maka
            exitData() #memanggil function exitData

def login():
    clearData() #memanggil function clearData
    cover() #memanggil function cover
    while True : #perulangan ketika benar

        usernameadmin = 'admin' #kata admin disimpan dalam variabel usernameadmin
        passwordadmin = 'admin' #kata admin disimpan dalam variabel passwordadmin

        print("") #string kosong untuk jarak
        username = input('Masukkan Username : ') #inputan untuk username disimpan dalam variabel username
        password = input('Masukkan Password : ') #inputan password disimpan dalam variabel password

        if username == usernameadmin : #jika inputan username sama dengan variabel usernameadmin maka
            if password == passwordadmin : #masuk kesini, kemudian jika inputan password sama dengan variabel passwordadmin maka
                print("") #string kosong untuk jarak
                print('Selamat Anda Telah Berhasil Login') #menampilkan kalimat disamping
                print('') #string kosong untuk jarak
                input('Tekan [enter] Untuk Melanjutkan') #inputan
                menu() #memanggil function menu
            else : #pengecualian
                print("") #string kosong untuk jarak
                print('='*51) #garis
                print('Username atau Password Salah Silahkan Login Kembali') #menampilkan kalimat disamping
                print('='*51) #garis
        else: #pengecualian
            print("") #string kosong untuk jarak
            print('='*51) #garis
            print('Username atau Password Salah Silahkan Login Kembali') #menampilkan kalimat disamping
            print('='*51) #garis
        
if __name__ == "__main__":
    login() #memanggil login
