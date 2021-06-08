import numpy as np

T = int(input())

# creates list from inputs
for i in range(T):
    N, K = (input()).split()
    A = input().split(" ")

    # shifts list by K steps to the right
    SA = np.roll(A, int(K))
    out = " ".join(SA)

    print(out)