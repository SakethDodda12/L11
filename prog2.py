rows = int(input("Please enter the total amount of rows: "))
number = 1 

print("loyd triangle")
for i in range(1,rows + 1):
    for j in range(1,i +1):
        print(number, end = ' ')
        number = number + i
    print()
