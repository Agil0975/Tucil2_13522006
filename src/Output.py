# Module for output handling
import matplotlib.pyplot as plt

def print_points(points : list) -> None:
# prosedur yang mencetak list of tuple ke layar
    for point in points:
        print(point)

def ingin_simpan() -> bool:
# fungsi yang menerima input apakah ingin menyimpan hasil ke dalam file atau tidak
    masukan = False
    while not masukan:
        simpan = input("Apakah ingin menyimpan hasil ke dalam file? (y/n) : ")
        if simpan == "y" or simpan == "Y":
            return True
        elif simpan == "n" or simpan == "N":
            return False
        else:
            is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
            while is_ulangi != "y" and is_ulangi != "Y" and is_ulangi != "n" and is_ulangi != "N":
                is_ulangi = input("Masukan tidak valid, ingin mengulangi? (y/n) : ")
            if is_ulangi == "n" or is_ulangi == "N":
                #print("Keluar dari program")
                exit()

def save_plot_to_png(filename : str) -> None:
# prosedur yang menyimpan plot ke dalam file png
    plt.savefig("test/" + filename + ".png")
    print("Plot berhasil disimpan ke dalam file " + filename)

def save_points_to_txt(points : list, filename : str) -> None:
# prosedur yang menyimpan list of tuple ke dalam file txt
    with open("test/" + filename + ".txt", "w") as file:
        for point in points:
            file.write(str(point) + "\n")
    print("List berhasil disimpan ke dalam file " + filename)
