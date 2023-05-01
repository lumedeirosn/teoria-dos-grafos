from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
#from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado #já é importado em meu_grafo_matriz
from meu_grafo_matriz_adjacencia_nao_dir import *

g = GrafoMatrizAdjacenciaNaoDirecionado(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g.adicionaAresta('a1', 'J', 'C')
g.adicionaAresta('a2', 'C', 'E')
g.adicionaAresta('a3', 'C', 'E')
g.adicionaAresta('a4', 'P', 'C')
g.adicionaAresta('a5', 'P', 'C')
g.adicionaAresta('a6', 'T', 'C')
g.adicionaAresta('a7', 'M', 'C')
g.adicionaAresta('a8', 'M', 'T')
g.adicionaAresta('a9', 'T', 'Z')
#print(g.N)
print(g)

g1 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g1.adicionaAresta('a1', 'J', 'C')
g1.adicionaAresta('a2', 'C', 'E')
g1.adicionaAresta('a3', 'C', 'E')
g1.adicionaAresta('a4', 'P', 'C')
g1.adicionaAresta('a5', 'P', 'C')
g1.adicionaAresta('a6', 'T', 'C')
g1.adicionaAresta('a7', 'M', 'C')
g1.adicionaAresta('a8', 'M', 'T')
g1.adicionaAresta('a9', 'T', 'Z')
print(g1.N)
print(g1.dfs('J'))

g2 = GrafoListaAdjacencia(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g2.adicionaAresta('a1', 'J', 'C')
g2.adicionaAresta('a2', 'C', 'E')
g2.adicionaAresta('a3', 'C', 'E')
g2.adicionaAresta('a4', 'P', 'C')
g2.adicionaAresta('a5', 'P', 'C')
g2.adicionaAresta('a6', 'T', 'C')
g2.adicionaAresta('a7', 'M', 'C')
g2.adicionaAresta('a8', 'M', 'T')
g2.adicionaAresta('a9', 'T', 'Z')
#print(g2)