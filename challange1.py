def bilangan_prima(awal, akhir):
    print("Bilangan Prima:")
    for num in range(awal, akhir + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(num, end=" ")
    print("\n")

def bilangan_ganjil(awal, akhir):
    print("Bilangan Ganjil:")
    for num in range(awal, akhir + 1):
        if num % 2 != 0:
            print(num, end=" ")
    print("\n")

def bilangan_genap(awal, akhir):
    print("Bilangan Genap:")
    for num in range(awal, akhir + 1):
        if num % 2 == 0:
            print(num, end=" ")
    print("\n")

def main():
    while True:
        print("=====Cek Bilangan=====")
        print()
        print("Menu:")
        print("1. Tampilkan Bilangan Prima")
        print("2. Tampilkan Bilangan Ganjil")
        print("3. Tampilkan Bilangan Genap")
        print("0. Keluar")
        
        pilihan = input("Masukkan pilihan Anda (1/2/3/0): ")
        
        if pilihan == '0':
            print("Terima kasih, program selesai.")
            break
        
        awal = int(input("Masukkan nilai awal: "))
        akhir = int(input("Masukkan nilai akhir: "))
        
        if pilihan == '1':
            bilangan_prima(awal, akhir)
        elif pilihan == '2':
            bilangan_ganjil(awal, akhir)
        elif pilihan == '3':
            bilangan_genap(awal, akhir)
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

if __name__ == "__main__":
    main()
