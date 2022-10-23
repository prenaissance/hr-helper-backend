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
import json


class Format:
    @staticmethod
    def get_formatted_data(data: dict, sorted_time=False):
        mydata = {}
        for entry in data:
            formatted = {'event': entry['event_name'], 'time': entry['event_time'],
                         'url': entry['url'], 'device': entry['device_type'], 'locale': entry['locale']}
            if entry["personid"] not in mydata:
                mydata[entry["personid"]] = [formatted]
            else:
                mydata[entry["personid"]].append(formatted)
        if (sorted_time):
            def criteria(e):
                return parser.parse(e['time'])
            sorted_data = {}
            for key, value in zip(mydata.keys(), mydata.values()):
                value.sort(key=criteria)
                sorted_data[key] = value
            return sorted_data

        return mydata

    @staticmethod
    def save_json(data, path):
        with open(path, "w") as outfile:
            json.dump(data, outfile)

    @staticmethod
    def load_json(path):
        f = open(path)
        data = json.load(f)
        f.close()
        return data
