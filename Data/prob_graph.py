import matplotlib.pyplot as plt 
import numpy as np 

prob = 100
array = []

for i in range(prob):
    if prob >= 0:
        prob -= i
        array.append(prob)
    
    else:
        print(array, "finished at", i, " iterations")
        break


plt.plot(array)
plt.show()
