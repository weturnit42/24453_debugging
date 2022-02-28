N, M = input().split()
arr = list(map(int, input().split()))
X, Y = input().split()

line = list(range(1, int(N)+1))
errorCount = int(Y)

for i in line:
    if(i in arr):
        line[i-1] = [int(line[i-1]), -1]
    else:
        line[i-1] = [int(line[i-1]), 1]

for i in range(len(line)):
    if(line[i][1] == -1):
        line[i][1] = 1
        errorCount = errorCount-1
    
    if(errorCount == 0):
        break

nonErrorCount = int(X)
count = 0
havetoFixCount = 0

for i in range(len(line)):
    for j in range(i, len(line)):
        if(line[j][1] == 1):
            count = count + 1
        else:
            count = 0
            break
        if(count == nonErrorCount):
            break
    if(count == nonErrorCount):
        for k in range(j, len(line)):
            if(line[k][1] == -1):
                havetoFixCount = havetoFixCount + 1
        break

print(havetoFixCount)