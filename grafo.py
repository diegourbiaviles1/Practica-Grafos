
class Grafo:
    def __init__(self, es_dirigido=False):
        self.grafo = {}
        self.es_dirigido = es_dirigido

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, u, v, peso=1):
        if u not in self.grafo:
            self.agregar_vertice(u)
        if v not in self.grafo:
            self.agregar_vertice(v)
        
        if not self.es_dirigido:
            self.grafo[u].append((v, peso))
            self.grafo[v].append((u, peso))
        else:
            self.grafo[u].append((v, peso))

    def obtener_vecinos(self, vertice):
        if vertice not in self.grafo:
            raise ValueError(f"El vértice {vertice} no existe.")
        return [v[0] for v in self.grafo[vertice]]

    def existe_arista(self, u, v):
        if u not in self.grafo or v not in self.grafo:
            return False
        for vecino, _ in self.grafo[u]:
            if vecino == v:
                return True
        return False
