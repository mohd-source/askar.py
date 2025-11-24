import pandas as pd
import matplotlib.pyplot as plt 

# data = {
#     'Name': ['Askar', 'Baqar', 'Cakar'],
#     'Age': [21, 22, 23],
#     'City': ['Peshawar', 'Islamabad', 'Karachi']
# }

# frame = [['Pakistan' , 'India' , 'China','USA','Turkey'],
#          ['Islamabad' , 'New Delhi' , 'Beijing' , 'Washington DC' , 'Ankara'],
#          ['220 Million' , '1.4 Billion' , '1.4 Billion' , '330 Million' , '80 Million']]

# # f = pd.DataFrame(frame , index = ['Country' , 'Capital' , 'Population'])
# # print(f)



# df = pd.DataFrame(data, index = ['1.', '2.', '3.'])
# df1 = df.iloc[0,0] = 'Ashad'
# print(df1)
# print(df)




# print(df.head(1))  # prints the first row
# print()
# print(df.tail(1))   # prints the last two rows
# print()



# # manupulating dataframe

# df.loc[len(df.index)]= ['Farhan', 25, 'Multan']
# print(df)
# print()


# df.drop('Name',axis=1, inplace=True)

# print(df)


car = ['Carala', 'Honda', 'Suzuki']
weight = [500, 300, 600]

data = {'Car': car , 'Waight': weight}



df = pd.DataFrame(data)

df.plot(x = 'Car', y = 'Waight', kind = 'line' )
plt.xlabel('Cars Name')
plt.ylabel('Weight')
plt.title('Car data')
plt.show()


