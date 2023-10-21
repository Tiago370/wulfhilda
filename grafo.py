from random import randint as rand
import sys

class Grafo:
    def __init__(self, nVertices: int = 0):
        self.nVertices = nVertices
        self.adjacencia = {}
        self.pesos = []
        for i in range(nVertices):
            self.pesos.append([])
            for j in range(nVertices):
                self.pesos[i].append(-1)
        self.origem = {}
        self.W = {}
        self.resetDijkstra()

    def resetDijkstra(self):
        for i in range(self.nVertices):
            self.origem[i] = -1
            self.W[i] = sys.maxsize

    def adicionarAresta(self, u: int, v: int, w: int):
        assert u < v
        if u >= self.nVertices or v >= self.nVertices or u < 0 or v < 0:
            raise Exception("Vertice inexistente")
        if u in self.adjacencia:
            self.adjacencia[u].append(v)
        else:
            self.adjacencia[u] = [v]
        
        if v in self.adjacencia:
            self.adjacencia[v].append(u)
        else:
            self.adjacencia[v] = [u]

        self.pesos[v][u] = self.pesos[u][v] = w        
    
    def adicionarVertice(self):
        self.nVertices += 1
        self.listaAdj.append([])
    
    def __str__(self):
        return f"{self.adjacencia}\n{self.pesos} "

    def dijkstra_go(self, u, v, W=0):
        if self.W[v] <= W:
            return
        self.W[v] = W
        self.origem[v] = u

        for vertice in self.adjacencia[v]:
            self.dijkstra_go(v, vertice, W + self.pesos[v][vertice])


    def dijkstra(self, origem: int, destino: int):
        self.resetDijkstra()
        self.dijkstra_go(origem, origem)

        caminho = []
        x = self.origem[destino]
        while x != origem:
            caminho.append(x)
            x = self.origem[x]
        caminho.append(origem)
        caminho.reverse()
        caminho.append(destino)
        return (self.W[destino], caminho)

if __name__ == "__main__":
    grafo = Grafo(9)
    grafo.adicionarAresta(0, 1, 4)
    grafo.adicionarAresta(0, 7, 8)
    grafo.adicionarAresta(1, 2, 8)
    grafo.adicionarAresta(1, 7, 11)
    grafo.adicionarAresta(2, 3, 7)
    grafo.adicionarAresta(2, 5, 4)
    grafo.adicionarAresta(2, 8, 2)
    grafo.adicionarAresta(3, 4, 9)
    grafo.adicionarAresta(3, 5, 14)
    grafo.adicionarAresta(4, 5, 10)
    grafo.adicionarAresta(5, 6, 2)
    grafo.adicionarAresta(6, 7, 1)
    grafo.adicionarAresta(6, 8, 6)
    grafo.adicionarAresta(7, 8, 7)

    a = rand(0, 8)
    b = rand(0, 8)
    print('a = ',a)
    print('b = ',b)
    print(grafo.dijkstra(a, b))