from pprint import pprint


class SomeClass:
    def __init__(self) -> None:
        self.__value = None
        pprint(f"init: {self.__value}")

    def setter_value(self, value: int) -> None:
        self.__value = value
        pprint(f"setter: {self.__value}")

    @property
    def getter_value(self) -> int:
        pprint(f"getter: {self.__value}")
        return self.__value


instance_some_class = SomeClass()
setter_value = instance_some_class.getter_value
