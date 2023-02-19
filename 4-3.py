#왕실의 나이트

putA = "a1"

x_y = [[2,1],[2,-1],[-2,1],[-2,-1],[-1,2],[-1,-2],[1,2],[1,-2]]
cnt = 0

tmp = [ord(putA[0])-96,putA[1]]
print(tmp)

for j in range(len(x_y)) :
    tmpA = [int(tmp[0])-x_y[j][0],int(tmp[1])-x_y[j][1]]
    print(tmpA)
    if tmpA[0]>8 or tmpA[0]<1 or tmpA[1]>8 or tmpA[1]<1 :
        continue
    else :
        cnt+=1

print(cnt)
