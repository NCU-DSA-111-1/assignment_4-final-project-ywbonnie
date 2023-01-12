import numpy as np

inputmap = [["-", "-", "-", "*", "-"],
            ["-", "-", "*", "*", "-"],
            ["-", "*", "-", "-", "*"],
            ["*", "-", "*", "*", "-"],
            ["-", "-", "*", "*", "-"]]


class node:
    def __init__(self, s):
        self.data = s
        self.locate = [-1, -1]
        self.mark = "unvisited"
        self.next = [None, None, None, None] #[up, left, down, right]
        return

def build_map(Map):
    linkMap = []
    
    for i in range(len(Map)):
        tmpMap = []
        for j in range(len(Map[i])):
            tmpMap.append(node(Map[i][j]))
            tmpMap[j].locate = [i, j]
        linkMap.append(tmpMap)
        
    print(np.shape(linkMap))
    
    for i in range(len(Map)):
        for j in range(len(Map[i])): #[linkMap[i-1][j], linkMap[i][j-1], linkMap[i+1][j], linkMap[i][j+1]]
            if i-1 < 0:
                #print("{0}, {1}". format(i, j))
                if j-1 < 0:
                    linkMap[i][j].next = [None, None, linkMap[i+1][j], linkMap[i][j+1]]
                elif j+1 > len(Map[i])-1:
                    linkMap[i][j].next = [None, linkMap[i][j-1], linkMap[i+1][j], None]
                else:
                    linkMap[i][j].next = [None, linkMap[i][j-1], linkMap[i+1][j], linkMap[i][j+1]]
            elif i+1 > len(Map)-1:
                #print("{0}, {1}". format(i, j))
                if j-1 < 0:
                    linkMap[i][j].next = [linkMap[i-1][j], None, None, linkMap[i][j+1]]
                elif j+1 > len(Map[i])-1:
                    linkMap[i][j].next = [linkMap[i-1][j], linkMap[i][j-1], None, None]
                else:
                    linkMap[i][j].next = [linkMap[i-1][j], linkMap[i][j-1], None, linkMap[i][j+1]]
            else:
                #print("{0}, {1}". format(i, j))
                if j-1 < 0:
                    linkMap[i][j].next = [linkMap[i-1][j], None, linkMap[i+1][j], linkMap[i][j+1]]
                elif j+1 > len(Map[i])-1:
                    linkMap[i][j].next = [linkMap[i-1][j], linkMap[i][j-1], linkMap[i+1][j], None]
                else:
                    linkMap[i][j].next = [None, linkMap[i][j-1], linkMap[i+1][j], linkMap[i][j+1]]
    return linkMap

def dfs(start):
    if start is None:
        return
    if start.data == "*":
        return
    if start.mark == "visited":
        return
    start.mark = "visited"
    print("{0} is visited".format(start.locate))
    for i in range(4):
        dfs(start.next[i])
                    
linkmap = build_map(inputmap)

for i in range(len(linkmap)):
    for j in range(len(linkmap[i])):
        dfs(linkmap[i][j])

