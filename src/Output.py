# Module for output handling
import matplotlib.pyplot as plt

def print_points(points : list) -> None:
# prosedur yang mencetak list of titik ke layar
    for point in points:
        print(point[0], point[1])

def save_plot_to_png(filename : str) -> None:
# prosedur yang menyimpan plot ke dalam file png
    plt.savefig("test/" + filename + ".png")
    print("Plot berhasil disimpan ke dalam file " + filename + ".png")

def save_points_to_txt(points : list, filename : str) -> None:
# prosedur yang menyimpan list of titik ke dalam file txt
    with open("test/" + filename + ".txt", "w") as file:
        for point in points:
            file.write(str(point[0]) + " " + str(point[1]) + "\n")
    print("Koordinat titik berhasil disimpan ke dalam file " + filename + ".txt")
