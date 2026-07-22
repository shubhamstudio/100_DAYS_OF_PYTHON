# sum of all numbers 1 to 100
# which are divisible by 2 and 7
n = 1
total = 0

while n <= 50:
    if n % 2 == 0 and n % 7 == 0:
        total += n
        print(total)
    n = n + 1

print(f"Total = {total}")
