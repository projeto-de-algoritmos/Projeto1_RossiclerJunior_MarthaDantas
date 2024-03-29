# libraries
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def bfs(self):
        visited_vertex = []
        visited_edges = []
        queue = []
        for vertex in self.__graph_dict.items():
            if vertex[0] not in visited_vertex:
                queue.append(vertex[0])
                visited_vertex.append(vertex[0])
                while len(queue) > 0:
                    u = queue.pop(0)
                    for v in vertex[1]:
                        if v not in visited_vertex:
                            visited_edges.append(v + "-" + u)
                            visited_vertex.append(v)
                            queue.append(v)
        
        print("BFS(G):")
        print("Visited vertex: " + str(visited_vertex))
        print("Visited edges: " + str(visited_edges))
        return None

    def __graph_to_arrays(self):
        graph = {
            "from": [],
            "to": [],
            "values": []
        }

        for node in self.__graph_dict.keys():
            for connection in self.__graph_dict[node]:
                graph['from'].append(connection)
                graph['to'].append(node)
                graph['values'].append(5)
        return graph

    def draw_graph(self):
        graph = self.__graph_to_arrays()
        df = pd.DataFrame({ 'from': graph['from'], 'to': graph['to'], 'value': graph['values']})
        G=nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.Graph())
        # nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_color=df['value'], width=10.0, edge_cmap=plt.cm.Blues)
        nx.draw(G, with_labels=True)
        plt.show()


if __name__ == "__main__":
    g = {
        "a": ["d", "f", "e"],
        "b": ["c"],
        "c": ["b", "c", "d", "e"],
        "d": ["a", "c"],
        "e": ["c"],
        "f": []
    }
    
    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("Add vertex:")
    graph.add_vertex("z")

    print("Vertices of graph:")
    print(graph.vertices())
 
    print("Add an edge:")
    graph.add_edge({"a","z"})
    
    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge({"x","y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())

    graph.bfs()
    graph.draw_graph()
