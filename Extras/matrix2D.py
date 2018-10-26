m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
l = []
small, dsum1, dsum2, csum = 0, 0, 0, 0

for i in range(m):
    l.append([])
    for j in range(n):
        l[i].append(int(input("Enter element: ")))
        if i == 0 and j == 0:
            small = l[i][j]
        elif l[i][j] < small:
            small = l[i][j]
            
           
for i in l:
    print(i, "\tSum of row =", sum(i))

if m == n:
    for i in range(m):
        dsum1 += l[i][i]
        dsum2 += l[i][m-i-1]
        
print()
for i in range(n):
    for j in range(m):
        csum += l[j][i]
    print(csum, end = " ")
    csum = 0

print("\n\nSmallest number in matrix is", small)
if m == n:
    print("\nSums of diagonals are", dsum1, ",", dsum2)
