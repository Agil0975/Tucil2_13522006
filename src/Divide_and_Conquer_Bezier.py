# Module: Divide_and_Conquer_Bezier
import matplotlib.pyplot as plt
import Animation

#############################################################################################################################
#
#   Divide and Conquer Bezier dengan Mid-Point
#   
#############################################################################################################################

# fungsi yang mengembalikan titik tengah antara dua titik
def midpoint(p1, p2) -> tuple: 
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# fungsi yang mengembalikan list of midpoint diantara dua titik pada sebuah list of titik
def list_of_midpoint(p : list) -> list:
    hasil = []
    for i in range(len(p) - 1):
        hasil.append(midpoint(p[i], p[i + 1]))
    return hasil

# fungsi yang mengembalikan titik kontrol baru pada satu waktu iterasi
def Control_Point_Left(p : list) -> list:
    hasil = []
    while len(p) > 1:
        p = list_of_midpoint(p)
        hasil.append(p[0])
    return hasil

def Control_Point_Right(p : list) -> list:
    hasil = []
    while len(p) > 1:
        p = list_of_midpoint(p)
        hasil.insert(0, p[-1])
    return hasil

# fungsi yang mengembalikan titik kurva bezier pada satu waktu iterasi
def Bezier_Point(titik_kontrol : list, warna : int, animasikan: bool, pause : float) -> list:
    if len(titik_kontrol) == 1:
        return titik_kontrol
    else:
        middle_point = list_of_midpoint(titik_kontrol)
        if animasikan:
            Animation.animate_with_pause(middle_point, (warna + 1) % 7, pause)
        return Bezier_Point(middle_point, (warna + 1) % 7, animasikan, pause)

# Fungsi yang menghasilkan kurva bezier kuadratik menggunakan metode mid-point (divide and conquer)
# Fungsi ini mengembalikan list of tuple yang berisi koordinat titik-titik yang membentuk kurva bezier
# Fungsi ini:
#   - menerima 5 parameter, yaitu 
#       List of titik kontrol
#       parameter iterasi yang menentukan tingkat kedetailan kurva bezier
#       parameter warna yang menentukan warna titik tiap iterasi
#       parameter animasikan yang menentukan apakah tiap iterasi akan di animasikan atau tidak
#       parameter pause yang menentukan lama jeda antar animasi
#   - mengembalikan list of tuple yang
#       jumlah mid-point yang dihasilkan adalah 2^(iterasi) - 1 (belum termasuk titik kontrol awal dan akhir)
def DnC_Quadratik_Bezier(Titik_Kontrol : list, iterasi : int, warna : int, animasikan : bool, pause : float) -> list:
    if iterasi == 0:
        return []
    elif iterasi == 1:                # Basis
        q0 = midpoint(Titik_Kontrol[0], Titik_Kontrol[1])
        q1 = midpoint(Titik_Kontrol[1], Titik_Kontrol[2])
        b = midpoint(q0, q1)
        if animasikan:
            Animation.animate_with_pause([q0,q1], warna+1, pause)
            Animation.animate_with_pause([b], warna+2, pause)
        return [b]
    else :                          # Rekurens
        q0 = midpoint(Titik_Kontrol[0], Titik_Kontrol[1])
        q1 = midpoint(Titik_Kontrol[1], Titik_Kontrol[2])
        b = midpoint(q0, q1)
        if animasikan:
            Animation.animate_with_pause([q0,q1], warna+1, pause)
            Animation.animate_with_pause([b], warna+2, pause)
    # Rekursi
        Kiri = DnC_Quadratik_Bezier([Titik_Kontrol[0], q0, b], iterasi - 1, warna, animasikan, pause)
        Kanan = DnC_Quadratik_Bezier([b, q1, Titik_Kontrol[2]], iterasi - 1, warna, animasikan, pause)
        return Kiri + [b] + Kanan

# Fungsi yang menghasilkan generalisasi kurva bezier menggunakan metode mid-point (divide and conquer) (banyak titik kontrol >= 1)
# Fungsi ini mengembalikan list of tuple yang berisi koordinat titik-titik yang membentuk kurva bezier
# Fungsi ini:
#   - menerima 5 parameter, yaitu 
#       List of titik kontrol
#       parameter iterasi yang menentukan tingkat kedetailan kurva bezier
#       parameter warna yang menentukan warna titik tiap iterasi
#       parameter animasikan yang menentukan apakah tiap iterasi akan di animasikan atau tidak
#       parameter pause yang menentukan lama jeda antar animasi
#   - mengembalikan list of tuple yang
#       jumlah mid-point yang dihasilkan adalah 2^(iterasi) - 1 (belum termasuk titik kontrol awal dan akhir)
def DnC_Generalized_Bezier(titik_kontrol : list, iterasi : int, warna : int, animasikan : bool, pause : float) -> list:
    if iterasi == 0:
        return []
    elif iterasi == 1:                # Basis
        return Bezier_Point(titik_kontrol, warna, animasikan, pause)
    else :                          # Rekurens
        Kiri = Control_Point_Left(titik_kontrol)    # menghasilkan titik kontrol baru untuk iterasi selanjutnya (bagian kiri)
        Kiri.insert(0, titik_kontrol[0])            # menambahkan titik kontrol pertama untuk iterasi selanjutnya

        Kanan = Control_Point_Right(titik_kontrol)  # menghasilkan titik kontrol baru untuk iterasi selanjutnya (bagian kanan)
        Kanan.append(titik_kontrol[-1])             # menambahkan titik kontrol terakhir untuk iterasi selanjutnya
        
        current = Bezier_Point(titik_kontrol, warna, animasikan, pause)    # menghasilkan titik bezier pada iterasi sekarang

        return DnC_Generalized_Bezier(Kiri, iterasi - 1, warna, animasikan, pause) + current + DnC_Generalized_Bezier(Kanan, iterasi - 1, warna, animasikan, pause)
