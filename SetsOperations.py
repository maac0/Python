import math

def podaj():
    n = int(input("Podaj rozmiar listy: "))
    assert n > 0, "Lista jest pusta"
    t = [0]*n
    i = 0
    z = -1
    while z < n-1:
        a = int(input(f"Podaj {i} element: "))
        for j in range(a):
            z += 1
            if z < n:
                t[z] = i
            else:
                break
        i += 1
    return t


def wypisz(x):
    assert len(x) > 0, "Lista jest pusta"
    suma = 0
    for i in range(len(x)):
        suma += x[i]
    a = [0]*suma
    z = -1
    for i in range(len(x)):
        for j in range(x[i]):
            z+= 1
            a[z] = i

    return a
def dodaj(x, y):
    assert y >= 0, "Element jest ujemny"
    if y > 0 and y <(len(x)):
        x[y] += 1
        return x
    elif  y >=len(x):
        n = len(x)+y-len(x)+1
        t = [0]*(n)
        for i in range(0, len(x)):
            t[i] = x[i]
        for i in range(len(x), n-1):
            t[i] = 0
        t[n-1] = 1
        return t


def przeciecie(a, b):
    i = 0
    m = len(a)
    n = len(b)

    if m > n:
        t = [0]*n
    else:
        t = [0]*m

    while i < n and i < m:
        t[i]= min(a[i], b[i])
        i += 1

    h = 0
    for i in range(len(t)-1, 0, -1):
        if t[i] == 0:
            h += 1
        else:
            break
    g = [0]*(len(t)-h)
    for i in range(0, len(t)-h):
        g[i] = t[i]
    return g

def roznica(a, b):
    c = len(a)
    e = len(przeciecie(a, b))
    y = przeciecie(a, b)

    if c > e:
         z = [0]*c
         for i in range(e):
             z[i] = a[i] - y[i]
         for i in range(e, c, 1):
             z[i] = a[i]

         h = 0
         for i in range(len(z)-1, 0, -1):
             if z[i] == 0:
                 h += 1
             else:
                 break

         g = [0] * (len(z) - h)
         for i in range(len(z) - h):
             g[i] = z[i]
         return g

    else:
        z = [0] *e
        for i in range(e):
            z[i] = a[i] - y[i]

        h = 0
        for i in range(len(z)-1, 0, -1):
            if z[i] == 0:
                h += 1
            else:
                break

        g = [0] * (len(z) - h)
        for i in range(len(z) - h):
            g[i] = z[i]
        return g


def main():
    x  =[5, 2]
    y = [5, 2, 3]
    z = 4
    print(podaj())
    print(wypisz(x))
    print(dodaj(x,z))
    print(przeciecie(x,y))
    print(roznica(y, x))

if __name__ == "__main__":
    main()