class Select:
    def by_id(self, id):
        return f"select * from table where id = {id}"

class Insert:
    def value(self):
        return f"insert value into table __tablename__"

class Repository:
    def __init__(self):
        self.__select = Select()
        self__insert = Insert()

    def select_by_id(self, id: int):
        print(self.__select.by_id(id))


repository = Repository()
repository.select_by_id(1)
