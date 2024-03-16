# Module for input handling

def print_pembuka() -> None:
# print pembuka program
    print("Program Kurva Bezier")
    print("Program ini digunakan untuk menampilkan kurva bezier dengan metode brute force atau divide and conquer")
    print("Program ini juga dapat menampilkan animasi pembentukan kurva bezier")

def print_batas() -> None:
# print batas antar menu
    print("=============================================================")

def is_float(s : str) -> bool:
# fungsi untuk mengecek apakah suatu string dapat diubah menjadi float atau tidak
    try:
        float(s)
        return True
    except ValueError:
        return False

def input_method() -> int:
# input metode yang digunakan
    print_batas()
    print("Pilih metode yang digunakan : ")
    print("   1. Brute Force")
    print("   2. Divide and Conquer")
    masukan = False
    while not masukan:
        metode = input("Pilih metode yang digunakan : ")
        if metode == "1" or metode == "2":
            masukan = True
        else:
            is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
            while is_ulangi != "y" and is_ulangi != "Y" and is_ulangi != "n" and is_ulangi != "N":
                is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
            if is_ulangi == "n" or is_ulangi == "N":
                #print("Keluar dari program")
                exit()
    return int(metode)

def input_jenis(metode : int) -> int:
# input jenis kurva bezier
    print_batas()
    if metode == 1: # brute force
        print("Pilih jenis kurva bezier : ")
        print("   1. Kurva Bezier Kuadratik")
        print("   2. Kurva Bezier N-Titik")
        print("   3. Kurva Bezier De Casteljau's N-Titik")
        masukan = False
        while not masukan:
            jenis = input("Pilih jenis kurva bezier : ")
            if jenis == "1" or jenis == "2" or jenis == "3":
                masukan = True
            else:
                is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
                while is_ulangi != "y" and is_ulangi != "Y" and is_ulangi != "n" and is_ulangi != "N":
                    is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
                if is_ulangi == "n" or is_ulangi == "N":
                    #print("Keluar dari program")
                    exit()
        return int(jenis)
    else: # divide and conquer
        print("Pilih jenis kurva bezier : ")
        print("   1. Kurva Bezier Kuadratik")
        print("   2. Kurva Bezier N-Titik")
        masukan = False
        while not masukan:
            jenis = input("Pilih jenis kurva bezier : ")
            if jenis == "1" or jenis == "2":
                masukan = True
            else:
                is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
                while is_ulangi != "y" and is_ulangi != "Y" and is_ulangi != "n" and is_ulangi != "N":
                    is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
                if is_ulangi == "n" or is_ulangi == "N":
                    #print("Keluar dari program")
                    exit()
        return int(jenis)

def input_iterasi() -> int:
# input banyaknya iterasi yang dilakukan
    print_batas()
    masukan = False
    while not masukan:
        iterasi = input("Masukkan iterasi : ")
        if iterasi.isdigit() and int(iterasi) >= 0:
            masukan = True
        else:
            is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
            while is_ulangi != "y" and is_ulangi != "Y" and is_ulangi != "n" and is_ulangi != "N":
                is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
            if is_ulangi == "n" or is_ulangi == "N":
                #print("Keluar dari program")
                exit()
    return int(iterasi)

def input_animate() -> bool:
# input apakah ingin di animasikan atau tidak (langsung menunjukkan hasil akhir)
    print_batas()
    masukan = False
    while not masukan:
        is_animasikan = input("Apakah ingin di animasikan per langkah? (y/n) : ")
        if is_animasikan == "y" or is_animasikan == "Y":
            is_animasikan = True
            masukan = True
        elif is_animasikan == "n" or is_animasikan == "N":
            is_animasikan = False
            masukan = True
        else:
            is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
            while is_ulangi != "y" and is_ulangi != "Y" and is_ulangi != "n" and is_ulangi != "N":
                is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
            if is_ulangi == "n" or is_ulangi == "N":
                #print("Keluar dari program")
                exit()
    return is_animasikan

def input_pause(is_animasi : bool) -> float:
# input lama jeda antar animasi
    print_batas()
    masukan = False
    while not masukan:
        if is_animasi:
            pause = input("Masukkan lama jeda animasi (dalam detik) : ")
            if is_float(pause) and float(pause) > 0:
                masukan = True
            else:
                is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
                while is_ulangi != "y" and is_ulangi != "Y" and is_ulangi != "n" and is_ulangi != "N":
                    is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
                if is_ulangi == "n" or is_ulangi == "N":
                    #print("Keluar dari program")
                    exit()
        else:
            pause = 0
            masukan = True
    return float(pause)

def input_jumlah_titik_kontrol() -> int:
# input jumlah titik kontrol
    masukan = False
    while not masukan:
        n = input("Masukkan jumlah titik kontrol : ")
        if n.isdigit() and int(n) > 0:
            masukan = True
        else:
            is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
            while is_ulangi != "y" and is_ulangi != "Y" and is_ulangi != "n" and is_ulangi != "N":
                is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
            if is_ulangi == "n" or is_ulangi == "N":
                #print("Keluar dari program")
                exit()
    return int(n)

def input_titik_kontrol(jenis : int) -> list:
# input daftar titik kontrol
    print_batas()
    titik_kontrol = []
    if jenis == 1:
        print("Masukkan titik kontrol (Format input : x y) : ")
        for i in range(3):
            masukan = False
            while not masukan:
                input_titik = input("Masukkan titik ke-" + str(i + 1) + " : ")
                titik = input_titik.split()
                if len(titik) == 2 and is_float(titik[0]) and is_float(titik[1]):
                    titik_kontrol.append((float(titik[0]), float(titik[1])))
                    masukan = True
                else:
                    is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
                    while is_ulangi != "y" and is_ulangi != "Y" and is_ulangi != "n" and is_ulangi != "N":
                        is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
                    if is_ulangi == "n" or is_ulangi == "N":
                        #print("Keluar dari program")
                        exit()
    else:
        n = input_jumlah_titik_kontrol()
        print("Masukkan titik kontrol : ")
        print("   Format input : x y")
        for i in range(n):
            masukan = False
            while not masukan:
                input_titik = input("Masukkan titik ke-" + str(i + 1) + " : ")
                titik = input_titik.split()
                if len(titik) == 2 and is_float(titik[0]) and is_float(titik[1]):
                    titik_kontrol.append((float(titik[0]), float(titik[1])))
                    masukan = True
                else:
                    is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
                    while is_ulangi != "y" and is_ulangi != "Y" and is_ulangi != "n" and is_ulangi != "N":
                        is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
                    if is_ulangi == "n" or is_ulangi == "N":
                        #print("Keluar dari program")
                        exit()
    return titik_kontrol
