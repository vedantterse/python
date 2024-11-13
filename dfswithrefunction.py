from collections import deque
# this is function of algorithm which is used for competitive programming.
# this algorithm is often used for "minimam road problem"
# this algorithm is witten in sevral ways, but this time I'll write with queue
# dfs is combination of 3 words : breadth first saerch

# Assuming the plobrem is about "minimam road problem in grid".
# 1 is block which people couldn't walk
grid = [
    [0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1],
    [1,1,1,0,0,1,0],
    [1,0,0,0,1,1,1],
    [0,0,1,1,1,0,0],
    [0,1,1,1,0,1,0],
    [0,1,1,0,0,0,0],
]

def dfs(grid):
    dx=[0,1,0,-1]
    dy=[-1,0,1,0]

    start = 0
    goal  = 0
    # make start and goal with 0 indexed number also 1 gen number ex:) (1,5)=1*6+5=11, (2,3)=2*6+3 = 15
    
    disatnce = [-1]*(7*7)

    seen = [0]*(7*7)
    # make seen which shows whether this point has already been searched

    q = deque()
    q.append(0)

    disatnce[start] = 0
    while(len(q)>0):
        now = q.popleft()

        # any function

        for i in 4:
            nextx = now/6
            nexty = now%6
            if nextx>=6 or nextx<0 or nexty>=6 or nexty<0 or grid[nextx][nexty]==1:
                continue
            q.append(nextx*6+nexty)
        # this "for" can append points for 4 directions into queue

# this is just inistance. there alo ways to code in the world.
# you can solve it with tree,grid,and strings.
# you should check it
            



