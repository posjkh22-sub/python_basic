from car_build.make_body import Body
from car_build.make_wheel import Wheel


class Assemble:
    def __init__(self, _body, _wheel):
        self.body = _body
        self.wheel = _wheel

    def print_info(self):
        print("[body] ")
        self.body.print_info()
        print("[wheel] ")
        self.wheel.print_info()


if __name__ == "__main__":
    body = Body("Black", "Big")
    wheels = Wheel("Red", "Giant")
    assemble_a = Assemble(body, wheels)
    assemble_a.print_info()
