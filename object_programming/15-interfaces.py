from abc import ABC, abstractmethod
from pprint import pprint


class Employee(ABC):
    @abstractmethod
    def do_work(self) -> None: ...
    @abstractmethod
    def go_to_home(self) -> None: ...
    @abstractmethod
    def pause_work(self) -> None: ...


class DataEngineer(Employee):
    def do_work(self):
        pprint("DataEngineer Working")

    def go_to_home(self):
        pprint("Go to home")

    def pause_work(self):
        pprint("Pause work")


class Developer(Employee):
    def do_work(self):
        pprint("Developer Working")

    def go_to_home(self):
        pprint("Go to home")

    def pause_work(self):
        pprint("Pause work")


def employee_notifications(employee: Employee):
    employee.do_work()
    print("Work finished, go to home employee")
    employee.go_to_home()


if __name__ == "__main__":
    john_doe = DataEngineer()
    van_doe = Developer()

    employee_notifications(john_doe)
    employee_notifications(van_doe)
