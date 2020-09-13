"""
Навигатор на сетке.
Дана плоская квадратная двумерная сетка (массив), на которой определена стоимость захода в каждую ячейку
(все стоимости положительные). Необходимо найти путь минимальной стоимости из заданной ячейки в заданную ячейку и
вывести этот путь.
"""
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
shape = (5, 7)
chess_board_ = np.random.randint(1, 10, (shape))


def calculate_paths(chess_board_):
    g = nx.Graph()
    M, N = chess_board_.shape
    for i in range(N):
        for j in range(M):
            g.add_node((j, i))
            if j - 1 > 0:
                g.add_weighted_edges_from([((j, i), (j - 1, i), chess_board_[j - 1, i])])
            if i - 1 > 0:
                g.add_weighted_edges_from([((j, i), (j, i - 1), chess_board_[j, i - 1])])
            if j + 1 < M and i <= N:
                g.add_weighted_edges_from([((j, i), (j + 1, i), chess_board_[j + 1, i])])
            if i + 1 < N and j <= M:
                g.add_weighted_edges_from([((j, i), (j, i + 1), chess_board_[j, i + 1])])

    # pos = nx.spring_layout(g)
    # nx.draw(g, pos, with_labels=True)
    # labels = {e: g.edges[e] for e in g.edges}
    # nx.draw_networkx_edge_labels(g, pos, edge_labels=labels, with_labels=True)
    # plt.show()
    dijkstra(g, stX=1, stY=1, X=3, Y=6)
    return g


def dijkstra(g, stX, stY, X, Y):
    diction = {}
    all_ways = []
    A = (X, Y)
    B = []

    starting_node = (stX, stY)
    for i in g.nodes:
        diction[i] = float("inf")

    diction[starting_node] = 0
    len_g = len(list(g.edges))
    exit_ = True

    while exit_:
        exit_ = False
        for i in range(len_g):
            k = list(g.edges)[i][0]  # from "A"
            h = list(g.edges)[i][1]  # to "B"
            if g[k][h]["weight"] + diction[k] < diction[h]:
                diction[h] = g[k][h]["weight"] + diction[k]
                # print(f"{diction[k]} + {g[k][h]['weight']} = {diction[h]} || {k} -> {h}")
                all_ways.append([k, h])
                exit_ = True
    while A != (stX, stY):
        for i in reversed(all_ways):
            if i[1] == A:
                # print(i[1])
                B.append([i[0], i[1]])
                A = i[0]

    print(chess_board_)
    print(f"Минимальная стоимость пути до точки {X, Y}: {diction[(X, Y)]}")
    print(f"Минимальный путь из вершины {A} в вершину {X, Y}:\n{B}")

