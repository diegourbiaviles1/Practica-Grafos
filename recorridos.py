
from collections import deque
from grafo import Grafo

def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])
    recorrido = []
    
    while cola:
        vertice = cola.popleft()
        if vertice not in visitados:
            visitados.add(vertice)
            recorrido.append(vertice)
            for vecino, _ in grafo.grafo[vertice]:
                if vecino not in visitados:
                    cola.append(vecino)
    return recorrido

def dfs(grafo, inicio):
    visitados = set()
    recorrido = []
    _dfs_recursivo(grafo, inicio, visitados, recorrido)
    return recorrido

def _dfs_recursivo(grafo, vertice, visitados, recorrido):
    visitados.add(vertice)
    recorrido.append(vertice)
    for vecino, _ in grafo.grafo[vertice]:
        if vecino not in visitados:
            _dfs_recursivo(grafo, vecino, visitados, recorrido)
