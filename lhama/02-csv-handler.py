class CsvHandler:
    def __init__(self, directory) -> None:
        self.dir = directory

    def read(self, data):
        self.__dir_exists()
        print(f"value '{data}' read from {self.dir}")

    def insert(self, data):
        print(f"value '{data}' inserted to {self.dir}")

    def __dir_exists(self):
        exists = False
        if self.dir:
            exists = True

        print(f"dir existance is {exists}")
        return exists

handler = CsvHandler("path/data.csv")

handler.read("marilzon")
