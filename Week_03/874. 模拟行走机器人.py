class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def distance(x,y):
            return x**2+y**2

        directions = {
            #direction:[[movement change],turn right,turn left]
            "N":[[0,1],"E","W"],
            "E":[[1,0],"S","N"],
            "S":[[0,-1],"W","E"],
            "W":[[-1,0],"N","S"]
        }
        obstacles = set(map(tuple, obstacles))
        cur_dir = "N"
        cur_pos = [0,0]
        max_dis = 0
        for command in commands:
            if command == -1:
                cur_dir = directions[cur_dir][1]
                continue
            if command == -2:
                cur_dir = directions[cur_dir][2]
                continue
            delta = directions[cur_dir][0]
            for _ in range(command):
                cur_pos[0]+=delta[0]
                cur_pos[1]+=delta[1]
                if (cur_pos[0],cur_pos[1]) in obstacles:
                    cur_pos[0]-=delta[0]
                    cur_pos[1]-=delta[1]
                    break
            dist = distance(cur_pos[0],cur_pos[1])
            max_dis = max(max_dis,dist)
        return max_dis