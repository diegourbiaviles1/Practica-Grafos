# conectividad.py
from grafo import Grafo
from collections import deque

def dfs_recursivo(grafo, vertice, visitados, recorrido):
    """Método auxiliar para DFS recursivo"""
    visitados.add(vertice)
    recorrido.append(vertice)
    for vecino, _ in grafo.grafo[vertice]:
        if vecino not in visitados:
            dfs_recursivo(grafo, vecino, visitados, recorrido)

def es_conexo(grafo):
    """Verifica si el grafo no dirigido es conexo"""
    if not grafo.grafo:
        return True  # Un grafo vacío es considerado conexo
    visitados = set()
    dfs_recursivo(grafo, next(iter(grafo.grafo)), visitados, [])
    return len(visitados) == len(grafo.grafo)

def encontrar_camino(grafo, inicio, fin):
    """Encuentra un camino entre inicio y fin"""
    visitados = set()
    padres = {inicio: None}
    cola = deque([inicio])
    
    while cola:
        vertice = cola.popleft()
        if vertice == fin:
            camino = []
            while vertice is not None:
                camino.insert(0, vertice)
                vertice = padres[vertice]
            return camino
        for vecino, _ in grafo.grafo[vertice]:
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = vertice
                cola.append(vecino)
    return []  # Si no existe camino
