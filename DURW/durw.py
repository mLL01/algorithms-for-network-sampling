from igraph import *
from sys import *
from random import uniform

class Arquivo(object):
    """ Manipulacao do arquivo """
    
    def abre_arquivo_leitura(self,arq):
        """ Abre arquivo para leitura """
        
        self.arquivo = open(arq, 'r')

    def n_vertices(self):
        """ Encontra no arquivo o numero de vertices """
        
        for linha in self.arquivo:
            aux = linha.split()
            if aux[1] == "Nodes:":
                return int(aux[2])
        self.arquivo.close()

    def n_arestas(self):
        """ Encontra no Arquivo o numero de arestas """
        
        for linha in self.arquivo:
            aux = linha.split()
            if aux[1] == "Edges:":
                return int(aux[2])
        self.arquivo.close()

    def le_arestas(self, n_arestas):
        """ Le todas as arestas de um grafo """
        
        arestas = []
        for linha in self.arquivo:
            aux = linha.split()
            if aux[0] != '#':
                aux1 = (int(aux[0]),int(aux[1]))
                arestas.append(aux1)
        self.arquivo.close()
        return arestas


class Grafo(Arquivo,Graph):
    """ Classe do grafo """
    
    def __init__(self,direcionado):
        """ Construtor da classe grafo"""
        
        if direcionado:
            #Python 2
            super(Graph,self).__init__(directed=True)
            
            #Python 3
            """ super().__init__(directed=direcionado) """

        elif not direcionado: 
            #Python 2
            super(Graph,self).__init__(directed=False)
            
            #Python 3
            """ super().__init__(directed=direcionado) """

    def total_arestas(self):
        """ Insere o numero total de arestas do grafo """
        
        self.n_arestas = self.arq1.n_arestas()

    def total_vertices(self):
        """ Insere o numero total de vertices do grafo """
        
        self.n_vertices = self.arq1.n_vertices()
        self.add_vertices(self.n_vertices)

    def adiciona_arestas(self):
        
        arestas = self.arq1.le_arestas(self.n_arestas)
        for u,v in arestas:
            self.add_edges([(u,v)])

    def cria_grafo_direcionado(self, arq):
        """ Cria um grafo direcionado com as entradas do arquivo """
        
        # temporario
        self.arq1 = Arquivo()
        self.arq1.abre_arquivo_leitura(arq)
        self.total_vertices()
        self.arq1.abre_arquivo_leitura(arq)
        self.total_arestas()
        self.arq1.abre_arquivo_leitura(arq)
        self.adiciona_arestas()
        

        
class Durw(Grafo):
    """ Implementacao do Directed Unbiased Random Walk """
    
    def distribuicao_uniforme(self):
        """ Calculo do "p" do algoritmo 2"""
        
        p.self = uniform(0,1)
    
    def __init__(self,arq):
        """ Cria o grafo direcionado referente ao arquivo de entrada """    

        self.grafo_direcionado = Grafo(True)
        self.grafo_direcionado.cria_grafo_direcionado(arq)
    
    def escolhe_budget(self):
        """ escolhe o orcamento como 10% do numero dos vertices """
        
        # code ...
    
    def gera_c(self):
        """ Temporario """
        
        return randint(0,50)

    def gera_w(self):
        """ Temporario """

        return randint(0,30)

    def escolhe_vd(self):
        """ Escolhe um vertice do grafo direcionado aleatoriamente """
        
        # code ...
    
    def escolhe_vu(self):
        """ Escolhe um vertice do grafo nao direcionado aleatoriamente """

        # code ...

    def grau_vertice(self):
        """ Retorna o grau do vertice """
        
        # code ...
    
    def add_vertice(self):
        """ Adiciona vertice ao grafo nao direcionado """

        # code ...

    def cria_grafo_undirected(self):
        """ Cria um grafo nao direcionado utilizando o "passeio aleatorio" """

        # code ...


sampled = Durw(argv[1])


