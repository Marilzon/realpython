from IPython.display import display

class Hero:
    def __init__(self, name, points):
        self.name = name
        self.status = points

    def get_name(self):
        name = self.name
        return f"name: {name}"

    def get_points(self):
        points = self.points
        return f"name: {points}"


spider = Hero("Spider", 200)
spider_name = spider.get_name()

display(spider_name)
