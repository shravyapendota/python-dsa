def interleave_queue_elements(queue):
    n = len(queue) // 2
    first_half = queue[:n]
    second_half = queue[n:]
    result = []

    for i in range(n):
        result.append(first_half[i])
        result.append(second_half[i])

    return result

queue = [1, 2, 3, 4, 5, 6]
print(interleave_queue_elements(queue))
