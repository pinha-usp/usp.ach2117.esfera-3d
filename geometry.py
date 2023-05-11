class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def subdivide(self) -> list:
        midpoints = []

        for edge in [
            (self.a, self.b),
            (self.b, self.c),
            (self.c, self.a)
        ]:
            vec1 = edge[0]
            vec2 = edge[1]

            midpoints.append([
                (vec1[i] + vec2[i]) / 2
                for i
                in range(3)
            ])

        ab = midpoints[0]
        bc = midpoints[1]
        ac = midpoints[2]

        return [
            Triangle(self.a, ab, ac),
            Triangle(ab, self.b, bc),
            Triangle(ac, bc, self.c),
            Triangle(ab, bc, ac)
        ]

import numpy as np

class Sphere:

    def __init__(self, depth):
        self.depth = depth 

        octa = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, -1]
        ]

        self.triangles = [
            Triangle(octa[0], octa[1], octa[2]),
            Triangle(octa[0], octa[1], octa[5]),
            Triangle(octa[0], octa[2], octa[4]),
            Triangle(octa[0], octa[4], octa[5]),
            Triangle(octa[1], octa[2], octa[3]),
            Triangle(octa[1], octa[3], octa[5]),
            Triangle(octa[2], octa[3], octa[4]),
            Triangle(octa[3], octa[4], octa[5])
        ]

        self.__calculate_subdivisions()
        self.__calculate_vertices()
        self.__normalize_vertices()

    def __calculate_subdivisions(self):
        self.vertices = []

        base_triangles = self.triangles.copy()

        for triangle in base_triangles:
            self.__subdivide(triangle, self.depth)

    def __subdivide(self, triangle, depth):
        if depth == 0:
            return

        subtriangles = triangle.subdivide()

        self.triangles.extend(subtriangles)

        for subtriangle in subtriangles:
            self.__subdivide(subtriangle, depth - 1)

    def __calculate_vertices(self):
        self.vertices = []

        for triangle in self.triangles:
            self.vertices.extend([triangle.a, triangle.b, triangle.c])

        self.vertices = np.array(self.vertices, dtype = np.float32)

    def __normalize_vertices(self):
        radius = 1

        for i in range(len(self.vertices)):
            vertice = self.vertices[i]

            direction = vertice / np.linalg.norm(vertice)

            self.vertices[i] = radius * direction

