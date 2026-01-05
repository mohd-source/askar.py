# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [5, 10, 3, 6, 5]
# plt.bar(x, y)
# plt.title("Bar chart")
# plt.legend("Bar Chart")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.grid()
# plt.show()




# plt.plot(x, y)
# plt.title("Line chart")
# plt.legend("Bar Chart")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.grid()
# plt.show()



# plt.scatter(x, y)
# plt.title("scatter chart")
# plt.legend(['Scattrr'])
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.grid()
# plt.show()



# plt.hist(x, y)
# plt.title("Histogram chart")
# plt.legend(['Histogram'])
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.grid()
# plt.show()

# plt.pie(y, labels=x)
# plt.title("Pie Chart")
# plt.legend(['Pie'])
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.show()


# # combined all charts in one figure
# fig, axs = plt.subplots(2,2)
# fig.suptitle("All Charts in One Figure")
# axs[0,0].plot(x,y)
# axs[0,0].set_title("Line Chart")
# axs[0,1].bar(x,y)
# axs[0,1].set_title("Bar Chart")
# axs[1,0].scatter(x,y)
# axs[1,0].set_title("Scatter Plot")
# axs[1,1].hist(y)
# axs[1,1].set_title("Histogram")
# plt.tight_layout()
# axs[1,1].pie(y, labels=x)
# axs[1,1].set_title("Pie Chart") 
# plt.show()


import matplotlib.pyplot as plt

x = [1,2,3,4 ]
y = [5,2,3,4]
plt.plot(x,y)
plt.title("Line Chart")
plt.legend(['Line'])
plt.xlabel("X Axis")
plt.ylabel("Y Axis")


plt.bar(x,y)
plt.title("Bar Chart")
plt.legend(['Bar'])
plt.xlabel("X Axis")
plt.ylabel("Y Axis")


plt.scatter(x,y)
plt.title("Scatter Plot")
plt.legend(['Scatter'])
plt.xlabel("X Axis")
plt.ylabel("Y Axis")


plt.hist(y)
plt.title("Histogram")
plt.legend(['Histogram'])
plt.xlabel("X Axis")
plt.ylabel("Y Axis")


plt.pie(y, labels=x)
plt.title("Pie Chart")
plt.legend(['Pie'])
plt.xlabel("X Axis")
plt.ylabel("Y Axis")



fig, axs = plt.subplots(2,2)
fig.suptitle("All Charts in One Figure")
axs[0,0].plot(x,y)
axs[0,0].set_title("Line Chart")
axs[0,1].bar(x,y)
axs[0,1].set_title("Bar Chart")
axs[1,0].scatter(x,y)
axs[1,0].set_title("Scatter Plot")
axs[1,1].hist(y)
axs[1,1].set_title("Histogram")
plt.tight_layout()
axs[1,1].pie(y, labels=x)
axs[1,1].set_title("Pie Chart") 
plt.show()