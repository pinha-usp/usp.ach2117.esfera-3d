from pathlib import Path
import glm
import moderngl_window as mglw
from moderngl_window.opengl.vao import VAO
from sphere import Sphere

class Window(mglw.WindowConfig):

    gl_version = (3, 3)
    title = "Sphere"
    fullscreen = True
    resource_dir = Path("resources")
    aspect_ratio = 1.0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.program = self.load_program(
            vertex_shader="shaders/default.vert",
            fragment_shader="shaders/default.frag",
        )

        sphere = Sphere(depth = 4)

        self.vao = VAO(mode = self.ctx.POINTS)
        self.vao.buffer(sphere.vertices, "3f", ["in_vert"])

        self.program["perspective"].write(
            glm.perspective(
                glm.radians(45),
                1.0,
                0.1,
                100.0
            )
        )

    def render(self, time, frametime):
        self.ctx.clear()

        self.ctx.enable(self.ctx.DEPTH_TEST)

        self.program["model"].write(
            glm.rotate(
                glm.mat4(1.0),
                glm.radians(time * 45),
                glm.vec3(0, 1, 0)
            )
        )

        self.program["view"].write(
            glm.lookAt(
                glm.vec3(2, 2, 2),
                glm.vec3(0, 0, 0),
                glm.vec3(0, 1, 0)
            )
        )

        self.vao.render(self.program)
