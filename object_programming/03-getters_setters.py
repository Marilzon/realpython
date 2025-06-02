from IPython.display import display


class SomeClass:
    def __init__(self) -> None:
        self.__value = None
        display(f"init: {self.__value}")

    def setter_value(self, value: int) -> None:
        self.__value = value
        display(f"setter: {self.__value}")

    @property
    def getter_value(self) -> int:
        display(f"getter: {self.__value}")


instance_some_class = SomeClass()
setter_value = instance_some_class.setter_value(1)
setter_value = instance_some_class.setter_value(2)
setter_value = instance_some_class.setter_value(3)
setter_value = instance_some_class.getter_value
