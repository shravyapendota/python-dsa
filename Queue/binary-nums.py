def generate_bin(n):
    result = []
    q = []
    q.append("1")
    
    for _ in range(n):
        temp = q.pop(0)
        result.append(temp)
        q.append(temp + "0")
        q.append(temp + "1")
    
    return result

n = int(input())
print(" ".join(generate_bin(n)))
