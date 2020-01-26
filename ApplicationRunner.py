import pandas as pd

count = [5, 6, 8]
fruits =['apples', 'bananas', 'strawberry']
data = ["Max", "Ivan", "Jackie"]

dictionary = {'fruits': fruits,
              'count' : count}

series1 = pd.Series(data, index=["a", "b", "c"])
print(series1)

print(type(series1))

df = pd.DataFrame(dictionary)
print(df)



