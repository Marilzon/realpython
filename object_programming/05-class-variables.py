class SomeClass:
    project_name = "some_project"

    def __init__(self, state: bool) -> None:
        self.state = state
        print(f"init: {self.state}")


obj1 = SomeClass(True)
obj2 = SomeClass(True)
print(obj1.project_name)
print(obj2.project_name)

# static values on new set gain side effect for all instances.
SomeClass.project_name = "buzu"
obj3 = SomeClass(True)
print(obj3.project_name)
print(obj1.project_name)
print(obj2.project_name)
