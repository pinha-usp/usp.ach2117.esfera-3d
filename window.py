from pathlib import Path
import moderngl_window as mglw

class Window(mglw.WindowConfig):

    gl_version = (3, 3)
    title = "Sphere"
    fullscreen = True
    resource_dir = Path("resources") 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def render(self, time, frametime):
        self.ctx.clear()
