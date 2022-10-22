"""
converting from list of dictionaries to dictionary with primary key personid, the value of the keys it's a list off all the dictionaries
[
{"event_name", "event_time", "personid", "url", "device_type", "locale"}
...                                                             
{"event_name", "event_time", "personid", "url", "device_type", "locale"}
]
                                 |
                                 |
                                 |
{"personid": [ {"event", "time", "url", "device", "locale"},
                {"event", "time", "url", "device", "locale"},
                ...  ] }
"""
from dateutil import parser

def get_formated_data(data : dict, sorted_time=False):
    mydata = {}
    for entry in data:
        formated = {'event' : entry['event_name'], 'time': entry['event_time'], 'url': entry['url'], 'device': entry['device_type'], 'locale':entry['locale']}
        if entry["personid"] not in mydata:
            mydata[entry["personid"]] = [formated]
        else:
            mydata[entry["personid"]].append(formated)
    if (sorted_time):
        def criteria(e):
            return parser.parse(e['time'])
        sorted_data = {}
        for key, value in zip(mydata.keys(), mydata.values()):
            value.sort(key=criteria)
            sorted_data[key] = value
        return sorted_data
            
    return mydata



"""
converting from list of dictionaries to dictionary with primary key personid, the value of the keys it's dictionary where each key contains a list of values
[
{"event_name", "event_time", "personid", "url", "device_type", "locale"}
...                                                             
{"event_name", "event_time", "personid", "url", "device_type", "locale"}
]
                                 |
                                 |
                                 |
{"personid":    {"event": [...]}
                "time":[...]
                "url":[...]
                "device":[...]
                "locale":[...]}
    ...
}
"""

def get_formated_data_list(data : dict):
    mydata = {}
    for entry in data:
        if entry["personid"] not in mydata:
            mydata[entry["personid"]] = {'event':[entry['event_name']], 
                                        'time':[entry['event_time']],
                                        'url':[entry['url']],
                                        'device':[entry['device_type']],
                                        'locale':[entry['locale']]}
        else:
            mydata[entry["personid"]]['event'].append(entry['event_name'])
            mydata[entry["personid"]]['time'].append(entry['event_time'])
            mydata[entry["personid"]]['url'].append(entry['url'])
            mydata[entry["personid"]]['device'].append(entry['device_type'])
            mydata[entry["personid"]]['locale'].append([entry['locale']])
    return mydata


import json
def save_json(data, path):
    with open(path, "w") as outfile:
        json.dump(data, outfile)

def load_json(path):
    f = open(path)
    data = json.load(f)
    f.close()
    return data