rowSize =  int(input("Enter the number of rows you want: "))

if rowSize%2 == 0:
    halfDiamRow =int(rowSize/2)
else:
    halfDiamRow = int(rowSize/2)
space = halfDiamRow-1
for i in range(1, halfDiamRow+1): #loop for rows
    for j in range(1, space+1): #loop for columns
        print(end=" ")
    space = space-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
#incerementing number at each column
        num = num+1
    print()
space = 1
#loop for lower part
for i in range(1, halfDiamRow): #loop for rows
    for j in range(1, space+1): #loop for columns
        print(end=" ")
    space = space+1
    num = 1
    for j in range(1, 2*(halfDiamRow-i)):
        print(end=str(num)) #display result
#incerementing number at each column
        num = num+1
    print()