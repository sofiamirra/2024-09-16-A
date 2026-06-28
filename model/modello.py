from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMapSights = {}
        self._lista_archi = []

    def getShapes(self):
        return DAO.getAllShapes()

    def getValues(self):
        return DAO.getBorderValues()

    def buildGraph(self, shape, lat, lng):
        self._graph.clear()
        self._lista_archi.clear()
        self._idMapSights = {}
        nodes = DAO.getAllNodes(shape, lat, lng)
        self._graph.add_nodes_from(nodes)
        for s in nodes:
            self._idMapSights[s.id] = s
        allEdges = DAO.getAllEdges(shape, lat, lng, self._idMapSights)
        for e in allEdges:
            self._graph.add_edge(e.s1, e.s2, weight=e.peso)
            self._lista_archi.append(e)

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getTop5Archi(self):
        self._lista_archi.sort(key=lambda x: x.peso, reverse=True)
        return self._lista_archi[:5]

    def getTop5Nodi(self):
        nodes = list(self._graph.nodes)
        nodi_ordinati = sorted(nodes, key=lambda n: self._graph.degree(n), reverse=True)
        return nodi_ordinati[:5]
