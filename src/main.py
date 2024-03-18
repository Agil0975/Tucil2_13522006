# Program Utama
import matplotlib.pyplot as plt
import time
import Animation
import Brute_Force_Bezier
import Divide_and_Conquer_Bezier
import Input
import Output

######################################################
# Menampilkan menu input dan meminta input dari user #
######################################################
Input.print_pembuka()
metode = Input.input_method()
jenis = Input.input_jenis(metode)
iterasi = Input.input_iterasi()
titik_kontrol = Input.input_titik_kontrol(jenis)
animasikan = Input.input_animate()
pause = Input.input_pause(animasikan)

# Memplot seluruh titik kontrol
Animation.animate_with_pause(titik_kontrol, 0, 1)

########################################################################
# Melakukan perhitungan kurva bezier sesuai dengan metode yang dipilih #
########################################################################
if metode == 1: # brute force
    # mencari titik-titik kurva bezier dan memplotnya
    start = time.time()
    if jenis == 1:
        kurva_bezier = Brute_Force_Bezier.BF_Quadratik_Bezier(titik_kontrol, iterasi, animasikan, pause)
        # hubungkan tiap titik bezier dengan garis
        Animation.animate_without_pause(kurva_bezier, 1)
        plt.pause(2)
        warna = 1
    elif jenis == 2:        # generalized
        kurva_bezier = Brute_Force_Bezier.BF_Generalized_Bezier(titik_kontrol, iterasi, animasikan, pause)
        # hubungkan tiap titik bezier dengan garis
        Animation.animate_without_pause(kurva_bezier, 1)
        plt.pause(2)
        warna = 1
    elif jenis == 3:        # animasikan dengan algoritma de casteljau
        kurva_bezier = Brute_Force_Bezier.BF_De_Casteljaus_algorithm(titik_kontrol, iterasi, animasikan, pause)
        warna = (len(titik_kontrol) % 7 - 1)
        if warna == 0:
            warna = 1
    end = time.time()

    # hapus semua plot, perbarui plot dengan kurva_bezier akhir (hanya garis tanpa titik)
    plt.clf()
    Animation.animate_without_pause(titik_kontrol, 0)
    Animation.animate_just_line(kurva_bezier, warna)
else:           # divide and conquer
    # mencari titik-titik kurva bezier dan memplotnya
    start = time.time()
    if jenis == 1:          # kuadratik
        kurva_bezier = Divide_and_Conquer_Bezier.DnC_Quadratik_Bezier(titik_kontrol, iterasi, 0, animasikan, pause)
    elif jenis == 2:                   # generalized
        kurva_bezier = Divide_and_Conquer_Bezier.DnC_Generalized_Bezier(titik_kontrol, iterasi, 0, animasikan, pause)
    end = time.time()

    # tambahkan titik kontrol awal dan akhir ke dalam kurva bezier
    kurva_bezier.insert(0, titik_kontrol[0])
    kurva_bezier.append(titik_kontrol[-1])
    
    warna = (len(titik_kontrol) % 7 - 1)
    if warna == 0:          # membedakan warna titik bezier dengan titik kontrol
        warna = 1
    
    # animasikan kurva_bezier akhir dengan hanya titik kurva bezier yang diplot
    plt.pause(2)
    plt.clf()
    Animation.animate_without_pause(titik_kontrol, 0)
    Animation.animate_without_pause(kurva_bezier, warna)
    plt.pause(2)
    
    # hapus semua plot, perbarui plot dengan kurva_bezier akhir (hanya garis tanpa titik)
    plt.clf()
    Animation.animate_without_pause(titik_kontrol, 0)
    Animation.animate_just_line(kurva_bezier, warna)

plt.show()

# Menampilkan titik-titik kurva bezier pada terminal
is_print = Input.is_print_points_to_terminal()
if is_print:
    Output.print_points(kurva_bezier)

# Menampilkan waktu eksekusi
# Mulai dari saat pertama kali melakukan pencarian titik bezier pertama hingga titik bezier terakhir
# hanya menghitung waktu yang dibutuhkan untuk untuk menghasilkan list_of_titik_bezier
Input.print_batas()
print("Waktu eksekusi:", end - start, "detik")

#####################################
# Melakukan save hasil kurva bezier #
#####################################
is_save_png = Input.ingin_simpan_to_png()
if is_save_png:
    nama_file = input("Masukkan nama file (tanpa ekstensi): ")
    # memplot ulang untuk disimpan ke dalam file
    plt.clf()
    Animation.animate_without_pause(titik_kontrol, 0)
    Animation.animate_just_line(kurva_bezier, warna)
    # menyimpan plot ke dalam file
    Output.save_plot_to_png(nama_file + " Plot")                             # menyimpan hasil plot ke dalam file
    Output.save_points_to_txt(titik_kontrol, nama_file + " Titik Kontrol")   # menyimpan titik kontrol ke dalam file

is_save_txt = Input.ingin_simpan_to_txt()
if is_save_txt:
    nama_file = input("Masukkan nama file (tanpa ekstensi): ")
    Output.save_points_to_txt(kurva_bezier, nama_file + " Titik Bezier")     # menyimpan titik bezier ke dalam file

Input.print_batas()