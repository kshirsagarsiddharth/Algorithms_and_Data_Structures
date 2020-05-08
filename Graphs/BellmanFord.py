def bellman_ford(graph,source):
    # step 1: Prepare the distance and predecessor for each node
    distance,predecessor =dict(),dict()
    for node in graph:
        distance[node],predecessor[node] = float("inf"),None
    distance[source] = 0

    # step 2: relax the edges
    for i in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:
                # if the distance between the node and the neighbor is lower than the current, store it
                if distance[neighbor] >  distance[node] + graph[node][neighbor]:
                    distance[neighbor],predecessor[neighbor] = distance[node] + graph[node][neighbor],node

    # step 3: check for negative weight cycles
    for node in graph:
        for neighbor in graph[node]:
            assert distance[neighbor] <= distance[node] + graph[node][neighbor],"Negative weight cycle"
    return distance, predecessor


graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  3, 'd':  2, 'e':  2},
        'c': {},
        'd': {'b':  1, 'c':  5},
        'e': {'d': -3}
    }     