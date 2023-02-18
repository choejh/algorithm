#4-2 시각
#정수 n이 입력되면 00:00:00~ n시:59:59 까지 n이 몇번 나왔는지 카운트

n = 5
cnt = 0
for hour in range(n+1) :
    for min in range(60) :
        for sec in range(60) :
            change = str(hour)+str(min)+str(sec)
            if str(n) in change :
                cnt+=1

print(cnt)
