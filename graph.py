#Created by: Cameron Coles
#Created on: July 25th 2023
#Purpose: Revenue graph for a car insurance company

###########
#libraries#
###########

import matplotlib.pyplot as plt



x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_axis = [0,0,0,0,0,0,0,0,0,0,0,0]
num = 0
for Month in x_axis:
    y_axis[num] = int(input(f"Enter Total Revenue From {Month}: "))
    num += 1

plt.plot(x_axis,y_axis)

plt.xlabel("Months (2023)")
plt.ylabel("Revenue ($)")

plt.title("Monthly Revenue Graph")
plt.grid(True)
plt.show()