edges = [
    ('A', 'B'),
    ('C', 'D'),
    ('E', 'E'),
    ('G', 'H'),
    ('I', 'J'),
    ('Z', 'Z')  
]

graph = {}

for u, v in edges:
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)  

print("Adjacency List:")
for node in graph:
    print(node, ":", graph[node])
