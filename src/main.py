# Program Utama
import matplotlib.pyplot as plt
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

if jenis != 3:              # jika memilih algoritma de casteljau pasti dianimasikan
    animasikan = Input.input_animate()
    pause = Input.input_pause(animasikan)
else:
    animasikan = True
    pause = Input.input_pause(animasikan)

# Memplot seluruh titik kontrol
Animation.animate_with_pause(titik_kontrol, 0, 1)

########################################################################
# Melakukan perhitungan kurva bezier sesuai dengan metode yang dipilih #
########################################################################
if metode == 1: # brute force
    if jenis == 1:          # kuadratik
        if animasikan:
            # plot titik kontrol pertama sebagai titik bezier pertama
            Animation.animate_with_pause([titik_kontrol[0]], 1, pause)
            # hitung kurva bezier
            kurva_bezier = Brute_Force_Bezier.BF_Quadratik_Bezier(titik_kontrol, iterasi, animasikan, pause)
            kurva_bezier.insert(0, titik_kontrol[0])
            kurva_bezier.append(titik_kontrol[2])
            # plot titik kontrol terakhir sebagai titik bezier terakhir
            Animation.animate_with_pause([titik_kontrol[2]], 1, pause)
            # animasikan kurva_bezier akhir
            Animation.animate_without_pause(kurva_bezier, 1)
            plt.pause(2)
        else : # langsung kurva_bezier akhir
            kurva_bezier = Brute_Force_Bezier.BF_Quadratik_Bezier(titik_kontrol, iterasi, animasikan, pause)
            kurva_bezier.insert(0, titik_kontrol[0])
            kurva_bezier.append(titik_kontrol[2])
        # hapus semua plot, perbarui plot dengan kurva_bezier akhir (hanya garis tanpa titik)
        plt.clf()
        Animation.animate_without_pause(titik_kontrol, 0)
        warna = 1
        Animation.animate_just_line(kurva_bezier, warna)
    elif jenis == 2:        # generalized
        if animasikan:
            # plot titik kontrol pertama sebagai titik bezier pertama
            Animation.animate_with_pause([titik_kontrol[0]], 1, pause)
            # hitung kurva bezier
            kurva_bezier = Brute_Force_Bezier.BF_Generalized_Bezier(titik_kontrol, iterasi, animasikan, pause)
            kurva_bezier.insert(0, titik_kontrol[0])
            kurva_bezier.append(titik_kontrol[-1])
            # plot titik kontrol terakhir sebagai titik bezier terakhir
            Animation.animate_with_pause([titik_kontrol[-1]], 1, pause)
            # animasikan kurva_bezier akhir
            Animation.animate_without_pause(kurva_bezier, 1)
            plt.pause(2)
        else : # langsung kurva_bezier akhir
            kurva_bezier = Brute_Force_Bezier.BF_Generalized_Bezier(titik_kontrol, iterasi, animasikan, pause)
            kurva_bezier.insert(0, titik_kontrol[0])
            kurva_bezier.append(titik_kontrol[-1])
        # hapus semua plot, perbarui plot dengan kurva_bezier akhir (hanya garis tanpa titik)
        plt.clf()
        Animation.animate_without_pause(titik_kontrol, 0)
        warna = 1
        Animation.animate_just_line(kurva_bezier, warna)
    elif jenis == 3:        # generalized with de casteljau
        kurva_bezier = Brute_Force_Bezier.BF_De_Casteljaus_algorithm(titik_kontrol, iterasi, 0.1)
        kurva_bezier.append(titik_kontrol[-1])
        plt.clf()
        Animation.animate_without_pause(titik_kontrol, 0)
        # membedakan warna titik bezier dengan titik kontrol
        warna = (len(titik_kontrol) % 7 - 1)
        if warna == 0:
            warna = 1
        Animation.animate_just_line(kurva_bezier, warna)
else:           # divide and conquer
    if jenis == 1:          # kuadratik
        if animasikan:
            # hitung kurva bezier
            kurva_bezier = Divide_and_Conquer_Bezier.DnC_Quadratik_Bezier(titik_kontrol, iterasi, 0, animasikan, pause)
            kurva_bezier.insert(0, titik_kontrol[0])
            kurva_bezier.append(titik_kontrol[2])
            plt.pause(2)
            plt.clf()
            # animasikan kurva_bezier akhir dengan titik kurva bezier diplot
            Animation.animate_without_pause(titik_kontrol, 0)
            Animation.animate_without_pause(kurva_bezier, (len(titik_kontrol) % 7 - 1))
            plt.pause(2)
        else:
            kurva_bezier = Divide_and_Conquer_Bezier.DnC_Quadratik_Bezier(titik_kontrol, iterasi, 0, animasikan, pause)
            kurva_bezier.insert(0, titik_kontrol[0])
            kurva_bezier.append(titik_kontrol[2])
            plt.pause(2)
        # hapus semua plot, perbarui plot dengan kurva_bezier akhir (hanya garis tanpa titik)
        plt.clf()
        Animation.animate_without_pause(titik_kontrol, 0)
        warna = (len(titik_kontrol) % 7 - 1)
        if warna == 0:
            warna = 1
        Animation.animate_just_line(kurva_bezier, warna)
    else:                   # generalized
        if animasikan:
            # hitung kurva bezier
            kurva_bezier = Divide_and_Conquer_Bezier.DnC_Generalized_Bezier(titik_kontrol, iterasi, 0, animasikan, pause)
            kurva_bezier.insert(0, titik_kontrol[0])
            kurva_bezier.append(titik_kontrol[-1])
            plt.pause(2)
            plt.clf()
            # animasikan kurva_bezier akhir dengan titik kurva bezier diplot
            Animation.animate_without_pause(titik_kontrol, 0)
            # membedakan warna titik bezier dengan titik kontrol
            warna = (len(titik_kontrol) % 7 - 1)
            if warna == 0:
                warna = 1
            Animation.animate_without_pause(kurva_bezier, warna)
            plt.pause(2)
        else:
            kurva_bezier = Divide_and_Conquer_Bezier.DnC_Generalized_Bezier(titik_kontrol, iterasi, 0, animasikan, pause)
            kurva_bezier.insert(0, titik_kontrol[0])
            kurva_bezier.append(titik_kontrol[-1])
            plt.pause(2)
        # hapus semua plot, perbarui plot dengan kurva_bezier akhir (hanya garis tanpa titik)
        plt.clf()
        Animation.animate_without_pause(titik_kontrol, 0)
        # membedakan warna titik bezier dengan titik kontrol
        warna = (len(titik_kontrol) % 7 - 1)
        if warna == 0:
            warna = 1
        Animation.animate_just_line(kurva_bezier, warna)
plt.show()

# Menampilkan titik-titik kurva bezier pada terminal
Output.print_points(kurva_bezier)

#####################################
# Melakukan save hasil kurva bezier #
#####################################
Input.print_batas()
is_save = Output.ingin_simpan()
if is_save:
    nama_file = input("Masukkan nama file (tanpa ekstensi): ")
    # memplot ulang untuk disimpan ke dalam file
    plt.clf()
    Animation.animate_without_pause(titik_kontrol, 0)
    Animation.animate_just_line(kurva_bezier, warna)
    # menyimpan plot ke dalam file
    Output.save_plot_to_png(nama_file + " Plot")                             # menyimpan hasil plot ke dalam file
    Output.save_points_to_txt(titik_kontrol, nama_file + " Titik Kontrol")   # menyimpan titik kontrol ke dalam file
    Output.save_points_to_txt(kurva_bezier, nama_file + " Titik Bezier")     # menyimpan titik bezier ke dalam file