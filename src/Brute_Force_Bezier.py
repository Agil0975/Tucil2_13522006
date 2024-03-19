# Module: Brute_Force_Bezier
import matplotlib.pyplot as plt
import math
import Animation

#############################################################################################################################
#
#   Brute Force Bezier dengan Binomial Coefficients
#   
#############################################################################################################################

# Fungsi yang menghasilkan kurva bezier kuadratik menggunakan metode brute force
# Fungsi ini mengembalikan list of tuple yang berisi koordinat titik-titik yang membentuk kurva bezier
# Fungsi ini:
#   - menerima 4 parameter, yaitu
#       List of titik kontrol
#       parameter iterasi yang menentukan tingkat kedetailan kurva bezier
#       parameter animasikan yang menentukan apakah tiap iterasi akan di animasikan atau tidak
#       parameter pause yang menentukan lama jeda antar animasi
#   - mengembalikan list of tuple dengan
#       jumlah titik yang dihasilkan adalah (2^(iterasi) + 1) (sudah termasuk titik kontrol awal dan akhir)
def BF_Quadratik_Bezier(Titik_Kontrol : list, iterasi : int, animasikan : bool, pause : float) -> list:
    # Inisialisasi list of tuple yang akan menampung koordinat titik-titik kurva bezier
    hasil = []
    # Hitung jumlah titik yang dihasilkan, belum termasuk titik kontrol awal dan akhir
    n = 2 ** iterasi - 1
    # hitung interval nilai t
    dt = 1 / (n + 1)
    # Hitung koordinat tiap titik kurva bezier
    for i in range(n + 2):          # ditambah 2 untuk mengikutsertakan titik kontrol awal dan akhir
        t = i * dt
        x = (1 - t) ** 2 * Titik_Kontrol[0][0] + 2 * (1 - t) * t * Titik_Kontrol[1][0] + t ** 2 * Titik_Kontrol[2][0]
        y = (1 - t) ** 2 * Titik_Kontrol[0][1] + 2 * (1 - t) * t * Titik_Kontrol[1][1] + t ** 2 * Titik_Kontrol[2][1]

        if animasikan:
            Animation.animate_with_pause([(x, y)], 1, pause)
        
        hasil.append((x, y))
    
    return hasil

# Fungsi yang menghasilkan generalisasi kurva bezier menggunakan metode brute force (banyak titik kontrol >= 1)
# Fungsi ini mengembalikan list of tuple yang berisi koordinat titik-titik yang membentuk kurva bezier
# Fungsi ini:
#   - menerima 4 parameter, yaitu 
#       List of titik kontrol
#       parameter iterasi yang menentukan tingkat kedetailan kurva bezier
#       parameter animasikan yang menentukan apakah tiap iterasi akan di animasikan atau tidak
#       parameter pause yang menentukan lama jeda antar animasi
#   - mengembalikan list of tuple yang
#       jumlah mid-point yang dihasilkan adalah 2^(iterasi) + 1 (sudah termasuk titik kontrol awal dan akhir)
def BF_Generalized_Bezier(Titik_Kontrol : list, iterasi : int, animasikan : bool, pause : float) -> list:
    hasil = []
    n = 2 ** iterasi - 1 # banyak titik yang dihasilkan, belum termasuk titik kontrol awal dan akhir
    dt = 1 / (n + 1)

    for i in range(n + 2): # ditambah 2 untuk untuk mengikutsertakan titik kontrol awal dan akhir
        t = i * dt  
        x = 0
        y = 0
        for j in range(len(Titik_Kontrol)):
            x += (math.comb(len(Titik_Kontrol) - 1, j)) * ((1 - t) ** (len(Titik_Kontrol) - 1 - j)) * (t ** j) * (Titik_Kontrol[j][0])
            y += (math.comb(len(Titik_Kontrol) - 1, j)) * ((1 - t) ** (len(Titik_Kontrol) - 1 - j)) * (t ** j) * (Titik_Kontrol[j][1])

        if animasikan:
            Animation.animate_with_pause([(x, y)], 1, pause)
            
        hasil.append((x, y))

    return hasil



#############################################################################################################################
#
#   Brute Force Bezier dengan Algoritma De Casteljau
#   
#############################################################################################################################

# fungsi yang mengembalikan titik yang berjarak sebesar dt*panjang_garis_antara_p1_p2 dari titik p1 
# yang berada pada garis yang menghubungkan titik p1 ke titik p2
def point_dt(p1, p2, dt) -> tuple:
    # hitung peruabahan koordinat x dan y
    dx = abs(p2[0] - p1[0]) * dt
    dy = abs(p2[1] - p1[1]) * dt
    # tentukan arah perubahan koordinat x dan y
    if p2[0] < p1[0]:
        dx = -dx
    if p2[1] < p1[1]:
        dy = -dy
    # hitung koordinat titik yang dihasilkan
    x = p1[0] + dx
    y = p1[1] + dy

    return (x, y)

# fungsi yang mengembalikan point_dt diantara dua titik pada sebuah list of titik
def list_of_point_dt(p : list, dt : float) -> list:
    hasil = []
    for i in range(len(p) - 1):
        hasil.append(point_dt(p[i], p[i + 1], dt))
    return hasil

# fungsi yang mengembalikan titik bezier pada satu waktu iterasi
def Titik_Bezier(titik_kontrol : list, warna : int, dt : float, animasikan : bool) -> list:
    if len(titik_kontrol) == 1:
        if animasikan:
            Animation.animate_without_pause(titik_kontrol, warna)
        return titik_kontrol
    else:
        new_kontrol_point = list_of_point_dt(titik_kontrol, dt)
        if animasikan:
            Animation.animate_without_pause(new_kontrol_point, (warna + 1) % 7)
        return Titik_Bezier(new_kontrol_point, (warna + 1) % 7, dt, animasikan)

# Algoritma De Casteljau
# Fungsi yang menghasilkan kurva bezier kuadratik menggunakan metode De Casteljau
# Fungsi ini mengembalikan list of tuple yang berisi koordinat titik-titik yang membentuk kurva bezier
# Fungsi ini:
#   - menerima 3 parameter, yaitu
#       List of titik kontrol
#       parameter iterasi yang menentukan tingkat kedetailan kurva bezier
#       parameter pause yang menentukan lama jeda antar animasi
#   - mengembalikan list of tuple dengan
#       jumlah titik yang dihasilkan adalah (2^(iterasi) + 1) (sudah termasuk titik kontrol awal dan akhir)
def BF_De_Casteljaus_algorithm(TitiK_Kontrol : list, iterasi : int, animasikan : bool, pause : float) -> list:
    hasil = []
    n = 2 ** iterasi - 1 # banyak titik yang dihasilkan, belum termasuk titik kontrol awal dan akhir
    dt = 1 / (n + 1)

    for i in range(n + 2):
        t = i * dt
        p = Titik_Bezier(TitiK_Kontrol, 0, t, animasikan)
        hasil.append(p[0])
        
        if animasikan:
            # Menghapus plot sebelumnya
            plt.pause(pause)
            plt.clf()
            # Menggambar ulang plot
            Animation.animate_without_pause(TitiK_Kontrol, 0)
            plt.plot([j[0] for j in hasil], [j[1] for j in hasil], c = Animation.COLOUR[(len(TitiK_Kontrol) % 7)-1])

    return hasil
