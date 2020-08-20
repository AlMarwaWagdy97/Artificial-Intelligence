from collections import defaultdict
import math
class Node:
    id = None  # Unique value for each node.
    up = None  # Represents value of neighbors (up, down, left, right).
    down = None
    left = None
    right = None
    previousNode = None  # Represents value of neighbors.
    edgeCost = None  # Represents the cost on the edge from any parent to this node.
    gOfN = None  # Represents the total edge cost
    hOfN = None  # Represents the heuristic value
    heuristicFn = None  # Represents the value of heuristic function

    def __init__(self, value):
        self.value = value


class SearchAlgorithms:
    ''' * DON'T change Class, Function or Parameters Names and Order
        * You can add ANY extra functions,
          classes you need as long as the main
          structure is left as is '''

    path = []  # Represents the correct path from start node to the goal node.
    fullPath = []  # Represents all visited nodes from the start node to the goal node.
    totalCost = -1  # Represents the total cost in case using UCS, AStar (Euclidean or Manhattan)
    n = Node(0)
    list = []
    board = []
    temp=[]
    collen=0
    rowlen=0
    # start = 0
    # end = 0
    # start2=0
    # end2=0
    length=0
    def __init__(self, mazeStr, edgeCost=None):
        ''' mazeStr containsmost node'''
        #p the full board


        self.m = mazeStr.split()
        self.collen = len(self.m)
        list1 = []



        for i in range(self.collen):
            list1.insert(i, self.m[i].split(','))
        for k in range (0,len(list1)):
            for i in list1[k]:
                self.list.append(i)
                self.temp.append(i)
        # for i in self.list:
        #     print (i)
        self.rowlen = len(list1[0])
        for i in range(len(list1)):
            for j in range(self.rowlen):
                self.board.append(Node(j))


        #print(self.list)
        self.length=len(self.list)
        count = 0
        for i in range (0,len(self.list)):
            self.board[i].id = count
            count += 1

            if ((i % self.rowlen) != (self.rowlen-1)) and (self.list[i+1] != '#'):
                self.board[i].right = self.board[i].id +1
                #self.board[i].
            if ((i %self. rowlen) != 0 ) and (self.list[i-1] != '#'):
                self.board[i].left =  self.board[i].id -1
            if (i  > self.rowlen  ) and (self.list[i-self.rowlen] != '#'):
                self.board[i].up =  self.board[i].id - self.rowlen
            if ((i + self.rowlen) < len(self.list)) and (self.list[i+self.rowlen] != '#'):
                self.board[i].down = self.board[i].id + self.rowlen
        if edgeCost != None:
            for i in range (0,len(edgeCost)):
                self.board[i].edgeCost = edgeCost[i]
                self.board[i].heuristicFn = math.inf



            # if (self.list[i] == 'S'):
            #     self.start = self.board[i].id
            #    # self.start2=self.board[i].id
            # if (self.list[i] == 'E'):
            #     self.end = self.board[i].id
                #self.end2=self.board[i].id


       # for i in range (0,len(self.list)):
            #print(self.board[i].id)
       # print(self.board[0][0])
    #/////////////////////////////////////////////////////////////DFS//////////////////////////////////////////////////////////////////////////////////////////////////
    def DFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        start=None
        end=None
        self.fullPath=[]
        start = self.list.index('S')
        #print(start)
        end = self.list.index('E')
        #print(end)
        size=self.rowlen*self.collen
        #print (size)


        vist = []
        path = []
        stack = [start]
        #stack.append(start)
        #vist.append(start)
        count = 0
        self.board[start].previousNode = -1
        while len(stack)!=0:
            x = stack[count]
            #print(vist)
            #print(x)
            #
            y = stack.pop(count)
            count -= 1


            if x <=size-1:

                vist.append(x)
                if (self.board[x].left != None  and  self.board[x].left not in vist and self.board[x].left not in stack):
                    stack.insert(count + 1, self.board[x].left)
                    # vist.append(self.board[x].left)
                    self.board[self.board[x].left].previousNode = x
                    count += 1
                if (self.board[x].right != None  and self.board[x].right not in vist and self.board[x].right not in stack ):
                    stack.insert(count+1,self.board[x].right)
                    self.board[self.board[x].right].previousNode = x
                    count += 1
                if (self.board[x].down != None  and  self.board[x].down not in vist and self.board[x].down not in stack):
                    stack.insert(count + 1, self.board[x].down)
                    # vist.append(self.board[x].down)
                    self.board[self.board[x].down].previousNode = x
                    count += 1
                if (self.board[x].up != None  and  self.board[x].up not in  vist and self.board[x].up not in stack  ):
                    stack.insert(count+1,self.board[x].up)
                    self.board[self.board[x].up].previousNode = x
                    count += 1
                    #vist.append(self.board[x].up)

                if x == end:
                    break

        self.fullPath = vist
        return self.path, self.fullPath

    #/////////////////////////////////////////////////////////BFS/////////////////////////////////////////////////////////////////////////////////////////////////
    def BFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        start = self.list.index('S')
        #print(start)
        end = self.list.index('E')
        #print(end)
        self.fullPath = []
        vist = []
        path = []
        queue = [start]
        count = 0
        #print(self.start)
       # print(self.end)
        self.board[start].previousNode = -1
        while queue !=[] :
            #x = self.start
            x=queue[count]
            vist.append(x)
            # print(vist)
            # print(x)


            if x == end:
                break

            queue.pop(count)
            count -= 1

            if (self.board[x].up != None and not self.board[x].up  in vist):
                queue.insert(0, self.board[x].up)
                self.board[self.board[x].up].previousNode = x
                count += 1
            if (self.board[x].down != None and not  self.board[x].down  in vist):
                queue.insert(0, self.board[x].down)
                self.board[self.board[x].down].previousNode = x
                count += 1
            if (self.board[x].right != None and not self.board[x].right  in vist):
                self.board[self.board[x].right].previousNode = x
                queue.insert(0, self.board[x].right)
                count += 1
            if (self.board[x].left != None and not self.board[x].left in vist):
                queue.insert(0, self.board[x].left)
                self.board[self.board[x].left].previousNode = x
                count += 1
        # shortpath = []
        # endindex = end
        # while self.board[endindex].previousNode != -1 and self.board[endindex].previousNode not in vist:
        #     shortpath.append(self.board[endindex].id)
        #     endindex = self.board[endindex].previousNode
        #     shortpath.append(start)
        # shortpath.reverse()
        # self.path = shortpath
        self.fullPath = vist
        self.fullPath=list(dict.fromkeys(self.fullPath))

        #print(len(vist))
       # self.board.clear()

        return self.path, self.fullPath
    #///////////////////////////////////////////////////////////////////UCS////////////////////////////////////////////////////////////////////////////////////////////
    def UCS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        return self.path, self.fullPath, self.totalCost
    #//////////////////////////////////////////////////////////////////A*////////////////////////////////////////////////////////////////////////////////////////////
    def AStarEuclideanHeuristic(self):
        # Cost for a step is calculated based on edge cost of node
        # and use Euclidean Heuristic for evaluating the heuristic value
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        start = self.list.index('S')
        end = self.list.index('E')
        colend = self.board[end].id % self.rowlen
        rowend = int(self.board[end].id / self.rowlen)
        #print(colend)
        #print (rowend)
        visit = []
        queue = [start]
        count = 0;
        cost = 0
        size = self.collen * self.rowlen
        self.board[start].heuristicFn = 0
        self.board[start].gOfN = self.board[start].edgeCost
        while queue != []:
            less = 0
            index = -1
            for i in range(0, len(queue)):
                if (self.board[i].heuristicFn < less):
                    less = self.board[i].heuristicFn
                    index = i;
                #print(self.board[i].heuristicFn)
            x = queue[index]
            if x == end:
                break
            #cost += self.board[i].edgeCost
            #if self.board[x].gOfN  == None:
                #self.board[x].gOfN = self.board[x].edgeCost
            queue.remove(x)
            #print (queue)
            count -= 1
            if x <= size - 1:
                visit.append(x)
                if (self.board[x].up != None and self.board[x].up not in queue and  self.board[self.board[x].up].id <size):

                    self.board[self.board[x].up].previousNode = x
                    colchild = self.board[self.board[x].up].id % self.rowlen
                    rowchild = int(self.board[self.board[x].up].id / self.rowlen)
                    hn   = int(math.pow((colend - colchild),2) + math.pow((rowend-rowchild),2))
                    gn   = float(float(self.board[x].gOfN or 0) + float(self.board[self.board[x].up].edgeCost))
                    ghn = hn + gn
                    if self.board[x].up  in visit:
                        if self.board[self.board[x].up].heuristicFn < ghn:
                            self.board[self.board[x].up].hOfN = hn
                            self.board[self.board[x].up].gOfN= gn
                            self.board[self.board[x].up].heuristicFn = ghn
                    else:
                        self.board[self.board[x].up].hOfN = hn
                        self.board[self.board[x].up].gOfN = gn
                        self.board[self.board[x].up].heuristicFn = ghn
                        queue.insert(count + 1, self.board[x].up)
                        count += 1

                if (self.board[x].right != None and  self.board[x].right not in queue and self.board[self.board[x].right].id <size):

                    self.board[self.board[x].right].previousNode = x
                    colchild = self.board[self.board[x].right].id % self.rowlen
                    rowchild = int(self.board[self.board[x].right].id / self.rowlen)
                    hn = int(math.pow((colend - colchild), 2) + math.pow((rowend - rowchild), 2))
                    gn = float(float(self.board[x].gOfN or 0) + float(self.board[self.board[x].right].edgeCost))
                    ghn = hn + gn
                    if self.board[x].right in visit:
                        if self.board[self.board[x].right].heuristicFn < ghn:
                            self.board[self.board[x].right].hOfN = hn
                            self.board[self.board[x].right].gOfN = gn
                            self.board[self.board[x].right].heuristicFn = ghn
                    else:
                        self.board[self.board[x].right].hOfN = hn
                        self.board[self.board[x].right].gOfN = gn
                        self.board[self.board[x].right].heuristicFn = ghn
                        queue.insert(count + 1, self.board[x].right)
                        count += 1

                if (self.board[x].down != None  and self.board[x].down not in queue and self.board[self.board[x].down].id <size):

                    self.board[self.board[x].down].previousNode = x
                    colchild =int (self.board[self.board[x].down].id % self.rowlen)
                    rowchild = int(self.board[self.board[x].down].id / self.rowlen)
                    hn = int(math.pow((colend - colchild), 2) + math.pow((rowend - rowchild), 2))
                    gn = float(float(self.board[x].gOfN or 0) + float(self.board[self.board[x].down].edgeCost))
                    ghn = hn + gn
                    if self.board[x].down in visit:
                        if self.board[self.board[x].down].heuristicFn < ghn:
                            self.board[self.board[x].down].hOfN = hn
                            self.board[self.board[x].down].gOfN = gn
                            self.board[self.board[x].down].heuristicFn = ghn
                    else:
                        self.board[self.board[x].down].hOfN = hn
                        self.board[self.board[x].down].gOfN = gn
                        self.board[self.board[x].down].heuristicFn = ghn
                        queue.insert(count + 1, self.board[x].down)
                        count += 1

                # and self.board[x].left not in stack
                if (self.board[x].left != None  and self.board[x].left not in queue and self.board[self.board[x].left].id <size):

                    self.board[self.board[x].left].previousNode = x
                    colchild = self.board[self.board[x].left].id % self.rowlen
                    rowchild = int(self.board[self.board[x].left].id / self.rowlen)
                    hn = int(math.pow((colend - colchild), 2) + math.pow((rowend - rowchild), 2))
                    gn = float(float(self.board[x].gOfN or 0) + float(self.board[self.board[x].left].edgeCost))
                    ghn = hn + gn
                    if self.board[x].left in visit:
                        if self.board[self.board[x].left].heuristicFn < ghn:
                            self.board[self.board[x].left].hOfN = hn
                            self.board[self.board[x].left].gOfN = gn
                            self.board[self.board[x].left].heuristicFn = ghn
                    else:
                        self.board[self.board[x].left].hOfN = hn
                        self.board[self.board[x].left].gOfN = gn
                        self.board[self.board[x].left].heuristicFn = ghn
                        queue.insert(count + 1, self.board[x].left)
                        count += 1
            if x == end:
                break
        visit.append(end)
        self.fullPath = visit
        self.totalCost = self.board[end].gOfN
        return self.path, self.fullPath, self.totalCost
    #///////////////////////////////////////////////////////////////A*///////////////////////////////////////////////////////////////////////////////////////////////
    def AStarManhattanHeuristic(self):
        # Cost for a step is 1
        # and use ManhattanHeuristic for evaluating the heuristic value
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        start = self.list.index('S')
        end = self.list.index('E')
        colend = self.board[end].id % self.rowlen
        rowend = int(self.board[end].id / self.rowlen)
        # print(colend)
        # print (rowend)
        visit = []
        queue = [start]
        count = 0;
        cost = 0
        size = self.collen * self.rowlen
        self.board[start].heuristicFn = 0
        self.board[start].gOfN = self.board[start].edgeCost
        while queue != []:
            less = 0
            index = -1
            for i in range(0, len(queue)):
                if (self.board[i].heuristicFn < less):
                    less = self.board[i].heuristicFn
                    index = i;
                # print(self.board[i].heuristicFn)
            x = queue[index]
            if x == end:
                break
            # cost += self.board[i].edgeCost
            # if self.board[x].gOfN  == None:
            # self.board[x].gOfN = self.board[x].edgeCost
            queue.remove(x)
            # print (queue)
            count -= 1
            if x <= size - 1:
                visit.append(x)
                if (self.board[x].up != None and self.board[x].up not in queue and self.board[
                    self.board[x].up].id < size):

                    self.board[self.board[x].up].previousNode = x
                    colchild = self.board[self.board[x].up].id % self.rowlen
                    rowchild = int(self.board[self.board[x].up].id / self.rowlen)
                    hn = int(math.pow((colend - colchild), 2) + math.pow((rowend - rowchild), 2))
                    gn = float(float(self.board[x].gOfN or 0) + float(self.board[self.board[x].up].edgeCost))
                    ghn = hn + gn
                    if self.board[x].up in visit:
                        if self.board[self.board[x].up].heuristicFn < ghn:
                            self.board[self.board[x].up].hOfN = hn
                            self.board[self.board[x].up].gOfN = gn
                            self.board[self.board[x].up].heuristicFn = ghn
                    else:
                        self.board[self.board[x].up].hOfN = hn
                        self.board[self.board[x].up].gOfN = gn
                        self.board[self.board[x].up].heuristicFn = ghn
                        queue.insert(count + 1, self.board[x].up)
                        count += 1

                if (self.board[x].right != None and self.board[x].right not in queue and self.board[
                    self.board[x].right].id < size):

                    self.board[self.board[x].right].previousNode = x
                    colchild = self.board[self.board[x].right].id % self.rowlen
                    rowchild = int(self.board[self.board[x].right].id / self.rowlen)
                    hn = int(math.pow((colend - colchild), 2) + math.pow((rowend - rowchild), 2))
                    gn = float(float(self.board[x].gOfN or 0) + float(self.board[self.board[x].right].edgeCost))
                    ghn = hn + gn
                    if self.board[x].right in visit:
                        if self.board[self.board[x].right].heuristicFn < ghn:
                            self.board[self.board[x].right].hOfN = hn
                            self.board[self.board[x].right].gOfN = gn
                            self.board[self.board[x].right].heuristicFn = ghn
                    else:
                        self.board[self.board[x].right].hOfN = hn
                        self.board[self.board[x].right].gOfN = gn
                        self.board[self.board[x].right].heuristicFn = ghn
                        queue.insert(count + 1, self.board[x].right)
                        count += 1

                if (self.board[x].down != None and self.board[x].down not in queue and self.board[
                    self.board[x].down].id < size):

                    self.board[self.board[x].down].previousNode = x
                    colchild = int(self.board[self.board[x].down].id % self.rowlen)
                    rowchild = int(self.board[self.board[x].down].id / self.rowlen)
                    hn = int(abs(colend - colchild) + abs(rowend - rowchild))
                    gn = float(float(self.board[x].gOfN or 0) + float(self.board[self.board[x].down].edgeCost))
                    ghn = hn + gn
                    if self.board[x].down in visit:
                        if self.board[self.board[x].down].heuristicFn < ghn:
                            self.board[self.board[x].down].hOfN = hn
                            self.board[self.board[x].down].gOfN = gn
                            self.board[self.board[x].down].heuristicFn = ghn
                    else:
                        self.board[self.board[x].down].hOfN = hn
                        self.board[self.board[x].down].gOfN = gn
                        self.board[self.board[x].down].heuristicFn = ghn
                        queue.insert(count + 1, self.board[x].down)
                        count += 1

                # and self.board[x].left not in stack
                if (self.board[x].left != None and self.board[x].left not in queue and self.board[
                    self.board[x].left].id < size):

                    self.board[self.board[x].left].previousNode = x
                    colchild = self.board[self.board[x].left].id % self.rowlen
                    rowchild = int(self.board[self.board[x].left].id / self.rowlen)
                    hn = int(abs(colend - colchild) + abs(rowend - rowchild))
                    gn = float(float(self.board[x].gOfN or 0) + float(self.board[self.board[x].left].edgeCost))
                    ghn = hn + gn
                    if self.board[x].left in visit:
                        if self.board[self.board[x].left].heuristicFn < ghn:
                            self.board[self.board[x].left].hOfN = hn
                            self.board[self.board[x].left].gOfN = gn
                            self.board[self.board[x].left].heuristicFn = ghn
                    else:
                        self.board[self.board[x].left].hOfN = hn
                        self.board[self.board[x].left].gOfN = gn
                        self.board[self.board[x].left].heuristicFn = ghn
                        queue.insert(count + 1, self.board[x].left)
                        count += 1
            if x == end:
                break
        visit.append(end)
        self.fullPath = visit
        self.totalCost = self.board[end].gOfN


        return self.path, self.fullPath, self.totalCost
    #////////////////////////////////////////////////////////////////////MAIN///////////////////////////////////////////////////////////////////////////////////////
def main():
    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.BFS()
    print('**BFS**\nPath is: ' + str(path) + '\nFull Path is:s ' + str(fullPath) + '\n\n')
            ############################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.DFS()
    print('**DFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')

                ######################################################################################



    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.', [0, 15, 2, 100, 60, 35, 30, 3
                                                                                                             , 100, 2, 15, 60, 100, 30, 2
                                                                                                             , 100, 2, 2, 2, 40, 30, 2, 2
                                                                                                             , 100, 100, 3, 15, 30, 100, 2
                                                                                                             , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = searchAlgo.UCS()
    print('** UCS **\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\nTotal Cost: ' + str(
        TotalCost) + '\n\n')
               #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.', [0, 15, 2, 100, 60, 35, 30, 3
                                                                                                             , 100, 2, 15, 60, 100, 30, 2
                                                                                                             , 100, 2, 2, 2, 40, 30, 2, 2
                                                                                                             , 100, 100, 3, 15, 30, 100, 2
                                                                                                             , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = searchAlgo.AStarEuclideanHeuristic()
    print('**ASTAR with Euclidean Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')

            #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath, TotalCost = searchAlgo.AStarManhattanHeuristic()
    print('**ASTAR with Manhattan Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')


main()
