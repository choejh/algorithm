#상하좌우

x = 1
y = 1

n = 5
plan = ["R","R","R","U","D","D"]

move = ["L","R","U","D"]

x_move = [0,0,-1,1]
y_move = [-1,1,0,0]

for plan_type in plan :
    for i in range(len(move)) :
        if plan_type == move[i] :
            nx = x + x_move[i]
            ny = y + y_move[i]
            
            if nx > 5 or nx < 1 or ny > 5 or ny < 1 :
                break
            else :
                x = nx
                y = ny

print("x=", x)
print("y=", y)
            
