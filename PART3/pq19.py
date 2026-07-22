
def print_fact(n):
    i, fact = 1, 1
    while i <= n:
        fact*=i
        print(fact)
        i+=1

print_fact(5)