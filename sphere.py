import numpy as np

class Sphere:

    def __init__(self, depth: int):
        self.depth = depth
        self._generate_vertices()

    def _generate_vertices(self):
        self._vertices = []

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
            self._generate_triangle(*triangle, self.depth)

        self._vertices = np.array(self._vertices, dtype = np.float32)

    def _generate_triangle(
        self,
        v1: tuple,
        v2: tuple,
        v3: tuple,
        depth: int
    ):
        if depth == 0:
            self._vertices.extend([*v1, *v2, *v3])
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
            self._generate_triangle(*subtriangle, depth - 1)

    def _normalize(self, v: tuple) -> tuple:
        return v / np.linalg.norm(v)

    def _middle_point(self, v1: tuple, v2: tuple) -> tuple:
        return tuple(
            (v1[i] + v2[i]) / 2
            for i
            in range(3)
        )

    @property
    def vertices(self) -> np.ndarray:
        return self._vertices

