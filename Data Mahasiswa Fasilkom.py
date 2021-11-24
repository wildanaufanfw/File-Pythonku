#PROJECT AKHIR
from _typeshed import FileDescriptor

def garis() :
    print('='*30)
#================================================================#
def menu():
    import os
    os.system('cls')
    garis()
    print('[Data Mahasiswa Fasilkom Universitas Jember Tahun 2021]')
    garis()
    print('\n1. Melihat Data Mahasiswa\n2. Menambahkan Data Mahasiswa\n3. Mencari Data Mahasiswa\n4. Mengubah Data Mahasiswa\n5. Menghapus Data Mahasiswa\n6. Exit')
    garis()
    no = int(input('Masukkan Pilihan yang Anda Inginkan : '))
#================================================================#
def pilih_menu(a) :
    if a == 1 :
        lihatdata()
    elif a == 2 :
        tambahdata()
    elif a == 3 :
        caridata()
    elif a == 4 :
        ubahdata()
    elif a == 5 :
        hapusdata()
    elif a == 6 :
        exitdata()
#================================================================#
def lihatdata() :
    garis()
    print('Anda Berada Pada Menu Menampilkan Data Mahasiswa')
    garis()
    f = open('database.txt')
    isi = f.readlines()
    isi.sort()
    if len(isi) == 0 :
        print('Data Mahasiswa Masih Kosong')
    else :
        i = 0
        for q in isi :
            pisah = q.split(',')
            print('Data', str(i))
            print('Nama : '+pisah[0])
            print('Prodi : '+pisah[1])
            print('Asal : '+pisah[2])
        i += 1
    print('Tekan Enter Untuk Melanjutkan')
    FileDescriptor.close()
    input()
    menu()
#================================================================#
def tambahdata() :
    garis()
    print('Anda Berada Pada Menu Menambahkan Data Mahasiswa')
    garis()
    print('Masukkan Data')
    nama = str(input('Masukkan Nama Mahasiswa : '))
    prodi = str(input('Masukkan Program Studi Mahasiswa : '))
    asal = str(input('Asal Daerah Mahasiswa : '))
    w = open('database.txt', 'a')
    w.writelines([nama+','+prodi+','+asal+'\n'])
    print('Tekan Enter Untuk Melanjutkan')
    w.close()
    input()
    menu()
#================================================================#
def caridata() :
    garis()
    print('Anda Berada Pada Menu Mencari Data Mahasiswa')
    garis()
    f = open('database.txt')
    g = input('Masukkan Nama Mahasiswa yang Ingin Anda Cari : ')
    isi = f.readlines()

    apa = 0
    urut = 1
    for a in isi :
        print(a)
        c = a.split(',')
        if c[0] == g :
            print('Data Mahasiswa Ditemukan, Data Ke : ', urut)
            garis()
            print('Nama : '+c[0])
            print('Prodi : '+c[1])
            print('Asal : '+c[2])
            urut += 1
            continue
            break
        apa += 1
        if apa == len(isi) :
            print('Data Tidak Ditemukan')
    print('Tekan Enter Untuk Melanjutkan')
    f.close()
    input()
    menu()
#================================================================#
def ubahdata() :
    garis()
    print('Anda Berada Pada Menu Mengubah Data Mahasiswa')
    garis()
    namabaru =input('Masukkan Data Nama Mahasiswa yang Ingin Diubah : ')
    print('- Masukkan Data Baru -')
    garis()
    nb = input('Masukkan Nama Mahasiswa : ')
    pb = input('Masukkan Program Studi Mahasiswa : ')
    ab = input('Masukkan Asal Mahasiswa : ')

    f = open('database.txt')
    isi = f.readlines()
    k = 0
    for i in isi :
        data = i.split(',')
        if data[0] == namabaru :
            data[0] = nb
            data[1] = pb
            data [2] = ab
            datax = ','.join(data)
            isi(k) = datax
            break
        k += 1
    f.close()
    f = open('database.txt','w')
    isi = f.writelines(isi)
    print('Tekan Enter Untuk Melanjutkan')
    f.close()
    input()
    menu()
#================================================================#
def hapusdata() :
    garis()
    print('Anda Berada Pada Menu Menghapus Data Mahasiswa')
    garis()
    hapus = input('Masukkan Data Nama Mahasiswa yang Ingin DIhapus : ')
    f = open('database.txt')
    isi = f.readlines()
    isi.sort()
    a = 0
    for i in isi :
        g = i.split(',')
        if g[0] == hapus :
            del(isi(a))
            print('Data Mahasiswa Berhasil Dihapus')
        a += 1
    f.close()
    f = open('database.txt', 'w')
    isi = f.writelines(isi)
    print('Tekan Enter Untuk Melanjutkan')
    f.close()
    input()
    menu()
#================================================================#
def exitdata() :
    print('Tekan Enter Untuk Melanjutkan')


