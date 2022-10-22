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
print(q.getConversionBy('device'))