from abc import ABC, abstractmethod
from pprint import pprint

"""
If class do not use full interface logic, create other interface to new class,
do not force this class uses a useless method in this class context
"""


class Employee(ABC):
    @abstractmethod
    def start_work(self) -> None: ...
    @abstractmethod
    def end_work(self) -> None: ...
    @abstractmethod
    def query_benefits(self) -> None: ...


class InternEmployee(ABC):
    @abstractmethod
    def start_work(self) -> None: ...
    @abstractmethod
    def end_work(self) -> None: ...


class Teacher(Employee):
    def start_work(self) -> None:
        print("Teacher start lesson")

    def end_work(self) -> None:
        print("Teacher ends lesson")

    def query_benefits(self) -> None:
        print("Teacher query benefits")


class InternTeacher(InternEmployee):
    def start_work(self) -> None:
        print("InternTeacher start lesson")

    def end_work(self) -> None:
        print("InternTeacher ends lesson")


if __name__ == "__main__":
    john_doe = Teacher()
    van_doe = InternTeacher()
