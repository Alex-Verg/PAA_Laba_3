import copy


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

    def ford_bellman(self, sub=False):
        answ = [[0 if i == j else 10e7 for j in range(self.v)] for i in range(self.v)]

        for k in range(self.v-1 if sub else 0, self.v):
            for i in range(self.v-1):
                for u in range(self.v):
                    for v in range(self.v):
                        if (self.matr_sub[u][v] != 0 if not sub else True) and answ[k][v] > answ[k][u] + self.matr_sub[u][v]:
                            answ[k][v] = answ[k][u] + self.matr_sub[u][v]

            if not k:
                for i in range(self.v-1):
                    for u in range(self.v):
                        for v in range(self.v):
                            if self.matr_sub[u][v] != 0 and answ[k][v] > answ[k][u] + self.matr_sub[u][v]:
                                return False

        return answ

    def dijkstra(self):
        answ = [[0 if i == j else 10e7 for j in range(self.v)] for i in range(self.v)]

        for k in range(self.v):
            not_visit = [True for j in range(self.v)]
            for i in range(self.v):
                v = None
                for j in range(self.v):
                    if not_visit[j] and (v is None or answ[k][j] < answ[k][v]):
                        v = j
                if answ[k][v] == 10e7:
                    break
                not_visit[v] = False
                for e in range(self.v):
                    if self.matr_sub[v][e] != 0 and answ[k][v] + self.matr_sub[v][e] < answ[k][e]:
                        answ[k][e] = answ[k][v] + self.matr_sub[v][e]

        return answ

    def floyd_warshall(self):
        answ = [[self.matr_sub[i][j] if self.matr_sub[i][j] else 10e7 for j in range(self.v)] for i in range(self.v)]
        for i in range(self.v):
            answ[i][i] = 0

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

    def johnson(self):
        pass
        """if not self.ford_bellman():
            return False

        self.matr_sub.append([1] * 31)
        for i in range(self.v):
            self.matr_sub[i].append(0)
        self.v += 1
        h = self.ford_bellman(sub=True)[30][:-1]
        self.v -= 1
        for i in range(self.v):
            self.matr_sub[i].pop()
            h[i] -= 1
        self.matr_sub.pop()
        tmp_w = copy.deepcopy(self.matr_sub)
        for i in range(self.v):
            for j in range(self.v):
                if self.matr_sub[i][j] != 0:
                    self.matr_sub[i][j] = self.matr_sub[i][j] + h[i] - h[j]

        """


if __name__ == "__main__":
    gr = Graph(read_graph())
    print(*gr.ford_bellman())
    print(*gr.dijkstra())
    print(*gr.floyd_warshall())
    print(gr.johnson())
