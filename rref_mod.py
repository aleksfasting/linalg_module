
A = [[0.5,-1,3.5,-1.5],[-2.5,1,2.5,-0.5]]
for i in range(len(A)):
    print(A[i])

print()

def firstNonZero(li,index):
    for i in range(index,len(li)):
        if li[i] != 0:
            return i
    return None

def rref(A):
    for x in range(len(A)):
        try:
            d = A[x][x] #elementet langs diagonalen
            for i in range(len(A[x])):
                A[x][i] = A[x][i]/d #del hele raden på elementet langs diagonalen
        except: #Hvis det første elementet i raden er 0
            for i in range(x+1,len(A)): #finner den første raden med ikke-null i diagonalen
                f = firstNonZero(A[i],x) #finner det første ikke-null elementet
                if f == x: #hvis det elementet er i diagonalen
                    li = A[x] #bytt radene
                    A[x] = A[i]
                    A[i] = li
                    break #avslutt løkken
    
        for i in range(x+1,len(A)):
            d = A[i][x] #første elementet i diagonalen
            for j in range(len(A[i])):
                A[i][j] = A[i][j] - d * A[x][j] #tar hele raden minus det d ganger hovedraden

    i = min(len(A),len(A[0])) - 1
    while i > 0:
        for j in range(1,i+1):
            d = A[i-j][i]
            for k in range(len(A[0])):
                A[i-j][k] = A[i-j][k] - d * A[i][k]
        i = i - 1

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == int(A[i][j]):
                A[i][j] = int(A[i][j])

rref(A)
for row in A:
    print(row)
print()
