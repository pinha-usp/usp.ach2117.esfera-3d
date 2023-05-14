import numpy as np
import moderngl as mgl
from moderngl_window.opengl.vao import VAO

class Shape:

    def __init__(self, mode):
        self._init_positions()
        self._init_colors()
        self._mode = mode

    def _init_positions(self):
        raise NotImplementedError
    
    def _init_colors(self):
        raise NotImplementedError

    def create_vao(self) -> VAO:
        vao = VAO(mode = self._mode)

        vao.buffer(
            buffer = np.array(self._positions, dtype = np.float32),
            buffer_format = "3f",
            attribute_names = ["in_position"]
        )

        vao.buffer(
            buffer = np.array(self._colors, dtype = np.float32),
            buffer_format = "3f",
            attribute_names = ["in_color"]
        )

        return vao

class Sphere(Shape):

    def __init__(self, color, depth: int):
        self._color = color
        self._depth = depth

        super().__init__(mode = mgl.POINTS)

    def _init_positions(self):
        self._positions = []

        v1, v2, v3, v4, v5, v6 = (
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (-1, 0, 0),
            (0, -1, 0),
            (0, 0, -1)
        )

        for triangle in [
            (v2, v1, v3),
            (v2, v1, v6),
            (v2, v4, v6),
            (v2, v3, v4),
            (v5, v1, v3),
            (v5, v1, v6),
            (v5, v4, v6),
            (v5, v3, v4)
        ]:
            self._calculate_triangle(*triangle, self._depth)

    def _calculate_triangle(
        self,
        v1: tuple,
        v2: tuple,
        v3: tuple,
        depth: int
    ):
        if depth == 0:
            self._positions.extend([*v1, *v2, *v3])
            return

        v12 = self._normalize(self._middle_point(v1, v2))
        v23 = self._normalize(self._middle_point(v2, v3))
        v31 = self._normalize(self._middle_point(v3, v1))

        for subtriangle in [
            (v1, v12, v31),
            (v2, v23, v12),
            (v3, v31, v23),
            (v12, v23, v31)
        ]:
            self._calculate_triangle(*subtriangle, depth - 1)

    def _normalize(self, v: tuple) -> tuple:
        return v / np.linalg.norm(v)

    def _middle_point(self, v1: tuple, v2: tuple) -> tuple:
        return tuple(
            (v1[i] + v2[i]) / 2
            for i
            in range(3)
        )

    def _init_colors(self):
        self._colors = [
            self._color
            for _
            in self._positions
        ]
