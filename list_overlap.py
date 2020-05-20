import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = []

# arrays for random integer generation
c = []
d = []
common_random = []

# for loop generating random integers
for i in range(20):
    c.append(random.randint(1, 20))
    d.append(random.randint(1, 20))

print(zip(a,b))
for (e1, e2) in zip(a,b):
    if e1 in b and e1 not in common:
        common.append(e1)
    if e2 in a and e2 not in common:
        common.append(e2)
common.sort()
print(common)

for (r1, r2) in zip(c,d):
    if r1 in b and r1 not in common_random:
        common_random.append(r1)
    if r2 in a and r2 not in common_random:
        common_random.append(r2)
common_random.sort()
print(common_random)

# most compact solution to find common integers by using the 'set()' function
print(set(a) & set(b))