from query import QueryJson
from data import Data

# if you haven't formated data yet
#data = Data(initial_path='in.json')
#data.savaData('formated.json')

# if you have formated data

data = Data(formated_path='formated.json')

# make queries
q = QueryJson(data.getData())
# print(q.getTotalConversions())
#print(q.getConversionBy('device'))
#print(q.getConversionBy('locale'))
#print(q.getConversionByHour("+00:00"))

# in order to sort by time do this
time = sorted(q.getConversionByHour("-10:00").items(), key=lambda x:int(x[0]) )
print(time)


