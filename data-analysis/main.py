from lib import query
from lib import data
from sys import getsizeof, exit
import matplotlib.pyplot as plt

# if you haven't formatted data yet if you don't provide any arguments it will take the path as Input_Records-rjopma1bz5n6bxxvxhq0.json
# data = data.Data()
# data.savaData('formatted.json')

# if you have formatted data do this cause it's faster
data = data.Data(formatted_path='formatted.json')
# make queries
q = query.QueryJson(data.getData())

keys_convert = q.getConvertKeys()

time_convert = []
for key in keys_convert.keys():
    tm = q.getConvertTimeById(key)
    time_convert.append(tm)
    keys_convert[key] = tm


new_dict = []
print(min(list(keys_convert.values())))
for key in keys_convert.keys():
    new_dict.append({"id":key, "convert_time":keys_convert[key]})


# Method 1
import pandas as pd
df = pd.DataFrame(new_dict)
df["zscore"] = (df.convert_time - df.convert_time.mean()) / df.convert_time.std()
df["time2"] = (df.zscore * 100) + 200

df.to_csv('my_file.csv', index=False, header=True)
df.sample(5)
print(df.time2.describe())
plt.hist(df.time2, bins=10, rwidth=0.8)
plt.show()
df = df[(df['zscore'] < -0.37)]
print(df.convert_time.describe())
plt.hist(df.convert_time, bins=10, rwidth=0.8)
plt.show()



# make queries
q = query.QueryJson(data.getData())

keys_convert = q.getConvertKeys()

time_convert = []
for key in keys_convert.keys():
    tm = q.getConvertTimeById(key, 471.964000)
    time_convert.append(tm)
    keys_convert[key] = tm
plt.bar([i for i in range(len(keys_convert))], time_convert)
plt.show()