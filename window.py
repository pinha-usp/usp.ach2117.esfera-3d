from pathlib import Path

import glm
import moderngl_window as mglw
from moderngl_window.opengl.vao import VAO

from mesh import Mesh
from sphere import Sphere
from loader import ProgramLoader

class Window(mglw.WindowConfig):

    gl_version = (3, 3)
    title = "Sphere"
    fullscreen = True
    resource_dir = Path("resources")
    aspect_ratio = 1.0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mesh = Mesh(
            program = ProgramLoader.load(
                both = "default"
            ),

            shape = Sphere(
                depth = 4,
                color = (0.0, 1.0, 0.0)
            ),
        )

        self.mesh2 = Mesh(
            program = ProgramLoader.load(
                both = "default"
            ),

            shape = Sphere(
                depth = 4,
                color = (1.0, 1.0, 0.0)
            ),
        )

        self.projection = glm.perspective(
            glm.radians(45),
            1.0,
            0.1,
            100.0
        )

        self.view = glm.lookAt(
            glm.vec3(0, 0, 50),
            glm.vec3(0, 0, 0),
            glm.vec3(0, 1, 0)
        )

    def render(self, time, frametime):
        self.ctx.clear()

        self.ctx.enable(self.ctx.DEPTH_TEST)

        (
            self.mesh
            .translate((10 * glm.sin(time), 0, 10 * glm.cos(time)))
            .rotate(time * -90, (1, 1, 0))
        )

        (
            self.mesh2
            .scale((3.0, 3.0, 3.0))
            .rotate(time * -90, (1, 1, 0))
        )

        self.mesh.draw(
            view = self.view,
            projection = self.projection
        )

        self.mesh2.draw(
            view = self.view,
            projection = self.projection
        )

        self.mesh.reset()
        self.mesh2.reset()
