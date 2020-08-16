class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        p = [i for i in range(len(M))]
        self.count = len(M)
        for i in range(len(M) - 1):
            for j in range(i + 1, len(M)):
                if M[i][j] == 1:
                    v1 = self.parent(p, i)
                    v2 = self.parent(p, j)
                    self.union(p, v1, v2)
        return self.count

    def union(self, p, i, j):
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        if p1 != p2:
            self.count -= 1
        p[p1] = p2

    def parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:  # 路径压缩 ?
            x = i;
            i = p[i];
            p[x] = root
        return root