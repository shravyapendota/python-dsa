v = int(input("Vertices: "))
e = int(input("Edges: "))
adj_matrix = [[0 for _ in range(v)] for _ in range(v)]

for _ in range(e):
    u, w = map(int, input().split())
    
    if u >= v or w >= v or u < 0 or w < 0:
        print("Invalid edge:", u, w)
        continue

    adj_matrix[u][w] = 1
    adj_matrix[w][u] = 1

print("\nAdjacency Matrix:")
for row in adj_matrix:
    print(" ".join(map(str, row)))
