class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        n = len(board)
        m = len(board[0])
        x, y = click[0], click[1]
        directions = [-1, 0, 1]

        def dfs(x, y):
            if board[x][y] == "M":
                board[x][y] = "X"
                return
            if board[x][y] == "E":
                # check surrounding num of mine
                count = 0
                for x_dir in directions:
                    for y_dir in directions:
                        if not (x_dir, y_dir) == (0, 0):
                            nex_x, nex_y = x + x_dir, y + y_dir
                            if 0 <= nex_x < n and 0 <= nex_y < m:
                                if board[nex_x][nex_y] == "M":
                                    count += 1
                if count > 0:
                    board[x][y] = str(count)
                    # we must return in this step!!! Otherwise we gona hit the Mine!
                    return
                else:
                    board[x][y] = "B"
                # dfs for the neighbours
                for x_dir in directions:
                    for y_dir in directions:
                        if not (x_dir, y_dir) == (0, 0):
                            nex_x, nex_y = x + x_dir, y + y_dir
                            if 0 <= nex_x < n and 0 <= nex_y < m:
                                dfs(nex_x, nex_y)
            else:
                return

        dfs(x, y)
        return board