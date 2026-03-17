import numpy as np
import matplotlib.pyplot as plt

def line(_x1, _y1, _x2, _y2):
    # y - y1 = ((y2 - y1)/(x2 - x1))*(x - x1)
    # y - A  =           B          *(x - C)
    # y = B*x - B*C + A
    #     n        l
    return [(_y2 - _y1)/(_x2 - _x1),(-((_y2 - _y1)/(_x2 - _x1))*x1 + y1)]

def display():
    plt.plot([x1,x2], [y1,y2])
    plt.plot([x1,x2], [y1,y2], ".")

    lt = True
    pdf = False

    while lt:
        opt = input("Odaberite:\n1 - Ispisati graf na ekranu.\n2 - Spremiti graf u obliku PDF datoteke.\n\nVas odabir: ")

        if (opt == "1"):
            lt = False
        elif (opt == "2"):
            pdf = True
            lt = False
        else:
            print("Neispravan odabir!\n")

    if pdf:
        name = input("Odaberite ime datoteke: ")
        plt.savefig("{}.pdf".format(name), format="pdf")
    else:
        plt.show()

loop = True

while loop:
    try:
        x1, y1 = map(float, input("Upišite koordinate x1 i y1 odvojene razmakom: ").split(" "))
        loop = False
    except ValueError:
        print("Upisane koordinate nisu valjane!\n")
        loop = True

loop = True

while loop:
    try:
        x2, y2 = map(float, input("Upišite koordinate x2 i y2 odvojene razmakom: ").split(" "))
        loop = False
    except ValueError:
        print("Upisane koordinate nisu valjane!\n")
        loop = True

ln = line(x1, y1, x2, y2)
print ("Tockama A({}, {}) i B({}, {}) prolazi pravac: y = ({})*x + ({})\n".format(x1, y1, x2, y2, ln[0], ln[1]))

display()
