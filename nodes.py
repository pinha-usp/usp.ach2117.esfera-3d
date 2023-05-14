import glm

from base import Node, Mesh
from geometry import Sphere
from loader import ProgramLoader

class FixedSphere(Node):

    def __init__(self):
        sphere = Sphere(
            color = (1.0, 1.0, 1.0),
            depth = 4
        )

        mesh = Mesh(
            program = ProgramLoader.load(both = "default"),
            vao = sphere.create_vao(),
        )

        super().__init__(mesh)

    def transform(self, time):
        self.scale((3.0, 3.0, 3.0))

        self.rotate(time * 30, (-1, 1, 0))

class RotatingSphere(Node):

    def __init__(self):
        sphere = Sphere(
            color = (0.0, 0.0, 1.0),
            depth = 4
        )

        mesh = Mesh(
            program = ProgramLoader.load(both = "default"),
            vao = sphere.create_vao(),
        )

        super().__init__(mesh)

    def transform(self, time):
        radius = 4 

        self.translate((
            radius * glm.sin(time),
            0,
            radius * glm.cos(time)
        ))

        self.rotate(time * 30, (-1, 1, 0))

class RotatingSphere2(Node):

    def __init__(self):
        sphere = Sphere(
            color = (1.0, 0.0, 0.0),
            depth = 4
        )

        mesh = Mesh(
            program = ProgramLoader.load(both = "default"),
            vao = sphere.create_vao(),
        )

        super().__init__(mesh)

    def transform(self, time):
        radius = 4 

        self.translate((
            0,
            radius * glm.sin(time),
            radius * glm.cos(time)
        ))

        self.rotate(time * 30, (-1, 1, 0))

class RotatingSphere3(Node):

    def __init__(self):
        sphere = Sphere(
            color = (0.0, 1.0, 0.0),
            depth = 4
        )

        mesh = Mesh(
            program = ProgramLoader.load(both = "default"),
            vao = sphere.create_vao(),
        )

        super().__init__(mesh)

    def transform(self, time):
        radius = 4 

        self.translate((
            radius * glm.sin(time),
            radius * glm.cos(time),
            0,
        ))

        self.rotate(time * 30, (-1, 1, 0))

