import glm
from moderngl_window.opengl.vao import VAO
import moderngl as mgl

class Mesh:

    def __init__(self, program, shape):
        self._program = program
        self._shape = shape
        self._model = glm.mat4(1.0)
        self._init_vao()

    def _init_vao(self):
        self._vao = VAO(mode = mgl.POINTS)
        self._vao.buffer(self._shape.vertices, "3f", "position")

    def translate(self, vector):
        self._model = glm.translate(self._model, vector)
        return self

    def rotate(self, angle, axis):
        self._model = glm.rotate(self._model, glm.radians(angle), axis)
        return self

    def scale(self, vector):
        self._model = glm.scale(self._model, vector)
        return self

    def reset(self):
        self._model = glm.mat4(1.0)
        return self

    def draw(self, view, projection):
        self._program["model"].write(self._model)
        self._program["view"].write(view)
        self._program["projection"].write(projection)

        self._vao.render(self._program)
