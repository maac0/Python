class Graph():
    def __init__(self, v_n, a_n):
        assert type(v_n) is int and v_n > 0, "to nie jest graf"
        if a_n == None:
            self.__adjacency_matrix = [[0]*v_n for i in range(v_n)]
            self.__vertices_numer = v_n
            self.__edges_number = 0
        else:
            krawedzie = 0
            for i in range(v_n):
                j = i + 1
                while j < v_n:
                    if a_n == 1:
                        krawedzie += 1
                    j+= 1
            self.__adjacency_matrix = a_n
            self.__vertices_numer = v_n
            self.__edges_number = krawedzie
    def Get_Vertices_Number(self):
        return f"{self.__vertices_numer}"
    def Get_Edges_Number(self):
        return f"{self.__edges_number}"
    def __repr__(self):
        a = "|"
        b = " "
        c = "_"
        print(f"Graph with {self.__vertices_numer} vertices and {self.__edges_number} edges:")
        print(f"{b:^5}", end="")
        for i in range(self.__vertices_numer):
            print(f"{i:^5}", end="")
        print()
        print(f"{b:^5}", end="")
        for i in range(self.__vertices_numer):
            print(f"{c:^5}", end="")
        print()
        for i in range(self.__vertices_numer):
            print(f"{str(i)+a:^5}", end="")
            for j in range(self.__vertices_numer):
                print(f"{self.__adjacency_matrix[i][j]:^5}", end="")
            print()
        return ""
    def Add_Edge(self,x,y):
        assert x >= 0 and y >= 0 and x < self.__vertices_numer and y < self.__vertices_numer
        if self.__adjacency_matrix[x][y] == 1:
            return False
        else:
            self.__adjacency_matrix[x][y] = 1
            self.__adjacency_matrix[y][x] = 1
            return True
    def Del_Edge(self, x ,y):
        assert x >= 0 and y >= 0 and x < self.__vertices_numer and y < self.__vertices_numer
        if self.__adjacency_matrix[x][y] == 0:
            return False
        else:
            self.__adjacency_matrix[x][y] = 0
            self.__adjacency_matrix[y][x] = 0
            return True
    def __add__(self, other):
        m = Graph(self.__vertices_numer, self.__adjacency_matrix)
        assert type(other) is tuple
        assert other[0] >= 0 and other[1] >= 0 and other[0] < self.__vertices_numer and other[1] < self.__vertices_numer
        m.__adjacency_matrix[other[0]][other[1]] = 1
        m.__adjacency_matrix[other[1]][other[0]] = 1
        return m
    def __sub__(self, other):
        m = Graph(self.__vertices_numer, self.__adjacency_matrix)
        assert type(other) is tuple
        assert other[0] >= 0 and other[1] >= 0 and other[0] < self.__vertices_numer and other[1] < self.__vertices_numer
        m.__adjacency_matrix[other[0]][other[1]] = 0
        m.__adjacency_matrix[other[1]][other[0]] = 0
        return m
    def Draw(self):
        import math
        from PIL import Image, ImageFont, ImageDraw
        def Draw(self):
            """
            Rysowanie grafu
            wierzcholki maja byc narysowane na okregu
            o promieniu r = 200 i srodku ox = 250, oy = 250
            """

        img = Image.new('RGB', (500, 500), color="white")
        draw = ImageDraw.Draw(img)
        # wspolrzedne srodka kola:
        ox = 250
        oy = 250
        r = 200  # promien
        step = 2 * math.pi / self.__vertices_numer
        # Rysowanie grafu:
        # obliczenie współrzędnych zerowego wierzcholka
        for i in range(self.__vertices_numer):
            px0 = ox - math.cos(step * i) * r
            py0 = oy - math.sin(step * i) * r
            draw.ellipse((px0 - 5, py0 - 5, px0 + 5, py0 + 5), fill='black')
            draw.text((px0 - 25, py0 - 25), f"{i}", fill='black')
            for j in range(self.__vertices_numer):
        # obliczenie współrzędnych pierwszego wierzcholka
                px1 = ox - math.cos(step * (j)) * r
                py1 = oy - math.sin(step * (j)) * r
        # narysowanie wierzcholkow 0 i 1
        # podpisanie wierzcholkow
        # narysowanie krawedzi 0-1
                if self.__adjacency_matrix[i][j] == 1:
                    draw.line([(px0, py0), (px1, py1)], fill='black', width=2)
        # zapisanie obrazka
        img.save('graph.png')
def main():
    list = [[0,1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1,0]]
    G1 =  Graph(10," ")
    G2 = Graph(4, list)
    G2.Add_Edge(2, 0)
    print(G2)
    G2.Add_Edge(2, 1)
    print(G2)
    G2.Del_Edge(2, 1)
    print(G2)
    G2.Del_Edge(0, 2)
    print(G2)
    a = (1,2)
    G2.__add__(a)
    print(G2)
    G2.Draw()




if __name__ == "__main__":
    main()