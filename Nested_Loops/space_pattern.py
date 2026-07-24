for i in range(1, 6):
    for k in range(1, 6 - i, 1):
        # 6=>5 and 5-1=>4 ****1 and so on
        print(" ", end=" ")
    for j in range(1, i + 1, 1):
        print(j, end=" ")
    print()
