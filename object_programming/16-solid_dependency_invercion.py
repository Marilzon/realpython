from abc import ABC, abstractmethod


# Interfaces
class IProcess(ABC):
    @abstractmethod
    def execute(self) -> None: ...


# Class
class Process(IProcess):
    def execute(self) -> None:
        print("Process execute")


class System:
    def __init__(self, process: IProcess) -> None:
        self.__process = process

    def run(self) -> None:
        self.__process.execute()
        print("System run")


if __name__ == "__main__":
    process = Process()
    system = System(process)
    system.run()
