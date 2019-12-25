
class Wheel:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def change_color(self, color):
        self.color = color

    def change_size(self, size):
        self.size = size

    def change_body(self, color, size):
        self.change_color(color)
        self.change_size(size)

    def print_info(self):
        print("color: " , self.color, ", size: ", self.size)


if __name__ == "__main__":
    body_a = Wheel("Black", "Big")
    body_a.print_info()


