print("Hello Krikor")

list = [1,2,3,4,5]

for x in list:
    print(x)

def sum_list(lst):
    total = 0
    for x in lst:
        total += x
    return total

print("sum", sum_list(list))

