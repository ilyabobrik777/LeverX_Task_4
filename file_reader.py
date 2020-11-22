import json

class File_reader:
    def __init__(self, file):
        self.file = file


    def file_reader(self):
        with open(self.file) as read_file:
            data = json.load(read_file)
        return data












