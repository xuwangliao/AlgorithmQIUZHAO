class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        self.result = []
        self.pie = set()
        self.na = set()
        self.col = set()

        def dfs(i, temp):
            if i == n:
                self.result.append(temp[:])
                return
            for j in range(n):
                if j not in self.col and (i + j) not in self.pie and (j - i) not in self.na:
                    self.col.add(j)
                    self.pie.add(i + j)
                    self.na.add(j - i)
                    temp.append(j)
                    dfs(i + 1, temp)
                    self.col.remove(j)
                    self.pie.remove(i + j)
                    self.na.remove(j - i)
                    temp.pop()

        dfs(0, [])
        return self.generate_result(self.result)

    def generate_result(self, n):
        board = []
        for sol in n:
            solution = []
            for j in sol:
                solution.append('.' * j + 'Q' + '.' * (len(sol) - j - 1))
            board.append(solution)
        return board