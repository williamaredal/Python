import time

loading = True
animation_list = ['[     ]','[->   ]', '[-->  ]', '[---> ]', '[---->]']

while loading:
    for a in animation_list:
        print(a)
        time.sleep(1)



# Also works, but less compact code
'''
i = 0
    if i >= len(animation_list):
        i = 0
    else:
        print(animation_list[i])
        i += 1
        time.sleep(1)
'''