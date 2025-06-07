

class User:
    def __init__(self, id, user_name):
        self.__id = id
        self.__user_name = user_name

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, value):
        if isinstance(value, str) and value:
            self.__user_name = value
        else:
            raise ValueError("Value is not str valid!")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if isinstance(value, int) and value:
            self.__id = value
        else:
            raise ValueError("Value is not integer valid!")


user = User(33, "Marilzon")
print(user.id, user.user_name)
user.id = 500
print(user.id, user.user_name)
