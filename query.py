import format


class QueryJson:
    def __init__(self, formated_data) -> None:
        self.data = formated_data

    def getTotalConversions(self):
        total = 0
        for value in self.data.values():
            for entry in value:
                if entry['event'] == 'conversion':
                    total += 1
        return total
    
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