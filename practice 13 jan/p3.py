import pandas as pd

marks = pd.Series({'Math': 80, 'Science': 85, 'English': 76})

marks = marks + 5

print("Highest Marks:", marks.max())
print()

mar = marks.items()

for i, j in mar:
    print(i, ":", j)