import os
from IPython.display import display

class CsvHandler:
    def __init__(self, directory, separator=",") -> None:
        self.dir = directory
        self.separator = separator

    def read(self, filename):
        file_path = f"{self.dir}/{filename}.csv"

        if not self.__file_path_exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        data = []
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            for line in csv_file:
                stripped_line = line.strip()
                if stripped_line:
                    row = stripped_line.split(self.separator)
                    data.append(row)

        return data

    def __file_path_exists(self, file_path):
            return os.path.exists(file_path)


handler = CsvHandler("object_programming/data", ",")

display(handler.read("heroes"))
