def Tower_of_Hanoi(n, source, destination, auxiliary):
    if n == 0:
        return
    elif n == 1:
        print('Move that disk from', source, 'to', destination)
    else:
        Tower_of_Hanoi(n - 1, source, auxiliary, destination)
        print('Move that disk from', source, 'to', destination)
        Tower_of_Hanoi(n - 1, auxiliary, destination, source)
n = int(input("Enter the number of disks: "))
moves = (2 ** n) - 1
print("Number of moves is:", moves)
Tower_of_Hanoi(n, 1, 3, 2)
