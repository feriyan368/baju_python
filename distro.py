menu = "y" or "Y"
while menu == "y" or "Y":
    print(" ========================================")
    print(" Selamat Datang di  Starbox")
    print(" List")
 
    print(" ========================================")
    print(" 1. crewneck : Rp 130.000")
    print(" 2. hoodie : Rp 170.000")
    print(" 3. kemeja : Rp 200.000")
    print(" 4. kaos : Rp 160.000")
    print(" 5. celana : Rp. 170.000")
    print(" ========================================")
    listMenu=str(input(" Masukkan angka sesuai dengan menu yang tersedia = "))
    jumlahPesanan=int(input(" Jumlah dibeli = "))
    if listMenu == "1":
        namaMenu= " crewneck"
        harga=(130000*jumlahPesanan)
        pajak= int(harga * 0.1)
        if jumlahPesanan >= 5:
            totalHarga=int(harga+pajak)
        else:
            totalHarga=int(harga+pajak)
    elif listMenu == "2":
        namaMenu= "hoodie"
        harga = (170000*jumlahPesanan)
        pajak = int(harga * 0.1)
        if jumlahPesanan >= 5:
            totalHarga =int(harga+pajak)
        else:
            totalHarga =int(harga+pajak)
    elif listMenu == "3":
        namaMenu= " kemeja "
        harga=int(200000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga=int(harga+pajak)
    elif listMenu == "4":
        namaMenu= " kaos + hoodie"
        harga=int(160000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga = int(harga+pajak)
    elif listMenu == "5":
        namaMenu= " celana + koas"
        harga=int(170000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga = int(harga+pajak)
    else:
        menu=input(" Maaf,Menu yang dipilih tidak tersedia di restoran")
 
    print(" ------------------------------")
    print(" Menu :",namaMenu)
    print(" Jumlah Pesanan :", jumlahPesanan)
    print(" Harga :", harga)
    print(" Pajak :", pajak)
    print(" ------------------------------")
    print(" Total Pembayaran :", totalHarga)
    print(" ------------------------------")
    lanjut = input('Apakah Mau Beli baju Lagi y/n d')
    if lanjut == 'y' or lanjut == 'Y':
        continue
    else:
        break
