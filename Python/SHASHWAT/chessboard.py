for i in range(1,9):
    if i%2==0:
        for j in range(1,9):
            if j%2==0:
                print("BLACK", end="  ")
            else:
                print("WHITE", end="  ")
        print()
    else:
        for j in range(1,9):
            if j%2==0:
                print("WHITE", end="  ")
            else:
                print("BLACK", end="  ")
        print()
print()