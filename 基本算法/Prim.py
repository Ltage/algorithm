# 算法导论P368 图23-5
from collections import defaultdict
from math import inf


class UnDirectedGraph:
    def __init__(self):
        self.graph = defaultdict(dict)

    # 添加边及权重
    def add_edge(self, point_one, point_two, weight):
        self.graph[point_one][point_two] = weight

    def __str__(self):
        return str(self.graph)

    def min_gen_tree(self):
        q = defaultdict(int)
        ans = defaultdict(list)
        for i in self.graph:
            q[i] = inf
        while q:
            u = min(q, key=lambda item: q[item])
            q.pop(u)

            # 遍历u的邻接点
            for v in self.graph[u]:
                # 如果该邻接点在队列q中，且v.key大于边(u,v)的权值
                if (v in q) and q[v] > self.graph[u][v]:
                    q[v] = self.graph[u][v]
                    ans[v] = u
        return ans


b = UnDirectedGraph()
b.add_edge("a", "b", 4)
b.add_edge("a", "h", 8)
b.add_edge("b", "h", 11)
b.add_edge("h", "i", 7)
b.add_edge("g", "h", 1)
b.add_edge("g", "i", 6)
b.add_edge("c", "i", 2)
b.add_edge("c", "b", 8)
b.add_edge("c", "f", 4)
b.add_edge("g", "f", 2)
b.add_edge("f", "e", 10)
b.add_edge("d", "e", 9)
b.add_edge("c", "d", 7)
b.add_edge("d", "f", 14)
print(b.min_gen_tree())
