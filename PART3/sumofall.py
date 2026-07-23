sum = 0
count=0
for i in range(1, 30 + 1):
    if i % 3 == 0 and i % 5 == 0:
        sum += i
        count+=1
        print(i)
print(f"The total sum is: {sum}")
print(f"Total divisible numbers are: {count}")
