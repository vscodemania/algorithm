def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra(graph, costs, parents):
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)



# the graph
graph = {}                  # {}
graph["start"] = {}         # { "start": {} } 
graph["start"]["a"] = 6     # { "start": { "a": 6 } } 
graph["start"]["b"] = 2     # { "start": { "a": 6, "b": 2 } } 

graph["a"] = {}             # { "start": { "a": 6, "b": 2 }, "a": {} } 
graph["a"]["fin"] = 1       # { "start": { "a": 6, "b": 2 }, "a": { "fin": 1 } } 

graph["b"] = {}             # { "start": { "a": 6, "b": 2 }, "a": { "fin": 1 }, "b": {} } 
graph["b"]["a"] = 3         # { "start": { "a": 6, "b": 2 }, "a": { "fin": 1 }, "b": { "a": 3 } } 
graph["b"]["fin"] = 5       # { "start": { "a": 6, "b": 2 }, "a": { "fin": 1 }, "b": { "a": 3, "fin": 5 } } 

graph["fin"] = {}           # { "start": { "a": 6, "b": 2 }, "a": { "fin": 1 }, "b": { "a": 3, "fin": 5 }, "fin": {} } 

# the costs table
infinity = float("inf")     # int("inf") is NOT valid!
costs = {}                  # {}
costs["a"] = 6              # { "a": 6 }
costs["b"] = 2              # { "a": 6, "b": 2 }
costs["fin"] = infinity     # { "a": 6, "b": 2, "fin": infinity }

# the parents table
parents = {}                # {}
parents["a"] = "start"      # { "a": "start" }
parents["b"] = "start"      # { "a": "start", "b": "start" }
parents["fin"] = None       # { "a": "start", "b": "start", "fin": None }

dijkstra(graph, costs, parents)
print(costs)
print(parents)