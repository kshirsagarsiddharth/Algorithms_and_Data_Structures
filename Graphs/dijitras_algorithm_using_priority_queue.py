import heapq

def calculate_distances(graph,starting_vertex):
    distances = {vertex : float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    priority_queue = [(0,starting_vertex)]
    while len(priority_queue) > 0:
        current_distance,current_vertex = heapq.heappop(priority_queue)
        # nodes are added to the priority queue multiple times but we only process thiose nodes which have less distance and other are discarded
        if current_distance > distances[current_vertex]:
            continue
        for neighbour,weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(priority_queue,(distance,neighbour))
    return distances

example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}