# 差分约束系统 (Bellman-Ford)
# 算法导论P389 图24-8
from math import inf

# Adj
G = {
    "v0": ["v1", "v2", "v3", "v4", "v5"],
    "v1": ["v3", "v4"],
    "v2": ["v1"],
    "v3": ["v4", "v5"],
    "v4": ["v5"],
    "v5": ["v1", "v2"],
}

# Weight
W = {
    ("v0", "v1"): 0,
    ("v0", "v2"): 0,
    ("v0", "v3"): 0,
    ("v0", "v4"): 0,
    ("v0", "v5"): 0,
    ("v1", "v3"): 5,
    ("v1", "v4"): 4,
    ("v2", "v1"): 0,
    ("v3", "v4"): -1,
    ("v3", "v5"): -3,
    ("v4", "v5"): -3,
    ("v5", "v1"): -1,
    ("v5", "v2"): 1,
}


def BellmanFord():
    # 松弛操作
    def relax(u, v, w):
        if vertices[v] > vertices[u] + w:
            vertices[v] = vertices[u] + w

    # 初始化
    vertices = {}
    for vertex in G:
        vertices[vertex] = inf
    vertices["v0"] = 0

    # |V| - 1 次松弛
    for i in range(len(vertices) - 1):
        for edge in W:
            u, v = edge
            w = W[edge]
            relax(u, v, w)

    # 验证是否存在负环
    for edge in W:
        u, v = edge
        if vertices[v] > vertices[u] + W[edge]:
            return "Negative weight cycle exists."

    return vertices


print(BellmanFord())
