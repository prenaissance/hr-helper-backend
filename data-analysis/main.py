from lib import query
from lib import data
from sys import getsizeof, exit

# if you haven't formated data yet if you don't provide any arguments it will take the path as Input_Records-rjopma1bz5n6bxxvxhq0.json
# data = data.Data()
# data.savaData('formated.json')

# if you have formated data do this cause it's faster
data = data.Data(formated_path='formated.json')
# make queries
q = query.QueryJson(data.getData())
print(q.getTotalConversions())
print(q.getConversionBy('device'))
print(q.getConversionBy('locale'))
# print(q.getConversionByHour("+00:00"))

# in order to sort by time do this
time = sorted(q.getConversionByHour("-10:00").items(), key=lambda x:int(x[0]) )
print(time)
print(q.getAllTypes('event'))
print(q.getTotalBy({"event" : ["conversion"],
                    "locale": ["en-US"],
                }))