from dateutil import parser
import pandas as pd


class QueryJson:
    def __init__(self, formatted_data) -> None:
        self.data = formatted_data
        self.df = pd.read_json(formatted_data)

    def getTotalConversions(self):
        total = 0
        for value in self.data.values():
            for entry in value:
                if entry['event'] == 'conversion':
                    total += 1
        return total

    # do not use it to get conversion by time
    def getConversionBy(self, field):
        locale = {}
        for value in self.data.values():
            for entry in value:
                if entry['event'] == 'conversion':
                    if entry[field] not in locale:
                        locale[entry[field]] = 1
                    else:
                        locale[entry[field]] += 1
        return locale

    def getEventsByHour(self, specifications, utc_timezone="+00:00"):
        daytime = {}
        for value in self.data.values():
            for entry in value:
                flag = True
                for key in specifications.keys():
                    if entry[key] not in specifications[key]:
                        flag = False
                if flag:
                    time = parser.parse(
                        entry['time'].replace('Z', utc_timezone))
                    time += time.utcoffset()
                    if str(time.hour) not in daytime:
                        daytime[str(time.hour)] = 1
                    else:
                        daytime[str(time.hour)] += 1
        return daytime

    # use this for event and device field
    def getAllTypes(self, field):
        events = []
        for value in self.data.values():
            for entry in value:
                if entry[field] not in events:
                    events.append(entry[field])
        return events

    def getTotalBy(self, specifications):
        total = 0
        for value in self.data.values():
            for entry in value:
                flag = True
                for key in specifications.keys():
                    if entry[key] not in specifications[key]:
                        flag = False
                if flag:
                    total += 1

        return total
