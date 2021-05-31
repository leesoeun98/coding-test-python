from collections import deque


def isPrime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    else:
        return True


def BFS():
    while queue:
        cur = queue.popleft()
        if cur == second:
            print(visited[cur])
            return
        curnum = list(str(cur))
        for i in range(4):
            for j in range(1, 10):
                plusnext = int(''.join(curnum[:i] + [str(int(curnum[i]) + j)] + curnum[i + 1:]))
                if 1000 <= plusnext <= 9999 and visited[plusnext] == 0 and isPrime(plusnext):
                    visited[plusnext] = visited[cur] + 1
                    queue.append(plusnext)
                if int(curnum[i])-j>=0:
                    subnext = int(''.join(curnum[:i] + [str(int(curnum[i]) - j)] + curnum[i + 1:]))
                if 1000 <= subnext <= 9999 and visited[subnext] == 0 and isPrime(subnext):
                    visited[subnext] = visited[cur] + 1
                    queue.append(subnext)
    print("Impossible")


for _ in range(int(input())):
    first, second = map(int, input().split())
    visited = [0 for i in range(10000)]
    queue = deque()
    queue.append(first)
    BFS()
