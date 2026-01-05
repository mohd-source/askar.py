import numpy as np

# Temperature data (cities × days)
temperatures = np.array([
    [30, 32, 31, 29, 28, 30, 31],
    [25, 26, 27, 26, 25, 24, 26],
    [35, 36, 34, 33, 35, 36, 34],
    [20, 21, 19, 18, 20, 22, 21],
    [28, 29, 30, 31, 29, 28, 30],
    [33, 34, 35, 36, 35, 34, 33],
    [22, 23, 24, 23, 22, 21, 23],
    [27, 28, 29, 30, 28, 27, 29],
    [31, 32, 33, 32, 31, 30, 32],
    [24, 25, 26, 25, 24, 23, 25]
])




# City averages
city_avg = temperatures.mean(axis=1)
print("City averages:", city_avg)

print("Hottest city index:", city_avg.argmax())
print("Coldest city index:", city_avg.argmin())




day_avg = temperatures.mean(axis=0)
print("\nDaily averages:", day_avg)
print("Hottest day index:", day_avg.argmax())






min_temp = temperatures.min()
max_temp = temperatures.max()

normalized = (temperatures - min_temp) / (max_temp - min_temp)
print("\nNormalized temperatures:\n", normalized)
