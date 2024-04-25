class Rectangle(object):
    def __init__(self, b, h):
        self.base = b
        self.height = h
    def change_values(self, new_b, new_h):
        self.new_b = new_b
        self.new_h = new_h
        return f"Os novos valores para base e altura são respectivamente {self.new_h}, {self.new_h}"





rectangle = Rectangle(5, 8)
print(rectangle.base, rectangle.height)
