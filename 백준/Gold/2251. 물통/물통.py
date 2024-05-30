from collections import deque


def water_jug(A, B, C):
    visited = set()
    result = set()
    queue = deque([(0, 0, C)])

    while queue:
        a, b, c = queue.popleft()

        if (a, b, c) in visited:
            continue

        visited.add((a, b, c))

        if a == 0:
            result.add(c)

        # A -> B
        if a + b <= B:
            queue.append((0, a + b, c))
        else:
            queue.append((a - (B - b), B, c))

        # A -> C
        if a + c <= C:
            queue.append((0, b, a + c))
        else:
            queue.append((a - (C - c), b, C))

        # B -> A
        if b + a <= A:
            queue.append((b + a, 0, c))
        else:
            queue.append((A, b - (A - a), c))

        # B -> C
        if b + c <= C:
            queue.append((a, 0, b + c))
        else:
            queue.append((a, b - (C - c), C))

        # C -> A
        if c + a <= A:
            queue.append((c + a, b, 0))
        else:
            queue.append((A, b, c - (A - a)))

        # C -> B
        if c + b <= B:
            queue.append((a, c + b, 0))
        else:
            queue.append((a, B, c - (B - b)))

    return sorted(result)


A, B, C = map(int, input().split())
result = water_jug(A, B, C)
print(" ".join(map(str, result)))
