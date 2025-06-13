
from grafo import Grafo
from recorridos import bfs, dfs
from conectividad import es_conexo, encontrar_camino

# Crear el grafo no dirigido
grafo_no_dirigido = Grafo(es_dirigido=False)

# Agregar vértices y aristas
grafo_no_dirigido.agregar_vertice('A')
grafo_no_dirigido.agregar_vertice('B')
grafo_no_dirigido.agregar_vertice('C')
grafo_no_dirigido.agregar_vertice('D')
grafo_no_dirigido.agregar_vertice('E')

grafo_no_dirigido.agregar_arista('A', 'B')
grafo_no_dirigido.agregar_arista('A', 'C')
grafo_no_dirigido.agregar_arista('B', 'D')
grafo_no_dirigido.agregar_arista('C', 'D')
grafo_no_dirigido.agregar_arista('D', 'E')

# Verificar los vecinos
print("Vecinos de A:", grafo_no_dirigido.obtener_vecinos('A'))
print("Vecinos de D:", grafo_no_dirigido.obtener_vecinos('D'))
try:
    print("Vecinos de F:", grafo_no_dirigido.obtener_vecinos('F'))  # Vértice no existente
except ValueError as e:
    print(e)

# Verificar existencia de aristas
print("Existe la arista ('A', 'C')", grafo_no_dirigido.existe_arista('A', 'C'))
print("Existe la arista ('A', 'D')", grafo_no_dirigido.existe_arista('A', 'D'))

# Realizar recorridos
print("\nBFS desde 'A':", bfs(grafo_no_dirigido, 'A'))
print("DFS desde 'A':", dfs(grafo_no_dirigido, 'A'))

# Verificar conectividad
print("\nEs conexo el grafo:", es_conexo(grafo_no_dirigido))

# Encontrar caminos
print("\nCamino de A a E:", encontrar_camino(grafo_no_dirigido, 'A', 'E'))
print("Camino de A a F:", encontrar_camino(grafo_no_dirigido, 'A', 'F'))
