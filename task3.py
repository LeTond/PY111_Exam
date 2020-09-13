"""
Назовем связным такой граф, в котором есть путь от любой вершины к любой другой вершине.
Дан граф, состоящий из 2+ связных подграфов, которые не связаны между собой.
Задача: посчитать число компонент связности графа, т.е. количество таких подграфов.
Картинки по запросу число компонент связности
В графе на картинке – три подграфа, т.е. число компонент связности = 3.

"""

import networkx as nx

counter = 0
list2 = []
graph = nx.Graph()
graph.add_nodes_from("ABCDEFGHIJ")
graph.add_edges_from([
    ('B', 'G'),
    ('F', 'G'),
    ('G', 'C'),
    ('G', 'H'),
    ('G', 'I'),
    ('C', 'H'),
    ('I', 'H'),
    ('H', 'J'),
    ('E', 'D'),
])
len_graph = graph.number_of_nodes()


def freedom(start_node, list2, g=graph):
    list_ = list(g.neighbors(start_node))
    if len(list_) == 0:
        list2.append(start_node)
    else:
        while list_ != []:
            if len(list_) > 0:
                if list_[0] not in list2:
                    list2.append(list_[0])
                    list_ += list(g.neighbors(list_[0]))
                list_.remove(list_[0])


def componenti_svyaznosti(counter):
    i = 0
    while len(list2) < len_graph:
        start_node = list(graph.nodes)[i]
        if start_node not in list2:
            freedom(start_node, list2, graph)
            counter += 1
        else:
            i += 1
    print(f" Число компонент связности: {counter}")

