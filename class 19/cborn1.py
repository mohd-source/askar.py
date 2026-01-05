import seaborn as sns
import matplotlib.pyplot as plt

ds = sns.load_dataset("tips")
ds.head()
print(ds.head())


sns.jointplot(x = "total_bill", y = "tip", data = ds, kind = "reg")
plt.show()


sns.jointplot(x = "total_bill", y = "tip", data = ds, kind = "hist")
plt.show()


sns.jointplot(x = "total_bill", y = "tip", data = ds, kind = "kde")
plt.show()


sns.jointplot(x = "total_bill", y = "tip", data = ds, kind = "resid")
plt.show()




sns.displot(ds["total_bill"],kde = False)
plt.show()



sns.pairplot(ds, hue ='sex')
plt.show()


sns.rugplot(ds['total_bill'], color = 'black')
plt.show()


# create simple dashboard
sns.set(style="whitegrid")
fig, axs = plt.subplots(2,2, figsize=(10,8))
sns.lineplot(x="total_bill", y="tip", data=ds, ax=axs[0,0])
axs[0,0].set_title("Line Plot")
sns.barplot(x="day", y="total_bill", data=ds, ax=axs[0,1])
axs[0,1].set_title("Bar Plot")
sns.scatterplot(x="total_bill", y="tip", data=ds, ax=axs[1,0])
axs[1,0].set_title("Scatter Plot")
sns.histplot(ds["total_bill"], kde=False, ax=axs[1,1])
axs[1,1].set_title("Histogram")
plt.tight_layout()
plt.show()