import pandas as pd
import os
from tabulate import tabulate
import csv
import time
import datetime
import random

fon = '''
░▒▓███████▓▒░ ░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░    ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     
░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     
░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░                                                                                              
'''

def utama():
    while True:
        os.system('cls')
        print(fon)
        print("\nPilih jenis akun untuk login:")
        print("[1] Admin")
        print("[2] User")
        print("-" * 40)
        try:
            akunUser = int(input("Masuk sebagai [1/2]: "))           
            if akunUser == 1:
                login_admin()
            elif akunUser == 2:
                login_user2()
            else:
                print("Input tidak sesuai, silakan coba lagi.")
                time.sleep(2)
                continue
        except ValueError:
            print('Pilihan harus berupa angka dan tidak boleh kosong')
            time.sleep(2)

def login_admin():
    os.system('cls')
    print('='*40)
    print('LOGIN ADMIN'.center(40))  
    print('='*40)
    inputUser = input("Masukkan username Anda: ").rstrip().lower()
    inputPass = input('Masukkan password Anda: ').rstrip().lower()
    data = pd.read_csv('csv/dataAdmin.csv')
    user = data[(data['Username'] == inputUser) & (data['Password'] == inputPass)]
    if not user.empty:
        print("\nSelamat datang, Anda berhasil login sebagai Admin...")
        time.sleep(2)
        halaman_admin()
    else:
        print("Username atau password salah, silakan coba lagi.")
        time.sleep(2)

def login_user2():
    os.system('cls')
    print('='*40)
    print('[1] Login User')
    print('[2] Daftar User')
    print('='*40)
    try:
        pilihan = int(input('Masukkan pilihan : '))
        if pilihan == 1:
            login_user()
        elif pilihan == 2:
            register()
        else:
            print('Pilihan tidak tersedia')
    except ValueError:
        print('Pilihan harus berupa angka & tidak boleh kosong')

def login_user():
    os.system('cls')
    global userInputh
    global userPassh    
    print("=" *40)
    print(" LOGIN USER ".center(40))
    print("=" *40)
    userInputh = input("Masukkan username: ").rstrip().lower()
    userPassh = input("Masukkan password: ").rstrip().lower()
    print('='*40)
    data = pd.read_csv('csv/dataUser.csv')
    user = data[(data['Username'] == userInputh) & (data['Password'] == userPassh)]
    if not user.empty: 
        print("Selamat datang, Anda berhasil login!")
        time.sleep(2)
        halaman_user()
    else:
        os.system('cls')
        print(f'Pengguna dengan username [{userInputh}], Password [{userPassh}] tidak ditemukan.')
        print("Ingin mendaftar atau mencoba lagi?")
        print('-'*40)
        print("[Enter] untuk mencoba lagi")
        print("[y] untuk mendaftar")           
        jawaban = input("Masukkan pilihan >>> ").strip().lower()
        if jawaban == 'y':
            register()
        elif jawaban == '':
            login_user()
        else:
            print("\nInput tidak sesuai, silakan coba lagi.")
            time.sleep(2)

def register():
    os.system('cls')
    print("=" * 40)
    print(" REGISTRASI AKUN ".center(40))
    print("=" * 40)
    username = input("Masukkan username: ").lower()
    password = input("Masukkan password: ").lower()
    if username == '' or password == '':
        print('Tidak boleh ada yang kosong!')
        time.sleep(2)
        register()
    data = pd.read_csv('csv/dataUser.csv')
    if username in data['Username'].values:
        print("Username sudah digunakan, silakan coba lagi.")
        time.sleep(2)
        register()
    else:
        saldo = 0
        hari = datetime.date.today()
        with open('csv/dataUser.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password, saldo, hari])
            print("\nSelamat, Anda telah berhasil terdaftar!")
            time.sleep(2)
        login_user()

def halaman_user():
    os.system('cls')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^ 	     	   SELAMAT DATANG           ^^^  ||')
    print('||--------- Apa yang ingin anda lakukan?---------||')
    print('||                1. Lihat Profil                ||')
    print('||                2. Pemesanan                   ||')
    print('||                3. Cek Harga                   ||')
    print('||                4. Histori Pemesanan           ||')
    print('||                5. Keluhan                     ||')
    print('||                6. Log Out                     ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    try:
        pilihan = int(input("Masukan Pilihan Anda : "))
        if pilihan == 1:
            lihat_profil()
        elif pilihan == 2:
            pemesanan()
        elif pilihan == 3:
            cek_harga()
        elif pilihan == 4:
            histori_pemesanan()
        elif pilihan == 5:
            keluhan()
        elif pilihan == 6:
            utama()
        else:
            print('Pilihan tidak ada, silakan coba lagi')
            time.sleep(2)
            halaman_user()
    except ValueError:
        print('Harus angka & tidak boleh kosong')
        time.sleep(2)
        halaman_user()

def lihat_profil():
    os.system('cls')
    print('='*40)
    print('LIHAT PROFIL'.center(40))
    print('='*40)
    data = pd.read_csv('csv/dataUser.csv')
    cek = data.loc[data['Username'] == userInputh]
    saldo = cek['Saldo'].values[0]
    tanggal = cek['Tanggal Daftar'].values[0]
    pw = cek['Password'].values[0]
    print('BERIKUT INFORMASI ANDA')
    print(f'Username anda adalah = {userInputh}')
    print(f'Password anda adalah = {pw}')
    print(f'Sisa saldo anda adalah = Rp.{saldo}')
    print(f'Akun anda dibuat pada tanggal {tanggal}')
    print('='*40)
    input1 = input('Apakah Anda ingin mengubah password? (y/n) ')
    if input1 == 'y':
        a = input('Masukkan Password baru :')
        b = input('Masukkan Password baru lagi :')
        if a == b:
            data.loc[data['Username'] == userInputh, 'Password'] = b
            os.system('cls')
            print('Sedang mengubah password anda...')
            time.sleep(2)
            data.to_csv('csv/dataUser.csv', index=False)
            print('Password berhasil diubah')
            time.sleep(2)
            halaman_user()
        else:
            print('Password tidak sama')
            time.sleep(2)
            halaman_user()
    elif input1 == 'n':
        halaman_user()
    else:
        print('Mohon pilih pilihan yang valid')
        time.sleep(2)
    halaman_user()

def pemesanan():
    os.system('cls')
    global kode
    data = pd.read_csv('csv/dataMitra.csv') 
    data.index = range(1, len(data)+1)
    print(tabulate(data, headers='keys',tablefmt='grid'))
    kode = input('Masukkan kode toko yang ingin dibeli : ').upper()
    if kode in data['kode'].values:
        print('Toko tersedia, mengarahkan ke halaman pembelian...')
        time.sleep(2)
        pemesanan_toko()
    else:
        print('Toko tidak ditemukan...')
        time.sleep(2)
        pemesanan()

def pemesanan_toko():
    os.system('cls')
    data2 = pd.read_csv('csv/dataUser.csv')
    cek = data2.loc[data2['Username'] == userInputh]
    saldo = cek['Saldo'].values[0]
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^ 	     	   SELAMAT DATANG           ^^^  ||')
    print('||--------- Apa yang ingin anda lakukan?---------||')
    print('||                1. Pesan                       ||')
    print('||                2. Isi Saldo                   ||')
    print('||                3. Kembali                     ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print(f'Saldo anda tersisa : {saldo}')
    try:
        inputanUser = int(input('Masukkan Pilihan : '))
        if inputanUser == 1:
            pesan()
        elif inputanUser == 2:
            isi_saldo()
        elif inputanUser == 3:
            halaman_user()
        else:
            print('Pilihan tidak tersedia...')
            time.sleep(2)
            pemesanan_toko()
    except ValueError:
        print('Pilihan tidak valid...')
        time.sleep(2)
        pemesanan_toko()

def pesan():
    os.system('cls')
    data = pd.read_csv(f'csv/toko/{kode}.csv')
    dataUser = pd.read_csv('csv/dataUser.csv')
    data.index = range(1,len(data)+1)
    print(tabulate(data,headers='keys',tablefmt='grid'))
    kodebrg = input('Masukkan kode barang yang akan dibeli : ').upper()
    if kodebrg in data['KodeBrg'].values:
        cek = data[data['KodeBrg'] == kodebrg]
        cekTrue = cek['Stok'].values[0]
        cek2 = dataUser[dataUser['Username'] == userInputh]
        cekSaldo = cek2['Saldo'].values[0]
        while True:
            try:
                a = int(input('Masukkan jumlah yang ingin dibeli : '))
                break
            except ValueError:
                print('Jumlah tidak valid...')
        if cekTrue < 1:
            print('Barang tidak memiliki stok, semua akan dimulai ulang...')
            time.sleep(2)
            pesan()
        elif a == 0:
            print('Minimal pembelian adalah 1')
            time.sleep(2)
            pesan()
        elif cekTrue < a:
            print(f'Stok tidak mencukupi untuk dibeli, sisa barang {cekTrue}')
            time.sleep(2)
            pesan()
        elif cekSaldo < a * cek['Harga'].values[0]:
            print('Saldo tidak mecukupi untuk Membeli...')
            time.sleep(2)
            pesan()
        else:
            cek1 = data[data['KodeBrg'] == kodebrg]
            cekHarga = cek1['Harga'].values[0]
            cekNama = data['NamaBrg'].values[0]
            total = cekHarga * a
            hari = datetime.date.today()
            randomAngka = random.randint(1,999)
            data.loc[data['KodeBrg'] == kodebrg, 'Stok'] -= a
            dataUser.loc[dataUser['Username'] == userInputh, 'Saldo'] -= (total)
            data.to_csv(f'csv/toko/{kode}.csv',index=False)
            dataUser.to_csv('csv/dataUser.csv',index=False)
            if not os.path.exists(f'csv/histori/{userInputh}.csv'):
                with open(f'csv/histori/{userInputh}.csv','w',newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['kode','NamaBrg','Jumlah','Harga','Tanggal'])
                with open(f'csv/histori/{userInputh}.csv','a',newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([kodebrg,cekNama,a,cekHarga * a,hari])
            elif os.path.exists(f'csv/histori/{userInputh}.csv'):
                statusKirim = 'Belum dikirim'
                with open(f'csv/histori/{userInputh}.csv','a',newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([kodebrg,cekNama,a,total,hari])
                with open('csv/dataPengiriman.csv', 'a', newline='') as kirim:
                    writer = csv.writer(kirim)
                    writer.writerow([randomAngka,userInputh,hari,total,statusKirim])
            print('Anda berhasil membeli barang...')
            time.sleep(2)
    else:
        print('Kode tidak ditemukan...')
        time.sleep(2)
        pesan()
    input('ketik ENTER untuk kembali >>> ')
    pemesanan_toko()

def isi_saldo():
    os.system('cls')
    data = pd.read_csv('csv/dataUser.csv')
    print('='*40)
    print('ISI SALDO'.center(40))
    print('='*40)
    isiSaldo = int(input('Masukkan jumlah saldo yang ingin diisi : '))
    if isiSaldo < 5000:
        print('Minimal saldo yang dapat diisi adalah 5000')
        time.sleep(2)
        isi_saldo()
    os.system('cls')
    print('''Ingin membayar lewat apa :
1. Ewallet
2. Transfer Bank''')
    pilih = int(input('Masukkan pilihan : '))
    if pilih == 1:
        os.system('cls')
        print('''Pilih Metode pembayaran :
1. Dana
2. Gopay
3. Ovo
4. Shopeepay''')
        a = int(input('Masukkan pilihan : '))
        if a == 1 or a == 2 or a == 3 or a == 4:
            os.system('cls')
            print('Sedang memproses...')
            time.sleep(2)
            data.loc[data['Username'] == userInputh, 'Saldo'] += isiSaldo
            data.to_csv('csv/dataUser.csv',index=False)
            print('Selamat saldo anda telah terisi...')
            time.sleep(2)
            pemesanan_toko()
        else:
            print('Metode pembayaran tidak tersedia...')
            time.sleep(2)
            halaman_user()
    elif pilih == 2:
        os.system('cls')
        print('''Pilih Bank :
1. BRI
2. BNI
3. Seabank
4. Mandiri
5. BCA
6. BSI''')
        a = int(input('Masukkan pilihan : '))
        if a == 1 or a == 2 or a == 3 or a == 4 or a == 5 or a == 6:
            os.system('cls')
            print('Sedang memproses...')
            time.sleep(2)
            data.loc[data['Username'] == userInputh, 'Saldo'] += isiSaldo
            data.to_csv('csv/dataUser.csv',index=False)
            print('Selamat saldo anda telah terisi...')
            time.sleep(2)
            pemesanan_toko()
        else:
            print('Bank tidak tersedia...')
            time.sleep(2)
            halaman_user()
    else:
        print('Pilihan tidak tersedia...')
        time.sleep(2)
        halaman_user()

def cek_harga():
    os.system('cls')
    data = pd.read_csv('csv/dataMitra.csv')
    data.index = range(1, len(data)+1) 
    print(tabulate(data,headers='keys',tablefmt='grid'))
    print('\nKetik "EXIT" untuk kembali')
    a = input('Masukkan kode toko yang ingin di cek : ').upper()
    if a in data['kode'].values:
        os.system('cls')
        dataMitra = pd.read_csv(f'csv/toko/{a}.csv')
        dataMitra.index = range(1,len(dataMitra)+1)
        print(tabulate(dataMitra,headers='keys',tablefmt='grid'))
        input('Ketik ENTER untuk kembali >>> ')
        halaman_user()
    elif a == 'EXIT':
        halaman_user()
    else:
        print('Kode tidak ditemukan')
        time.sleep(2)
        cek_harga()

def histori_pemesanan():
    os.system('cls')
    data = pd.read_csv(f'csv/histori/{userInputh}.csv')
    data.index = range(1, len(data)+1)
    print(tabulate(data,headers='keys',tablefmt='grid'))
    total = data['Harga'].values.sum()
    print(f'Total pembelian kamu adalah {total}')
    input('Tekan ENTER untuk kembali >>> ')
    halaman_user()
    

def keluhan():
    os.system('cls')
    hari = datetime.date.today()
    print("="*50)
    print('FORMULIR KELUHAN'.center(50))
    print("="*50)
    keluhUser = input('Masukkan keluhan anda : ')
    if keluhUser == '':
        print('Mohon isi formulir keluhan')
        time.sleep(2)
        keluhan()
    data = pd.read_csv('csv/keluhanUser.csv')
    with open('csv/keluhanUser.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([userInputh,keluhUser,hari])
        data.to_csv('csv/keluhanUser.csv', index=False)
        print('Keluhan telah disampaikan')
        input('tekan enter untuk kembali')
    halaman_user()
    
def halaman_admin():
    os.system('cls')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^ 	     	   SELAMAT DATANG            ^^^ ||')
    print('||--------- Apa yang ingin anda lakukan?---------||')
    print('||                1. Kelola Mitra                ||')
    print('||                2. Kelola Barang               ||')
    print('||                3. Kelola kendaraan            ||')
    print('||                4. Atur Pengiriman             ||')
    print('||                5. Kelola Pengguna             ||')
    print('||                6. Laporan                     ||')
    print('||                7. Log Out                     ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    try:
        pilihan = int(input("Masukan Pilihan Anda : "))
        if pilihan == 1:
            kelola_mitra()
        elif pilihan == 2:
            kelola_barang()
        elif pilihan == 3:
            kelola_kendaraan()
        elif pilihan == 4:
            atur_pengiriman()
        elif pilihan == 5:
            kelola_user()
        elif pilihan == 6:
            laporan_admin()
        elif pilihan == 7:
            utama()
        else:
            print('Pilihan tidak ada')
            time.sleep(2)
            halaman_admin()
    except ValueError:
        print('Pilihan harus angka & tidak boleh kosong!')
        time.sleep(2)
        halaman_admin()

def atur_pengiriman():
    while True:
        os.system('cls')
        data = pd.read_csv('csv/dataPengiriman.csv')
        data['kode'] = data['kode'].astype(int)
        data.index = range(1, len(data) + 1)
        print(tabulate(data, headers='keys', tablefmt='grid'))
        print('\nKetik "0" untuk kembali')
        try:
            inputUser = int(input('Masukkan Kode pemesanan yang akan diantar : '))
        except ValueError:
            print('Pilihan harus angka & tidak boleh kosong!')
            time.sleep(2)
            continue

        if inputUser == 0:
            halaman_admin()
            return

        if not data[(data['kode'] == inputUser) & (data['status'] == 'Diantar')].empty:
            print('Pesanan dengan kode tersebut telah diantar!')
            time.sleep(2)
            continue

        if inputUser in data['kode'].values:
            os.system('cls')
            data2 = pd.read_csv('csv/dataKendaraan.csv')
            data2.index = range(1, len(data2) + 1)
            print(tabulate(data2, headers='keys', tablefmt='grid'))

            inputKode = input('Masukkan kode kendaraan untuk digunakan pengiriman : ').upper()

            if not data2[(data2['kode'] == inputKode) & (data2['Status'] == 'BEROPERASI')].empty:
                print('Kendaraan tersebut sedang beroperasi, pilih yang lain')
                time.sleep(2)
                continue

            if inputKode in data2['kode'].values:
                data2.loc[data2['kode'] == inputKode, 'Status'] = 'BEROPERASI'
                data2.to_csv('csv/dataKendaraan.csv', index=False)
                data.loc[data['kode'] == inputUser, 'status'] = 'Diantar'
                data.to_csv('csv/dataPengiriman.csv', index=False)
                print(f'Pesanan dengan kode {inputUser} telah diantar...')
                time.sleep(2)
                halaman_admin()
                return
            else:
                print('Tidak ada kendaraan dengan kode tersebut!')
                time.sleep(2)
                continue
        else:
            print('Tidak ada pesanan dengan kode tersebut!')
            time.sleep(2)
            continue


def kelola_mitra():
    os.system('cls')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^ 	     	   SELAMAT DATANG            ^^^ ||')
    print('||----- Berikut menu untuk mengelola mitra ------||')
    print('||                1. Cek Data mitra              ||')
    print('||                2. Tambah mitra                ||')
    print('||                3. Hapus mitra                 ||')
    print('||                4. Edit mitra                  ||')
    print('||                5. Kembali                     ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    pilihan = int(input("Masukan Pilihan Anda : "))
    try:
        if pilihan == 1:
            os.system('cls')
            data = pd.read_csv('csv/dataMitra.csv')
            data.index = range(1, len(data)+1)
            print(tabulate(data,headers='keys', tablefmt='grid'))
            input('Tekan enter untuk kembali>>>')
            kelola_mitra()
        elif pilihan == 2:
            kelola_mitra_Tambah()
        elif pilihan == 3:
            kelola_mitra_hapus()
        elif pilihan == 4:
            kelola_mitra_edit()
        elif pilihan == 5:
            halaman_admin()
        else:
            print('Tidak ada di pilihan')
            time.sleep(2)
            kelola_mitra()
    except ValueError:
        print('Pilihan harus berupa angka & tidak boleh kosong!')
        time.sleep(2)
        kelola_mitra()

def kelola_mitra_Tambah():
    os.system('cls')
    status = 'Tersedia'
    data = pd.read_csv('csv/dataMitra.csv')
    kodeMitra = input('Masukkan kode Mitra : ').upper()
    namaMitra = input('Masukkan nama Mitra : ').capitalize()
    alamatMitra = input('Masukkan lokasi Mitra : ').capitalize()
    kontakMitra = int(input('Masukkan kontak Mitra : '))
    if kodeMitra == '' or namaMitra == '' or alamatMitra == '' or kontakMitra == '':
        print('Tidak boleh ada yang kosong!')
        time.sleep(2)
        halaman_user()
    if kodeMitra in data['kode'].values:
        print('Kode sudah ada, gunakan kode lain!')
        time.sleep(2)
        kelola_mitra_Tambah()
    else:
        with open('csv/dataMitra.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([kodeMitra,namaMitra,alamatMitra,kontakMitra,status])
        with open(f'csv/toko/{kodeMitra}.csv', 'w', newline='') as fil:
            writer2 = csv.writer(fil)
            writer2.writerow(['KodeBrg','NamaBrg','Harga','Stok'])
        print('Data anda berhasil ditambahkan...')
        time.sleep(2)
        kelola_mitra()

def kelola_mitra_hapus():
    os.system('cls')
    data = pd.read_csv('csv/dataMitra.csv')
    data.index = range(1, len(data)+1)
    print(tabulate(data,headers='keys', tablefmt='grid'))
    print('KETIK "EXIT" UNTUK KEMBALI')
    hapusMitra = input('Masukkan kode mitra yang ingin dihapus : ').upper()
    if hapusMitra == 'EXIT':
        kelola_mitra()
    if os.path.exists(f'csv/toko/{hapusMitra}.csv'):
        konfirmasi = input('Apakah anda yakin ingin menghapus mitra [y][n] : ').lower()
        if konfirmasi == 'y':
            data = data[data['kode'] != hapusMitra]
            data.to_csv('csv/dataMitra.csv', index=False)
            os.remove(f'csv/toko/{hapusMitra}.csv')
            print('Mitra berhasil dihapus...')
            time.sleep(2)
            kelola_mitra()
        elif konfirmasi == 'n':
            print('Penghapusan dibatalkan...')
            time.sleep(2)
            kelola_mitra_hapus()
        else:
            print('Pilihan tidak sesuai & tidak boleh kosong')
            time.sleep(2)
            kelola_mitra_hapus()
    else:
        print('Tidak ada mitra dengan kode tersebut')
        time.sleep(2)
        kelola_mitra_hapus()

def kelola_mitra_edit():
    os.system('cls')
    data = pd.read_csv('csv/dataMitra.csv')
    data.index = range(1, len(data)+1)
    print(tabulate(data,headers='keys', tablefmt='grid'))
    print('KETIK "EXIT" UNTUK KEMBALI')
    kodeMitra = input('Masukkan kode toko yang ingin diubah : ').upper()
    if kodeMitra == 'EXIT':
        kelola_mitra()
    if kodeMitra in data['kode'].values:
        print('''Ingin mengubah bagian :
1. Nama
2. Lokasi
3. Kontak
4. Keluar''')
        try:
            inputUser = int(input('Masukkan pilihan : '))
            if inputUser == 1:
                inputNama = input('Masukkan nama baru : ').capitalize()
                data.loc[data['kode'] == kodeMitra, 'Nama'] = inputNama
                data.to_csv('csv/dataMitra.csv',index=False)
                print('Nama berhasil diubah')
                time.sleep(2)
                kelola_mitra()
            elif inputUser == 2:
                inputLok = input('Masukkan lokasi baru : ').capitalize()
                data.loc[data['kode'] == kodeMitra, 'Alamat'] = inputLok
                data.to_csv('csv/dataMitra.csv', index=False)
                print('Lokasi berhasil diubah...')
                time.sleep(2)
                kelola_mitra()
            elif inputUser == 3:
                inputKontak = int(input('Masukkan Kontak baru : '))
                data.loc[data['kode'] == kodeMitra, 'Kontak'] = inputKontak
                data.to_csv('csv/dataMitra.csv', index=False)
                print('Kontak berhasil diubah...')
                time.sleep(2)
                kelola_mitra()
            elif inputUser == 4:
                kelola_mitra()
            else:
                print('tidak ada di pilihan')
                time.sleep(2)
                kelola_mitra_edit()
        except ValueError:
            print('Pilihan harus berupa angka & tidak boleh kosong')
            time.sleep(2)
            kelola_mitra_edit()
    else:
        print('Tidak ada mitra dengan kode tersebut')
        time.sleep(2)
        kelola_mitra_edit()

def kelola_barang():
    os.system('cls')
    global inputToko
    data = pd.read_csv('csv/dataMitra.csv')
    data.index = range(1, len(data)+1)
    print(tabulate(data,headers='keys', tablefmt='grid'))
    print('Ketik "EXIT" Untuk kembali')
    inputToko = input('Masukkan kode Toko : ').upper()
    if ((data['kode'] == inputToko) & (data['Status'] == 'Tersedia')).any():
        print('Toko terdeteksi, mengarahkan ke halaman...')
        time.sleep(2)
        menu_kelola_barang()
    elif inputToko == 'EXIT':
        halaman_admin()
    else:
        print('Tidak ada toko dengan kode tersebut')
        time.sleep(2)
        kelola_barang()

def menu_kelola_barang():
    os.system('cls')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^ 	     	   SELAMAT DATANG            ^^^ ||')
    print('||--------- Apa yang ingin anda lakukan?---------||')
    print('||                1. Tampilkan Barang            ||')
    print('||                2. Tambah Barang               ||')
    print('||                3. Edit barang                 ||')
    print('||                4. Hapus barang                 ||')
    print('||                5. Keluar                      ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    inputUser = int(input('Masukkan pilihan : '))
    if inputUser == 1:
        tampilkan_barang()
    elif inputUser == 2:
        tambah_barang()
    elif inputUser == 3:
        edit_barang()
    elif inputUser == 5:
        halaman_admin()
    elif inputUser == 4:
        hapus_barang()
    else:
        print('Tidak ada dipilihan...')
        time.sleep(2)
        menu_kelola_barang()

def tampilkan_barang():
    os.system('cls')
    data = pd.read_csv(f'csv/toko/{inputToko}.csv')
    data.index = range(1, len(data)+1)
    print(tabulate(data,headers='keys', tablefmt='grid'))
    input('Tekan ENTER Untuk Keluar >>>')
    menu_kelola_barang()

def hapus_barang():
    os.system('cls')
    data = pd.read_csv(f'csv/toko/{inputToko}.csv')
    data.index = range(1,len(data)+1)
    print(tabulate(data,headers='keys',tablefmt='grid'))
    print('Ketik "EXIT" untuk kembali')
    kode = input('Masukkan kode barang yang ingin dihapus : ').upper()
    if kode in data['KodeBrg'].values:
        data = data[data['KodeBrg'] != kode]
        data.to_csv(f'csv/toko/{inputToko}.csv',index=False)
    elif kode == 'EXIT':
        menu_kelola_barang()
    else:
        print('Tidak ada kode barang yang sesuai')
        time.sleep(2)
        hapus_barang()
    print('Berhasil menghapus barang...')
    time.sleep(2)
    menu_kelola_barang()

def tambah_barang():
    os.system('cls')
    print('='*40)
    print('TAMBAH BARANG'.center(40))
    print('='*40)
    data = pd.read_csv(f'csv/toko/{inputToko}.csv')
    kodeBrg = input('Masukkan kode barang : ').upper()
    namaBrg = input('Masukkan nama barang : ').capitalize()
    hargaBrg = int(input('Tentukan harga barang : '))
    stokBrg = int(input('Masukkan Jumlah Stok :'))
    if kodeBrg in data['KodeBrg'].values:
        print('Kode sudah ada, pilih kode lain!')
        time.sleep(2)
        tambah_barang()
    else:
        with open(f'csv/toko/{inputToko}.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([kodeBrg,namaBrg,hargaBrg,stokBrg])
        print('Barang berhasil ditambahkan...')
        time.sleep(2)
        menu_kelola_barang()

def edit_barang():
    os.system('cls')
    print("=" * 40)
    print(" PILIH OPSI ".center(40, "="))
    print("=" * 40)
    print("1. Ubah Nama Barang".ljust(30))
    print("2. Ubah Harga Barang".ljust(30))
    print("3. Tambah Stok".ljust(30))
    print("4. Kurangi Stok".ljust(30))
    print("5. Kembali".ljust(30))
    print("=" * 40)
    inputUser = int(input('Masukkan pilihan : '))
    if inputUser == 1:
        ubah_nama_barang()
    elif inputUser == 2:
        ubah_harga_barang()
    elif inputUser == 3:
        tambah_stok_barang()
    elif inputUser == 4:
        kurangi_stok_barang()
    elif inputUser == 5:
        menu_kelola_barang()
    else:
        print('Tidak ada di pilihan...')
        time.sleep(2)
        edit_barang()

def ubah_nama_barang():
    while True:
        os.system('cls')
        data = pd.read_csv(f'csv/toko/{inputToko}.csv')
        print('Ketik "M" untuk lihat kode barang')
        inputKode = input('Masukkan kode barang yang akan diubah : ').upper()
        if inputKode == 'M':
            os.system('cls')
            data.index = range(1, len(data)+1)
            print(tabulate(data,headers='keys', tablefmt='grid'))
            input('Klik ENTER untuk kembali >>>')
            continue
        elif inputKode in data['KodeBrg'].values:
            a = input('Masukkan nama baru : ').capitalize()
            data.loc[data['KodeBrg'] == inputKode, 'NamaBrg'] = a
            data.to_csv(f'csv/toko/{inputToko}.csv', index=False)
            print('Nama barang berhasil diubah...')
            time.sleep(2)
            edit_barang()
        else:
            print('Kode tidak ditemukan')
            time.sleep(2)
            edit_barang()

def ubah_harga_barang():
    while True:
        os.system('cls')
        data = pd.read_csv(f'csv/toko/{inputToko}.csv')
        print('Ketik "M" untuk lihat kode barang')
        inputKode = input('Masukkan kode barang yang akan diubah : ').upper()
        if inputKode == 'M':
            os.system('cls')
            data.index = range(1, len(data)+1)
            print(tabulate(data,headers='keys', tablefmt='grid'))
            input('Klik ENTER untuk kembali >>>')
            continue
        elif inputKode in data['KodeBrg'].values:
            a = int(input('Masukkan harga baru : '))
            data.loc[data['KodeBrg'] == inputKode, 'Harga'] = a
            data.to_csv(f'csv/toko/{inputToko}.csv', index=False)
            print('Harga barang berhasil diubah...')
            time.sleep(2)
            edit_barang()
        else:
            print('Kode tidak ditemukan')
            time.sleep(2)
            edit_barang()

def tambah_stok_barang():
    while True:
        os.system('cls')
        data = pd.read_csv(f'csv/toko/{inputToko}.csv')
        print('Ketik "M" untuk lihat kode barang')
        inputKode = input('Masukkan kode barang yang akan diubah : ').upper()
        if inputKode == 'M':
            os.system('cls')
            data.index = range(1, len(data)+1)
            print(tabulate(data,headers='keys', tablefmt='grid'))
            input('Klik ENTER untuk kembali >>>')
            continue
        elif inputKode in data['KodeBrg'].values:
            a = int(input('Tambahkan jumlah stok : '))
            data.loc[data['KodeBrg'] == inputKode, 'Stok'] += a
            data.to_csv(f'csv/toko/{inputToko}.csv', index=False)
            print('Stok barang berhasil ditambah...')
            time.sleep(2)
            edit_barang()
        else:
            print('Kode tidak ditemukan')
            time.sleep(2)
            edit_barang()

def kurangi_stok_barang():
    while True:
        os.system('cls')
        data = pd.read_csv(f'csv/toko/{inputToko}.csv')
        print('Ketik "M" untuk lihat kode barang')
        inputKode = input('Masukkan kode barang yang akan diubah : ').upper()
        if inputKode == 'M':
            os.system('cls')
            data.index = range(1, len(data)+1)
            print(tabulate(data,headers='keys', tablefmt='grid'))
            input('Klik ENTER untuk kembali >>>')
            continue
        elif inputKode in data['KodeBrg'].values:
            a = int(input('Kurangi jumlah stok : '))
            cek = data[data['KodeBrg'] == inputKode]
            jml = cek['Stok'].values[0]
            if jml < 1:
                print('Barang tidak memiliki stok, tidak bisa dikurangi')
                time.sleep(2)
                edit_barang()

            elif a > jml:
                print('Jumlah yang diinput melebihi stok yang ada')
                time.sleep(2)
                kurangi_stok_barang()
            else:
                data.loc[data['KodeBrg'] == inputKode, 'Stok'] -= a
                data.to_csv(f'csv/toko/{inputToko}.csv', index=False)
                print('Stok barang berhasil dikurangi...')
                time.sleep(2)
                edit_barang()
        else:
            print('Kode tidak ditemukan')
            time.sleep(2)
            edit_barang()

def kelola_kendaraan():
    os.system('cls')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^ 	     	   SELAMAT DATANG            ^^^||')
    print('||----- Berikut menu untuk kelola kendaraan -----||')
    print('||                1. Cek kendaraan               ||')
    print('||                2. Tambah kendaraan            ||')
    print('||                3. Edit kendaraan              ||')
    print('||                4. Hapus kendaraan             ||')
    print('||                5. Kembali                     ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    try:
        pilihan = int(input("Masukan Pilihan Anda : "))
        if pilihan == 1:
            cek_ketersediaan_kendaraan()
        elif pilihan == 2:
            tambah_kendaraan()
        elif pilihan == 3:
            edit_kendaraan()
        elif pilihan == 4:
            hapus_kendaraan()
        elif pilihan == 5:
            halaman_admin()
        else:
            print("pilihan tidak ada, silahkan coba lagi")
            time.sleep(2)
            kelola_kendaraan()
    except ValueError:
        print("input harus berupa angka, silahkan coba lagi")
        time.sleep(2)
        kelola_kendaraan()

def cek_ketersediaan_kendaraan():
    os.system('cls')
    try:
        data = pd.read_csv('csv/dataKendaraan.csv')
        data.index = range(1,len(data)+1)
        print(tabulate(data,headers='keys',tablefmt='grid'))
    except FileNotFoundError:
        print("data kendaraan tidak ditemukan")
    input("tekan enter untuk kembali...")
    kelola_kendaraan()

def tambah_kendaraan():
    os.system('cls')
    status = 'Tersedia'
    kodeKendraan = input('Masukkan kode kendaraan : ').upper()
    jenisInput = input("masukkan jenis kendaraan : ").capitalize()
    inputPlat = input("masukkan nomor Plat kendaraan: ").upper()
    if kodeKendraan == '' or jenisInput == '' or inputPlat == '' :
        print("input tidak boleh kosong")
        time.sleep(2)
        tambah_kendaraan()
    with open('csv/dataKendaraan.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([kodeKendraan,jenisInput,inputPlat,status])
    print("kendaraan berhasil ditambahkan")
    time.sleep(2)
    kelola_kendaraan()

def edit_kendaraan():
    os.system('cls')
    try:
        data = pd.read_csv('csv/dataKendaraan.csv')
        data.index = range(1,len(data)+1)
        print(tabulate(data,headers='keys',tablefmt='grid'))
        kode = input("masukkan kode kendaraan yang ingin diedit: ").upper()
        if kode in data['kode'].values:
            print('Data kendaraan ditemukan')
            jenis_baru = input("masukkan jenis kendaraan baru (kosongkan jika tidak ada yang diubah) : ").capitalize()
            status_baru = input("masukkan status kendaraan baru (kosongkan jika tidak ada yang diubah) : ").capitalize()
            if jenis_baru:
                data.loc[data['kode'] == kode, 'Jenis'] = jenis_baru
            if status_baru:
                data.loc[data['kode'] == kode, 'Status'] = status_baru
            data.to_csv('csv/dataKendaraan.csv', index=False)
            print("Data kendaraan berhasil di tambahkan")
        else:
            print("Data kendaraan tidak ditemukan")
    except ValueError:
        print("Data kendaraan tidak ditemukan")
    input("Tekan enter untuk kembali...")
    kelola_kendaraan()

def hapus_kendaraan():
    os.system('cls')
    data = pd.read_csv('csv/dataKendaraan.csv')
    data.index = range(1,len(data)+1)
    print(tabulate(data,headers='keys',tablefmt='grid'))
    kode = input("Masukkan kode kendaraan yang ingin dihapus: ").upper()
    if kode in data['kode'].values:
        data = data[data['kode'] != kode]
        data.to_csv('csv/dataKendaraan.csv', index=False)
        print("Kendaraan berhasil dihapus.")
        time.sleep(2)
        kelola_kendaraan()
    else:
        print("Kendaraan tidak ditemukan.")
        time.sleep(2)
        kelola_kendaraan()
    input("Tekan enter untuk kembali...")
    kelola_kendaraan()


def kelola_user():
    os.system('cls')    
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^ 	     	   SELAMAT DATANG            ^^^ ||')
    print('||----- Berikut menu untuk mengelola user ------||')
    print('||                1. Cek Data user              ||')
    print('||                2. Cek Data Admin             ||')
    print('||                3. Tambah user                ||')
    print('||                4. Hapus user                 ||')
    print('||                5. Ganti Pass user            ||')
    print('||                6. Tambah Admin               ||')
    print('||                7. Kembali                    ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    try:
        inputUser = int(input('Masukkan pilihan : '))
        if inputUser == 1:
            tampilkan_user()
        elif inputUser == 2:
            tampilkan_admin()
        elif inputUser == 3:
            tambah_user()
        elif inputUser == 4:
            hapus_user()
        elif inputUser == 5:
            ganti_pass_user()
        elif inputUser == 6:
            tambah_admin()
        elif inputUser == 7:
            halaman_admin()
        else:
            print('Pilihan tidak ada')
            time.sleep(1.5)
    except ValueError:
        print('Pilihan harus berupa angka & tidak boleh kosong')
        time.sleep(2)
        kelola_user()

def ganti_pass_user():
    os.system('cls')
    data = pd.read_csv('csv/dataUser.csv')
    print(tabulate(data,headers='keys',tablefmt='grid'))
    print('\nKetik "exit" untuk kembali')
    user = input('Masukkan username user yang ingin diganti passwordnya : ').lower()
    if user in data['Username'].values:
        user2 = input('Masukkan password baru : ')
        data.loc[data['Username'] == user, 'Password'] = user2
        data.to_csv('csv/dataUser.csv', index=False)
        print('Password berhasil diganti...')
        time.sleep(2)
        kelola_user()
    elif user == 'exit':
        kelola_user()
    else:
        print('Username tidak ditemukan')
        time.sleep(2)
        ganti_pass_user()

def hapus_user():
    os.system('cls')
    data = pd.read_csv('csv/dataUser.csv')
    data.index = range(1,len(data)+1)
    print(tabulate(data,headers='keys',tablefmt='grid'))
    print('\nKetik "exit" untuk kembali')
    user = input('Masukkan username user yang ingin dihapus : ').lower()
    if user in data['Username'].values:
        data = data.loc[data['Username'] != user]
        data.to_csv('csv/dataUser.csv', index=False)
        print('User berhasil dihapus!')
        time.sleep(2)
        kelola_user()
    elif user == 'exit':
        kelola_user()
    else:
        print('User tidak ditemukan!')
        time.sleep(2)
        hapus_user()

def tampilkan_user():
    os.system('cls')
    df = pd.read_csv('csv/dataUser.csv')
    df.index = range(1, len(df)+1)
    print(tabulate(df,headers='keys', tablefmt='grid'))
    input('Tekan enter untuk kembali>>>')
    kelola_user()

def tampilkan_admin():
    os.system('cls')
    df = pd.read_csv('csv/dataAdmin.csv')
    df.index = range(1, len(df)+1)
    print(tabulate(df.head(5),headers='keys', tablefmt='grid'))
    input('Tekan enter untuk kembali>>>')
    kelola_user()

def tambah_admin():
    os.system('cls')
    print('Anda masuk dalam menu tambah admin')
    print('Silahkan masukan data admin yang akan ditambahkan')
    adminUser = input('Masukkan username : ')
    adminPass = input('Masukkan Password : ')
    with open('csv/dataAdmin.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([adminUser,adminPass])
        print('data Admin berhasil ditambahkan')
        time.sleep(2)
        halaman_admin()

def tambah_user():
    os.system('cls')
    saldo = 0
    adminUser = input('Masukkan username : ')
    adminPass = input('Masukkan Password : ')
    with open('csv/dataUser.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([adminUser,adminPass,saldo])
        print('data User berhasil ditambahkan')
        input('tekan enter untuk kembali>>>')
    halaman_admin()

def laporan_admin():
    os.system('cls')
    print('='*40)
    print('LAPORAN'.center(40))
    print('='*40)
    print('Pilih laporan apa yang ingin di tampilkan')
    print('1. Laporan keluhan\n2. Kembali')
    pilihan = int(input('Masukkan pilihan : '))
    if pilihan == 1:
        laporan_keluhan()
    elif pilihan == 2:
        halaman_admin()
    else:
        print('Tidak ada di pilihan...')
        time.sleep(2)
        laporan_admin()

def laporan_keluhan():
    os.system('cls')
    data = pd.read_csv('csv/keluhanUser.csv')
    data.index = range(1, len(data)+1)
    print(tabulate(data,headers='keys',tablefmt='grid'))
    input('tekan ENTER untuk kembali >>>')
    laporan_admin()

utama()