import copy
import random
import math
import csv

def wczytaj_csv():
    studenci = []
    with open("studenci.csv") as f:
        for row in csv.reader(f):
           studenci.append(row)
    return studenci


def popraw(studenci):
    for i in range(len(studenci)):
        for j in range(len(studenci[0])):
            if j >=0 and j <=1:
                    studenci[i][j] = str(studenci[i][j])
            if j ==2:
                    studenci[i][j] = int(studenci[i][j])
            if j >=3 and j <=7:
                if studenci[i][j] == "":
                    studenci[i][j] = 0.0
                else:
                    studenci[i][j]=float(studenci[i][j])

    for i in range(len(studenci)):
        suma = 0
        a = 0
        for j in range(3, 8):
            suma += studenci[i][j]
            if studenci[i][j] == 0:
                a += 1

        if a >= 2:
            for j in range(3, 8):
                 if studenci[i][j] == 0:
                     studenci[i][j] = 0
        elif a == 1:
            for j in range(3, 8):
              if studenci[i][j] == 0:
                studenci[i][j] = suma/5


    return studenci


def wypisz(studenci):
    for i in range(len(studenci)):
        print("|  ", end="")
        for j in range(len(studenci[0])):
            if studenci[i][j] == float:
                    if float(studenci[i][j]) == studenci[i][j]:
                        print(f"  {studenci[i][j]:^8.1f}", end='')
                    else:
                        print(f"  {studenci[i][j]:^12}", end='')
            else:
                print(f"  {studenci[i][j]:^12}", end='')
        print("  |")

def oceny(studenci):
    for i in range(len(studenci)):
        suma = 0
        for j in range(3, 8):
            suma += studenci[i][j]
        print(f"| {studenci[i][2]:^12}", end='')
        if suma <=50:
             print(2.0, end='')
        elif suma <= 60:
             print(3.0, end='')
        elif suma <= 70:
             print(3.5, end='')
        elif suma <= 80:
             print(4.0, end='')
        elif suma <= 90:
             print(4.5, end='')
        else:
             print(5.0, end='')
        print("   |")

def statystyki(studenci):
    for i in range(3,8):
        print(f"|   {i-2}", end='')
        suma = 0
        max = -float("Inf")
        min =  float("Inf")
        for j in range(len(studenci)):
            suma += studenci[j][i]
            if max < studenci[j][i]:
                max = studenci[j][i]
            if min > studenci[j][i]:
                min = studenci[j][i]

        print(f"{max:^12}{min:^12}{suma/len(studenci):^5}|")

def main():
    a = popraw(wczytaj_csv())
    wypisz(a)
    oceny(a)
    statystyki(a)

if __name__ == "__main__":
    main()
