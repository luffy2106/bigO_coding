"""
Nhận xét : 
Bài toán có thể được chuyển về thành:
- Sau khi duyệt xong Flowd Warshall, phần tử nào có đường đi với độ dài bằng 2 đến nhiều đỉnh nhất sẽ là đáp án.
"""

def FloydWarShall(dist, V):
    for k in range(V):
        for i in range(V):
            # if dist[i][k] == INF:
            #     continue
            if j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return


def Floyd(dist):
    minId, maxCount = 0,0
    for i in range(M):
        count = 0
        for j in range(M):
            if dist[i][j] == 2:
                count+=1
        if (count > maxCount): 
            maxCount = count
            minId = i
        elif (count == maxCount and i < minId):
            maxCount = count
            minId = i
    return minId, maxCount


INF = 10 ** 9
T = int(input())
for t in range(T):
    first_line = [c for c in input()]
    M =  len(first_line)
    dist = [[INF for m in range(M)] for i in range(M)]
    for i in range(M):
        if i == 0:
            for j in range(len(first_line)):
                if first_line[j] == "Y":
                    dist[i][j] = 1
        else:
            line_i = [c for c in input()]
            for u in range(len(line_i)):
                if line_i[u] == "Y":
                    dist[i][u] = 1
    FloydWarShall(dist, M)
    id, count = Floyd(dist)
    print(str(id)+" "+str(count))

         