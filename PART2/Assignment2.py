# def calc_tax(salary):
#     if salary < 30000:
#         return "5%"
#     elif 30000 <= salary <= 70000:
#         return "15%"
#     else:
#         return "25%"

# salary = int(input("enter salary: "))
# print(calc_tax(salary))

def print_even(a, b):
    start, end = min(a, b), max(a, b)
    if start%2!=0:
        start+=1
    
    for i in range(start, end + 1, 2):
        print(i)

print_even(199, 19) 