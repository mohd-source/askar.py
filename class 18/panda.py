import pandas as pd




# data = [10, 20, 30, 40, 'askar']
# my_series = pd.Series(data)
# print(my_series)
# print()

# print("pandas by using list")

# data1 = [20, 40, 'askar', 'baqar']
# series = pd.Series(data1)
# print(series)
# print()

# print("pandas by using index")
# print(pd.Series(data1, index = ['A', 'B', 'C', 'D']))
# print("pandas by using index")
# print()


# print("pandas by using dictionary")

# dataframe = {
#     'Name': ['Askar', 'Baqar', 'Cakar'],
#     'Age': [21, 22, 23],
#     'City': ['Peshawar', 'Islamabad', 'Karachi']
# }



# print("dictionary by series")

# se = pd.Series(dataframe)
# print(se)
# print()


# print("dictionary by dataframe\n")

# df = pd.DataFrame(dataframe, index = ['1.', '2.', '3.'])
# print(df)
# print()


# print("dictionary by dataframe\n")

# df = pd.DataFrame(dataframe, columns=['pashawar', 'Islamabad', 'Karachi'])
# print(df)
# print()



# frame = [['Pakistan' , 'India' , 'China','USA','Turkey'],
#          ['Islamabad' , 'New Delhi' , 'Beijing' , 'Washington DC' , 'Ankara'],
#          ['220 Million' , '1.4 Billion' , '1.4 Billion' , '330 Million' , '80 Million']]
# my_dataframe1 = pd.DataFrame(frame , index = ['Country' , 'Capital' , 'Population'])
# print(my_dataframe1)
# print()

dataframe = {
    'Name': ['Askar', 'Baqar', 'Cakar'],
    'Age': [21, 22, 23],
    'City': ['Peshawar', 'Islamabad', 'Karachi']
}

my_dataframe2 = pd.DataFrame(dataframe)
# print(my_dataframe2)
# print()


print("dataframe by using csv file\n")

my_dataframe2.rename(index={0: 'a', 1: 'b', 2: 'c'}, inplace=True)

my_dataframe2.to_csv('data.csv')
read_df = pd.read_csv('data.csv')

print(read_df)
print()


my_dataframe2 = pd.DataFrame(dataframe, index=pd.RangeIndex(1,4))
print(my_dataframe2)
print()





df = {
    'Name': ['Askar', 'Baqar', 'Cakar'],
    'Age': [21, 22, 23],
    'City': ['Peshawar', 'Islamabad', 'Karachi']
}


df1 = pd.DataFrame(df)
df1.iloc[1, 0] = 'ashhad'
print(df1)
print()


