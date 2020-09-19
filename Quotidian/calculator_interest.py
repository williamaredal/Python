import matplotlib.pyplot as plt 
import numpy as np 

deposit = int(input("Size of deposit you would like to calculate:"))
interest = int(input("Return on investment:")) 
duration = int(input("Duration of investment:")) 

array = []

while deposit <= 0 or interest <= 0 or duration <= 0:
    print("Please reenter valid digits.")
    int(input("Size of deposit you would like to calculate:"))
    int(input("Return on investment:"))
    int(input("Duration of investment:"))

else:
    for i in range(duration+1): 
        deposit = (deposit*(1+(interest/100))**i)
        array.append(deposit)


mpl_fig = plt.figure()
ax = mpl_fig.add_subplot(111)
line, = ax.plot(duration, deposit, lw=2)

ax.set_title("Investment over "+str(duration)+" years with "+str(interest)+"% return.")
ax.set_xlabel("Duration")
ax.set_ylabel("Investment")

plt.plot(array)
plt.show()