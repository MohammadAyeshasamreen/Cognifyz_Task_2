rows = 5

for i in range(1, rows + 1):
    # Print leading spaces
    for space in range(rows - i):
        print(" ", end="")
    
    # Print ascending numbers
    for num in range(1, i + 1):
        print(num, end="")
    
    # Print descending numbers
    for num in range(i - 1, 0, -1):
        print(num, end="")
    
    print()