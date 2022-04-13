from search import EightPuzzle, astar_search, breadth_first_graph_search, depth_first_graph_search

puzInit = (1, 2, 3, 5, 7, 4, 8, 6, 0)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

eight_puzzle = EightPuzzle(puzInit, goal)

#A* search
print("A* search")
print(astar_search(eight_puzzle, h=None, display=True).solution())

#Breadth first
print("Breadth first")
print(breadth_first_graph_search(eight_puzzle, display=True))

#Depth first
#print("Depth first")
#print(depth_first_graph_search(eight_puzzle, display=True))


