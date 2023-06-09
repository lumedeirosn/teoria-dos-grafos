import unittest
from meu_grafo_matriz_adjacencia_nao_dir import *
from bibgrafo.grafo_exceptions import *


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1', 'J', 'C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        # Grafos de teste DFS
        self.g_p_J = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_J.adicionaAresta('a1', 'J', 'C')
        self.g_p_J.adicionaAresta('a2', 'C', 'E')
        self.g_p_J.adicionaAresta('a4', 'C', 'P')
        self.g_p_J.adicionaAresta('a7', 'C', 'M')
        self.g_p_J.adicionaAresta('a8', 'M', 'T')
        self.g_p_J.adicionaAresta('a9', 'T', 'Z')

        self.g_p_P = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_P.adicionaAresta('a4', 'P', 'C')
        self.g_p_P.adicionaAresta('a1', 'C', 'J')
        self.g_p_P.adicionaAresta('a2', 'C', 'E')
        self.g_p_P.adicionaAresta('a7', 'C', 'T')
        self.g_p_P.adicionaAresta('a8', 'T', 'M')
        self.g_p_P.adicionaAresta('a9', 'T', 'Z')

        self.g_l11_A = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l11_A.adicionaAresta('a2', 'A', 'B')




        # Grafos test_caminhoDeEuler
        self.gHCDE_1 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])# 2 vertices de grau ímpar, Grafo do site
        self.gHCDE_1.adicionaAresta('a1', 'A', 'B')
        self.gHCDE_1.adicionaAresta('a2', 'A', 'C')
        self.gHCDE_1.adicionaAresta('a3', 'A', 'D')
        self.gHCDE_1.adicionaAresta('a4', 'A', 'F')
        self.gHCDE_1.adicionaAresta('a5', 'B', 'C')
        self.gHCDE_1.adicionaAresta('a6', 'B', 'E')
        self.gHCDE_1.adicionaAresta('a7', 'B', 'G')
        self.gHCDE_1.adicionaAresta('a8', 'E', 'F')
        self.gHCDE_1.adicionaAresta('a9', 'F', 'G')

        self.gHCDE_2 = MeuGrafo(['A', 'B', 'C'])# 2 vertices de grau ímpar
        self.gHCDE_2.adicionaAresta('a1', 'A', 'C')
        self.gHCDE_2.adicionaAresta('a2', 'B', 'C')

        self.gHCDE_3 = MeuGrafo(['A', 'B', 'C', 'D'])# 4 vertices de grau ímpar
        self.gHCDE_3.adicionaAresta('a1', 'A', 'C')
        self.gHCDE_3.adicionaAresta('a2', 'B', 'C')
        self.gHCDE_3.adicionaAresta('a3', 'D', 'C')

        self.gHCDE_4 = MeuGrafo(['A', 'B', 'C', 'D', 'E'])# 0 vertices de grau ímpar
        self.gHCDE_4.adicionaAresta('a1', 'A', 'C')
        self.gHCDE_4.adicionaAresta('a2', 'A', 'D')
        self.gHCDE_4.adicionaAresta('a3', 'D', 'C')
        self.gHCDE_4.adicionaAresta('a4', 'B', 'C')
        self.gHCDE_4.adicionaAresta('a5', 'B', 'E')
        self.gHCDE_4.adicionaAresta('a6', 'C', 'E')

        self.gHCDE_5 = MeuGrafo(['A', 'B', 'C'])# 0 vertices de grau ímpar
        self.gHCDE_5.adicionaAresta('a1', 'A', 'C')
        self.gHCDE_5.adicionaAresta('a2', 'B', 'C')
        self.gHCDE_5.adicionaAresta('a3', 'B', 'A')

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         ['J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z', 'M-Z'])
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), [])
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), [])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta duas vezes vez por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)


    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['a1']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['a7', 'a8']))
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), set(['a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), set(['asd']))
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse(self.g_p_sem_paralelas.eh_completo())
        self.assertTrue(self.g_c.eh_completo())
        self.assertTrue(self.g_c2.eh_completo())
        self.assertTrue(self.g_c3.eh_completo())
        self.assertFalse(self.g_l1.eh_completo())
        self.assertFalse(self.g_l2.eh_completo())
        self.assertFalse(self.g_l3.eh_completo())
        self.assertFalse(self.g_l4.eh_completo())
        self.assertFalse(self.g_l5.eh_completo())
    '''
        def test_dfs(self):
        self.assertEqual(self.g_p.dfs('J'), self.g_p_J)
        #self.assertEqual(self.g_p.dfs('P'), self.g_p_P)
        #self.assertEqual(self.g_l11_A.dfs('A'), self.g_l11_A) #teste, grafo com laço
    '''

    def test_conexo(self):
        self.assertTrue(self.g_p.conexo())
        self.assertFalse(self.g_d.conexo())

    def test_haCaminhoDeEuler(self):
        #Possui
        self.assertTrue(self.gHCDE_4.haCaminhoDeEuler())# 0 vertices de grau ímpar
        self.assertTrue(self.gHCDE_2.haCaminhoDeEuler())# 2 vertices de grau ímpar
        #NãoPossuihaCaminhoDeEuler
        self.assertFalse(self.gHCDE_3.haCaminhoDeEuler()) # 4 vertices de grau ímpar
        self.assertFalse(self.g_d.haCaminhoDeEuler()) #grafo desconexo

    def test_CaminhoDeEuler(self):
        self.assertEqual(self.gHCDE_1.caminhoDeEuler(), ['F', 'a4', 'A', 'a1', 'B', 'a6', 'E', 'a8', 'F',
                                                         'a9', 'G', 'a7', 'B', 'a5', 'C',
                                                         'a2', 'A', 'a3', 'D']) # 2 vertices de grau ímpar

        self.assertEqual(self.gHCDE_2.caminhoDeEuler(), ['B', 'a2', 'C', 'a1', 'A'])  # 2 vertices de grau ímpar


        self.assertEqual(self.gHCDE_4.caminhoDeEuler(), ['A', 'a1', 'C', 'a4', 'B', 'a5', 'E', 'a6', 'C',
                                                         'a3', 'D', 'a2', 'A']) # 0 vertices de grau ímpar

        self.assertEqual(self.gHCDE_5.caminhoDeEuler(), ['A', 'a3', 'B', 'a2', 'C',
                                                         'a1', 'A'])  # 0 vertices de grau ímpar

        # NãoPossuihaCaminhoDeEuler
        self.assertFalse(self.gHCDE_3.haCaminhoDeEuler())  # 4 vertices ímpares
        self.assertFalse(self.g_d.haCaminhoDeEuler())  # grafo desconexo