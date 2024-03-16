# Module for animation
import matplotlib.pyplot as plt
COLOUR = ['r', 'g', 'b', 'y', 'm', 'c', 'k']

# prosedur yang melakukan animasi pembentukan titik kurva bezier pada saat t / waktu iterasi tertentu
def animate_with_pause(list_of_point : list, warna : int, pause : float) -> None:
    plt.scatter([i[0] for i in list_of_point], [i[1] for i in list_of_point], c = COLOUR[warna])
    plt.plot([i[0] for i in list_of_point], [i[1] for i in list_of_point], c = COLOUR[warna])
    plt.pause(pause)

def animate_without_pause(list_of_point : list, warna : int) -> None:
    plt.scatter([i[0] for i in list_of_point], [i[1] for i in list_of_point], c = COLOUR[warna])
    plt.plot([i[0] for i in list_of_point], [i[1] for i in list_of_point], c = COLOUR[warna])

def animate_just_line(list_of_point : list, warna : int) -> None:
    plt.plot([i[0] for i in list_of_point], [i[1] for i in list_of_point], c = COLOUR[warna])