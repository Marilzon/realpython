"""
SOLID:
 - Single responsability.
"""

# BAD SOLID
# class SystemCore:
#     def sign(self, name: str, age: int) -> None:
#         if isinstance(name, str) and isinstance(age, int):
#             print("Accesing database")
#             print(f"Sign user {name}, age {age}.")
#         else:
#             print("Invalid data.")



# Single responsability.
class SystemCore:
    def sign(self, name: str, age: int) -> None:
        if  self.__validate_input(name, age):
            self.__create_user(name, age)
        else:
            self.__error_handle()

    def __validate_input(self, name: str, age: int) -> bool:
        return isinstance(name, str) and isinstance(age, int)

    def __create_user(self, name: str, age: int) -> None:
            print("Accesing database.")
            print(f"Sign user {name}, age {age}.")

    def __error_handle(self) -> None:
            print("Invalid data.")

system = SystemCore()
system.sign("marilzon", 32)
system.sign("marilzon", "32")
