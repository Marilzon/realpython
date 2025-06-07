import os
from IPython.display import display


class CsvHandler:
    def __init__(self, *, directory, separator=",") -> None:
        self.dir = directory
        self.separator = separator

    def read(self, filename):
        file_path = f"{self.dir}/{filename}.csv"

        if not self.__file_path_exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, "r", encoding="utf-8") as csv_file:
            lines = csv_file.readlines()
            processed_map = map(self.__csv_strip_split, lines, ",")
            processed_list = list(processed_map)

            if not processed_list:
                return []

            return processed_list

    def __file_path_exists(self, file_path):
        return os.path.exists(file_path)

    def __csv_strip_split(self, data, separator):
        return data.strip().split(separator)


handler = CsvHandler(directory="object_programming/data", separator=",")

display(handler.read("heroes"))
