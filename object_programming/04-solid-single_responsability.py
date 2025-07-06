# BAD SOLID
# class SystemCore:
#     def sign(self, name: str, age: int) -> None:
#         if isinstance(name, str) and isinstance(age, int):
#             print("Accesing database")
#             print(f"Sign user {name}, age {age}.")
#         else:
#             print("Invalid data.")


# Single responsability success.
class SystemCore:
    def sign(self, name: str, age: int) -> None:
        if self.__validate_input(name, age):
            self.__create_user(name, age)
        else:
            self.__error_handle(self.__create_user)
            self.__rollback()

    def __validate_input(self, name: str, age: int) -> bool:
        return isinstance(name, str) and isinstance(age, int)

    def __create_user(self, name: str, age: int) -> None:
        print("Creating user.")
        print(f"Sign: {name=}, {age=} success.")

    def __error_handle(self, value) -> None:
        print(f"{value=} called invalid instances.")

    def __rollback(self):
        print("Job rollback success.")


system = SystemCore()
system.sign("marilzon", 32)
system.sign("marilzon", "32")
