from lib import query
from lib import data
from sys import getsizeof, exit
import matplotlib.pyplot as plt

# if you haven't formatted data yet if you don't provide any arguments it will take the path as Input_Records-rjopma1bz5n6bxxvxhq0.json
# data = data.Data()
# data.savaData('formatted.json')

# if you have formatted data do this cause it's faster
data = data.Data(formatted_path='formated.json')
# make queries
q = query.QueryJson(data.getData())

keys_convert = q.getConvertKeys().keys()
time_convert = []
for key in keys_convert:
    time_convert.append(q.getConvertTimeById(key))
print(len(time_convert))
print(len(keys_convert))
for t in time_convert:
    if t is None:
        print("yes")
plt.bar([i for i in range(len(keys_convert))], time_convert)
plt.show()