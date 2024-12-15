'''DATA'''
menu = {
    "Pocari sweat"  : 8000,
    "Matcha latte"  : 15000,
    "Silver queen"  : 20000,
    "Coca cola"     : 7000,
    "Ice cream"     : 5000
}

'''PROGRAM'''
print ("=================================== Daftar Menu ===================================")
for i in menu:
    print("Daftar Menu : ", i, "\t Harga : ", menu[i])
print("Pembelian diatas Rp 100.000, mendapatkan diskon 20%")
print("===================================================================================")
User = input("Masukkan menu yang akan anda beli : ")
jumlah = int(input("Jumlah Pesanan  : "))
Bayar = jumlah * menu[beli]

'''PROGRAM DISKON'''
if Bayar > 100000:
    diskon = Bayar * 20/100
    total = Bayar - diskon
else:
    total = Bayar

'''PROGRAM STRUK'''
print("================================== Struk Pembayaran ===============================")
print("Menu yang dipesan         : ", beli)
print("Jumlah yang di pesan      : ", jumlah)
print("Total biaya               : ", Bayar)
print("Total yang harus diabayar : ", total)
print("==================================== Terima Kasih =================================")