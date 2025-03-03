
import heapq

class GRAPH:
    def __init__(self):
        self.adj_list = {}


    def adding_Edge(self, x,y,d):
        if x not in self.adj_list:
            self.adj_list[x] = []
        if y not in self.adj_list:
            self.adj_list[y] = []
        self.adj_list[x].append((y,d))
        #self.adj_list[y].append((x,d)) # this is for undirected graphs..


    def find_neighbors(self,state):
        neighbors = []
        if state in self.adj_list:
            for neighbor in self.adj_list[state]:
                neighbors.append(neighbor)
        return neighbors


    def display_Graph(self):
        for node in self.adj_list:
            print(node,'->', self.adj_list[node])


    def AstarAlgo(self, start, goal, heuristic):
        pq = []
        heapq.heappush(pq,(0,start))
        path1 = {}
        pathWeight = {}
        a_starValue = {}

        for node in self.adj_list:
            pathWeight[node] = float('inf')
            a_starValue[node] = float('inf')
        pathWeight[start] = 0
        a_starValue[start] = heuristic[start]

        while pq:
            _, curState = heapq.heappop(pq)

            if curState == goal:
                path2 = []
                while curState in path1:
                    path2.append(curState)
                    curState = path1[curState]
                path2.append(start)
                opt_path = ""
                for i in range(len(path2)-1, -1, -1):
                    opt_path += "->" + str(path2[i])
                return opt_path[2::], pathWeight[goal]
            for n, w in self.find_neighbors(curState):
                heu_sum = pathWeight[curState] + w
                if heu_sum < pathWeight[n]:
                    path1[n] = curState
                    pathWeight[n] = heu_sum
                    a_starValue[n] = pathWeight[n] + heuristic.get(n,float('inf'))
                    heapq.heappush(pq,(a_starValue[n],n))
        return None



#input files
grp = GRAPH()
heuristic = {}
inputFile = open('A_star input.txt', 'r')
stateData = inputFile.readlines()
for states in stateData:
    divideCity = states.split(' ')
    state = divideCity[0]
    heuristic[state] = int(divideCity[1])
    for i in range(2,len(divideCity),2):
        neighbors = divideCity[i]
        weight = int(divideCity[i+1])
        grp.adding_Edge(state,neighbors,weight)

#grp.display_Graph()

start_state = input("Enter from where you want to start your journey: ")
goal_state = "Bucharest"

final_path, cost = grp.AstarAlgo(start_state,goal_state,heuristic)
print(f"Optimal path from {start_state} to {goal_state} :", final_path)
print(f"Cost: {cost}")
