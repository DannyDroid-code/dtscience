
# Target - To Explain the different types of Plots possible using matplotlib
import matplotlib.pyplot as plt

# # Explain the case of using a histogram - Frequency chart
# ages = [22,55,36,45,21,67,45,23,89,11]
# bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# plt.hist(ages, bins, histtype = 'bar', rwidth = 0.8)
# plt.xlabel("Age Interval")
# plt.ylabel("Frequency")
# plt.title("Histogram")
# plt.show()

# Explain what is scatter plot - Use cases of scatter Plot
# x = [1,2,3,4,5,6,7,8,9]
# y = [0,1,0,1,0,1,0,1,0]

# plt.scatter(x, y, label = "Scatter Plot", color = 'red', marker = 'o', s = 50)

# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Scatter Plot")
# plt.legend()
# plt.show()

# # # Explain what is Pie chart - Use cases of Pie Chart
# slices = [6, 1 ,12, 1, 3]
# activities = ["sleeping", "eating", "working", "netflix", "workout & friends"]

# cols = ['c', 'm', 'r', 'b', 'g']

# plt.pie(slices, labels = activities, colors = cols, startangle = 90, shadow = True)
# plt.title("Day Chart")
# plt.show()

# # Explain what is stack-plot - Use cases of stack plot
# days = [1,2,3,4,5]

# eating = [2,3,4,3,2]
# sleeping = [7,8,6,11,7]
# working = [7,8,7,2,2]
# playing = [8,5,7,8,13]

# plt.plot([], [], color = 'm', label = "Eating", linewidth = 5)
# plt.plot([], [], color = 'c', label = "Sleeping", linewidth = 5)
# plt.plot([], [], color = 'r', label = "Working", linewidth = 5)
# plt.plot([], [], color = 'k', label = "Playing", linewidth = 5)

# plt.stackplot(days, eating, sleeping, working, playing, colors = ['m','c','r','k'])

# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Stack Plot")
# plt.legend()
# plt.show()

# Subplot - To make use of single matplotlib window to draw multiple plots
#plt.figure() -> the matplotlib window
#plt.subplot(221) - the cooncerned subplot, 2 - total row, 2 - total column, 1 - index in the subplot matrix


import numpy as np

def f(t):
  return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0, 5, 0.1)
t2 = np.arange(0, 5, 0.02)

plt.figure()
plt.subplot(221)
plt.plot(t1, f(t1), 'bo')

plt.subplot(224)
plt.plot(t2, np.cos(2*np.pi*t2))

plt.show()
