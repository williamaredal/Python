string = "lost"

str_list = []
pal_list = []
count = 0
for p in range(0, len(string), +1):
    pal_list.append(string[p])
    print(p)

for i in range(len(string)-1, -1, -1):
    str_list.append(string[i])
    print(i)

for l in range(len(str_list)):
    if str_list[l] == pal_list[l]:
        count += 1
    if str_list[l] != pal_list[l]:
        print("Not a palindrome unfortunately.")
        break
    if count == len(str_list):
        print("It's a palindrome!")
        break

# sugested solution, more compact code
'''
wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
'''