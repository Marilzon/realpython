class Hero:
    def __init__(self, name, points):
        self.name = name
        self.status = points

    def get_name(self):
        name = self.name
        print(f"name: {name}")

    def get_points(self):
        points = self.points
        print(f"name: {points}")


spider = Hero("Spider", 200)

spider.get_name()
