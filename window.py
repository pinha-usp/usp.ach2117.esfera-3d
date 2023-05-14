from pathlib import Path

import moderngl_window as mglw
from moderngl_window.opengl.vao import VAO

from base import Scene, Camera
from nodes import FixedSphere, RotatingSphere, RotatingSphere2, RotatingSphere3

class Window(mglw.WindowConfig):

    gl_version = (3, 3)
    title = "Sphere"
    fullscreen = True
    resource_dir = Path("resources")
    aspect_ratio = 1.0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        camera = Camera()
        camera.move_to((0, 0, 15))

        self.scene = Scene(
            camera = camera, 

            nodes = [
                FixedSphere(),
                RotatingSphere(),
                RotatingSphere2(),
                RotatingSphere3()
            ]
        )

    def render(self, time, frametime):
        self.ctx.clear()

        self.ctx.enable(self.ctx.DEPTH_TEST)

        self.scene.render(time)
