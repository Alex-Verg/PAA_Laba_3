import copy


def read_system():
    inp = open("input.txt", "r")
    matr = inp.readlines()
    table = list(matr[0].split("], ["))
    #print(*table, sep='\n')
    table[0] = str(table[0][2:])
    table[-1] = str(table[-1][:-2])

    out = open("output.txt", "w")
    for i in range(30):
        out.write(str(table[i])+"\n")

    inp.close()
    out.close()


def read_graph():
    inp = open("output.txt", "r")
    table = inp.readlines()
    for i in range(30):
        table[i] = list(map(int, table[i].split(", ")))

    inp.close()

    return table


class Graph():

    def __init__(self, table, v=30):
        self.matr_sub = copy.deepcopy(table)
        self.v = 30

    def floyd_warshall(self):
        answ = [[self.matr_sub[i][j] if self.matr_sub[i][j] else 10e7 for j in range(self.v)] for i in range(self.v)]

        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    if answ[i][k] + answ[k][j] < answ[i][j]:
                        answ[i][j] = answ[i][k] + answ[k][j]

        return answ

        """n = self.v
        A = [[[10e6 for j in range(n)] for i in range(n)] for k in range(n + 1)]
        for i in range(n):
            for j in range(n):
                if i == j or self.matr_sub[i][j]:
                    A[0][i][j] = self.matr_sub[i][j]
        for k in range(1, n + 1):
            for i in range(n):
                for j in range(n):
                    A[k][i][j] = min(A[k - 1][i][j], A[k - 1][i][k - 1] + A[k - 1][k - 1][j])

        return A[-1]"""


if __name__ == "__main__":
    gr = Graph(read_graph())
    print(*gr.floyd_warshall())
