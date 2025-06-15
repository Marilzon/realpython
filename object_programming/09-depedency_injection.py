from functools import reduce


class DatabaseConnector:
    def __init__(self) -> None:
        self.connection = False

    def connect(self) -> None:
        self.connection = True


class DatabaseRepository:
    def __init__(self, connection: DatabaseConnector) -> None:
        self.__connection = connection

    def data_query(self) -> list:
        if self.__connection.connection:
            return [1, 2, 3]
        return None


class Service:
    def __init__(self, repository: DatabaseRepository) -> None:
        self.__repository = repository

    def __add(self, x, y) -> int:
        return x + y

    def make_result(self) -> None:
        data = self.__repository.data_query()
        if not data:
            return None

        response = reduce(self.__add, data)

        print(response)


conn = DatabaseConnector()
conn.connect()

repo = DatabaseRepository(conn)

service = Service(repo)
service.make_result()
