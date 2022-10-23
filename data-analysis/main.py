from lib import query
from lib import data
from sys import getsizeof, exit

# if you haven't formatted data yet if you don't provide any arguments it will take the path as Input_Records-rjopma1bz5n6bxxvxhq0.json
# data = data.Data()
# data.savaData('formatted.json')

# if you have formatted data do this cause it's faster
data = data.Data(formatted_path='formatted.json')
# make queries
q = query.QueryJson(data.getData())
# print(q.getTotalConversions())
# print(q.getConversionBy('device'))
# print(q.getConversionBy('locale'))
# print(q.getConversionByHour("+00:00"))

# in order to sort by time do this
time = sorted(q.getConversionByHour("-10:00").items(), key=lambda x: int(x[0]))
print(time)
print(q.getAllTypes('event'))
print(q.getTotalBy({"event": ["conversion"],
                    "locale": ["en-US"],
                    }))
# time = sorted(q.getEventsByHour(["conversion"]).items(), key=lambda x:int(x[0]) )
# print(time)
# print(q.getAllTypes('event'))
# print(q.getTotalBy({"event" : ["conversion"],
#                    "locale": ["en-US"],
#                }))
"""
print(q.getConvertTimeById('7147895458715247184'))
t = q.getConvertKeys()
for key, value in zip(t.keys(), t.values()):
    if value > 1:
        print(key, value)
"""

keys_convert = q.getConvertKeys().keys()
time_convert = []
for key in keys_convert:
    time_convert.append(q.getConvertTimeById(key))
print(len(time_convert))
print(len(keys_convert))
for t in time_convert:
    if t is None:
        print("yes")
