from car_build.make_body import Body
from car_build.make_wheel import Wheel
from car_build.assemble_parts import Assemble

if __name__ == "__main__":
    body = Body("Black", "Giant")
    wheels = Wheel("Red", "Giant")
    assemble_a = Assemble(body, wheels)
    assemble_a.print_info()