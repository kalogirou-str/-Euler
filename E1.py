board = []
n=int(input("Παρακαλώ πληκτρολογήστε τον αριθμό των κορυφών: "))
if n%2==0:
    print("Δεν υπάρχει δρόμος Euler.")
else:
    print("Ο δρόμος Euler ειναι ο παρακάτω.")
    n=n+1
    for i in range(n):
        board.append([])
        for j in range(n):
            if i!=j:
                board[i].append(0)
            else:
                board[i].append(1)
    s=0
    for i in range(n-2,0,-1):
        s=s+i
    for k in range(1,s):
        if k==1:
            i=1
        for j in range(1,n):
            if board[i][j]==0:
                board[i][j]=1
                board[j][i] = 1
                print(i,"->")
                i=j
    print(i,".")
