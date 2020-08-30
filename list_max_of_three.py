import random
max_of = 3
list_var = []

for i in range(max_of):
    var = input("Type a single number")
    # works with 'random.randint(0,10)' as well
    if i == 0:
        list_var.append(var)
    elif var > list_var[0]:
        list_var.insert(0,var)
    else:
        list_var.append(var)
print(list_var)
