#定义马行走的每个方向
dx = [1, 1,-1,-1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, -1, 1]

def bfs(n, m):
	#先定义每个点是否访问过
	vis = [([0]*(m+1)) for i in range(n+1)]
	q = [(0, 0, 0)]
	vis[0][0] = 1
	step = 0xFFFFFFF
	while q:
		temp = q.pop(0)
		if temp[0] == n and temp[1] == m:
			if temp[2] < step:
				step = temp[2]
		for x, y in zip(dx, dy):
			curx = temp[0] + x
			cury = temp[1] + y
			if curx > n or cury > m or curx < 0 or cury < 0 or vis[curx][cury]:
				continue
			vis[curx][cury] = 1
			curstep = temp[2] + 1

			q.append((curx, cury,curstep))
	return -1 if step == 0xFFFFFFF else step

print(bfs(2, 2))