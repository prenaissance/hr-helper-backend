from lib import format
from dateutil import parser


class Data:
    def __init__(self, initial_path=None, formatted_path=None) -> None:
        # path1 is the path of the initial json
        # path2 is the path of formatted and saved json
        if formatted_path is None and initial_path is not None:
            self.data = format.Format.get_formatted_data(
                format.Format.load_json(initial_path), sorted_time=True)
        elif formatted_path is not None:
            self.data = format.Format.load_json(formatted_path)
        # if path2 and path1 are both none a default path1 will be provided
        elif formatted_path is None and initial_path is None:
            path = 'Input_Records-rjopma1bz5n6bxxvxhq0.json'
            self.data = format.Format.get_formatted_data(
                format.Format.load_json(path), sorted_time=True)

    def savaData(self, path):
        format.Format.save_json(self.data, path)

    def getData(self):
        return self.data
