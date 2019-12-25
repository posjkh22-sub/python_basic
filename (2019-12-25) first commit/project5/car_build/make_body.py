
class Body:
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
        print("color: ", self.color, ", size: ", self.size)


class MechanicBody(Body):
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.material = "mechanic"

    def print_info(self):
        print("material: ", self.material)
        super().print_info()


if __name__ == "__main__":
    print("[body_a]")
    body_a = Body("Black", "Big")
    body_a.print_info()

    print("[body_b]")
    body_b = MechanicBody("Black", "Big")
    body_b.print_info()


