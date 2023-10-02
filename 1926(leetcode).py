from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dx = [1, 0, 0, -1]
        dy = [0, 1, -1, 0]
        visited = [[False for i in range(len(maze[0]))] for _ in range(len(maze))]
        visited[entrance[0]][entrance[1]] = True
        cnt = [[1000 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        cnt[entrance[0]][entrance[1]] = 0
        if len(maze) == 1 and len(maze[0]) == 1:
            return -1
        queue = deque()
        queue.append(entrance)
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if nx < 0 or nx > (len(maze) - 1) or ny < 0 or ny > (len(maze[0]) - 1):
                    continue
                if visited[nx][ny] == True:
                    continue
                if maze[nx][ny] == "+":
                    continue
                else:
                    visited[nx][ny] = True
                    cnt[nx][ny] = cnt[x][y] + 1
                    queue.append((nx, ny))
        answer = []

        for i in range(len(cnt)):
            for j in range(len(cnt[0])):
                if i == entrance[0] and j == entrance[1]:
                    continue
                if i == 0 or i == (len(cnt) - 1):
                    answer.append(cnt[i][j])
                if j == 0 or j == (len(cnt[0]) - 1):
                    answer.append(cnt[i][j])
                else:
                    continue

        return min(answer) if min(answer) != 1000 else -1
