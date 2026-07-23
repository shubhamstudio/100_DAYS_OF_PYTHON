# start = int(input("enter number: "))
# end = int(input("enter number: "))
# for i in range(start, end):
#     if start < 0 or end < 0:
#         continue
#     start+=i
# print(start)

# total = 0
# while True:
#     num = int(input("enter number: "))
#     if num == 0:
#         break
#     if num < 0:
#         continue
#     total += num

# print(total)

total = 0
for _ in range(10):
    num = int(input("enter number"))
    if num == 0:
        break
    if num < 0:
        continue
    total += num

print(total)