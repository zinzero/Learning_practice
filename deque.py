from collections import deque

graph = [[0, 1], [3, 4]]
que = deque([1])

p = que.popleft()
print(p)