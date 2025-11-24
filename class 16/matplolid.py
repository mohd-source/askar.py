# import matplotlib.pyplot as plt   
# import numpy as np





# car = np.array(['BMW', 'Toyota', 'Honda', 'Ford'])
# weight = np.array([1000, 1500, 1200, 1300])
# colors = np.array(['r', 'g', 'b', 'y'])
# size = np.array([50, 200, 100, 150])

# # for line representation on graph
# plt.plot(car, weight)
# plt.show()



# # for point representation on graph
# plt.scatter(car, weight, c=colors, s=size)
# plt.show()



# # bar graph
# plt.bar(car, weight, color=colors)
# plt.show()

# # histogram representation
# histogram_data = np.random.randn(10)
# plt.hist(histogram_data, color='red', alpha=0.9, bins=30)
# plt.show()


# # pie chart representation
# plt.pie(weight, labels=car, colors=colors, startangle=100, shadow=True, explode=(0.1, 0, 0, 0), autopct='%1.1f%%')
# plt.show()





print("\n---------------------Deshboard----------------------\n")


# import numpy as np
# import matplotlib.pyplot as plt

# car = np.array(['BMW', 'Toyota', 'Honda', 'Ford'])
# weight = np.array([1000, 1500, 1200, 1300])
# colors = np.array(['r', 'g', 'b', 'y'])
# size = np.array([50, 200, 100, 150])

# histogram_data = np.random.randn(10)

# # Create dashboard
# plt.figure(figsize=(12, 10))

# # ------------------ 1. Line Plot ------------------
# plt.subplot(2, 3, 1)
# plt.plot(car, weight, marker='o')
# plt.title("Line Plot")
# plt.xlabel("Car")
# plt.ylabel("Weight")

# # # ------------------ 2. Scatter Plot ------------------
# # plt.subplot(2, 3, 2)
# # plt.scatter(car, weight, c=colors, s=size)
# # plt.title("Scatter Plot")
# # plt.xlabel("Car")
# # plt.ylabel("Weight")

# # ------------------ 3. Bar Chart ------------------
# plt.subplot(2, 3, 3)
# plt.bar(car, weight, color=colors)
# plt.title("Bar Chart")
# plt.xlabel("Car")
# plt.ylabel("Weight")

# # # ------------------ 4. Histogram ------------------
# # plt.subplot(2, 3, 4)
# # plt.hist(histogram_data, color='red', alpha=0.9, bins=30)
# # plt.title("Histogram")

# # ------------------ 5. Pie Chart ------------------
# plt.subplot(2, 3, 5)
# plt.pie(weight, labels=car, colors=colors, startangle=100,
#         shadow=True, explode=(0.1, 0, 0, 0), autopct='%1.1f%%')
# plt.title("Pie Chart")

# plt.tight_layout()
# plt.show()







import numpy as np
import matplotlib.pyplot as plt

# Data
car = np.array(['BMW', 'Toyota', 'Honda', 'Ford'])
weight = np.array([1000, 1500, 1200, 1300])
colors = np.array(['crimson', 'forestgreen', 'royalblue', 'gold'])
size = np.array([200, 350, 250, 300])

histogram_data = np.random.randn(100)

# --- Dashboard Style ---
plt.style.use("seaborn-v0_8-darkgrid")
plt.figure(figsize=(14, 10))
plt.suptitle("Car Data Visualization Dashboard", fontsize=18, fontweight='bold')

# ------------------ 1. Line Plot ------------------
plt.subplot(2, 3, 1)
plt.plot(car, weight, marker='o', linewidth=2, color='royalblue')
plt.title("Line Plot")
plt.xlabel("Car Models")
plt.ylabel("Weight")

# ------------------ 2. Scatter Plot ------------------
plt.subplot(2, 3, 2)
plt.scatter(car, weight, c=colors, s=size, edgecolor="black")
plt.title("Scatter Plot")
plt.xlabel("Car Models")
plt.ylabel("Weight")

# ------------------ 3. Bar Chart ------------------
plt.subplot(2, 3, 3)
plt.bar(car, weight, color=colors)
plt.title("Bar Chart")
plt.xlabel("Car Models")
plt.ylabel("Weight")

# ------------------ 4. Histogram ------------------
plt.subplot(2, 3, 4)
plt.hist(histogram_data, color='crimson', alpha=0.85, bins=25)
plt.title("Histogram of Random Data")

# ------------------ 5. Pie Chart ------------------
plt.subplot(2, 3, 5)
explode_values = (0.08, 0, 0, 0)
plt.pie(weight, labels=car, colors=colors, explode=explode_values,
        autopct='%1.1f%%', shadow=True, startangle=120)
plt.title("Weight Distribution by Car Model")
plt.axis('equal')  # Equal aspect ratio ensures pie chart is circular.
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
