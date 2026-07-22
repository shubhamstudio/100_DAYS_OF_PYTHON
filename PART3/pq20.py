def print_factors(n):
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count+=1
            print(i)
        i += 1
    print(f"Count = {count}")

print_factors(17)
