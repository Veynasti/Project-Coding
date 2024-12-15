#KALKULATOR SEDERHAN


print(20*"=")
print("KALKULATOR SEDERHANA")
print(20*"=")

angka_1 = int(input("masukkan angka pertama : "))
option = input('masukkan opsi(+, -, *, / ): ')
angka_2 = int(input("masukkan angka ke dua : "))

#OPSI
opsi_plus = angka_1 + angka_2
opsi_mines = angka_1 - angka_2
opsi_kali = angka_1 * angka_2
opsi_bagi = angka_1 / angka_2
print(20*"=")

if option == "+":
    print('hasilnya adalah : ' + str(opsi_plus))
elif option == "-":
    print('hasilnya adalah :'+ str(opsi_mines))
elif option == "*":
    print('hasilnya adalah :'+ str(opsi_kali))
elif option == "/":
    print('hasilnya adalah :'+ str(opsi_bagi))
    print('dan jika dibulatkan maka hasilnya :'+ str(round(opsi_bagi)))

print(20*"=")