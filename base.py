import glm

class Scene:
    """
    Uma cena contém uma câmera e um conjunto de objetos 3D. Ela é responsável por
    renderizar todos os objetos levando em consideração a configuração da câmera.
    """

    def __init__(self, camera, nodes):
        self._camera = camera
        self._nodes = nodes

    def render(self, time):
        view, projection = self._camera.view, self._camera.projection

        for node in self._nodes:
            node.mesh.program["view"].write(view)
            node.mesh.program["projection"].write(projection)
            node.render(time)

class Camera:
    """
    Representa uma câmera. Contém informações sobre sua posição, para onde ela
    está olhando e qual é o vetor que representa o "cima" da câmera. 
    """

    def __init__(self):
        self._eye = (0, 0, 0)
        self._center = (0, 0, 0)
        self._up = (0, 1, 0)

        self._projection = glm.perspective(
            glm.radians(45),
            1.0,
            0.1,
            100.0
        )

    def look_at(self, vector):
        self._center = vector

    def move_to(self, vector):
        self._eye = vector

    @property
    def view(self):
        return glm.lookAt(
            glm.vec3(*self._eye),
            glm.vec3(*self._center),
            glm.vec3(*self._up)
        )

    @property
    def projection(self):
        return self._projection 

class Node:
    """
    Representa um objeto 3D e suas transformações geométricas (translação, rotação
    e escala).
    """

    def __init__(self, mesh):
        self._mesh = mesh
        self._model = glm.mat4(1.0)

    def translate(self, vector):
        self._model = glm.translate(
            self._model,
            glm.vec3(*vector)
        )
        return self

    def rotate(self, angle, axis):
        self._model = glm.rotate(
            self._model,
            glm.radians(angle),
            glm.vec3(*axis)
        )
        return self

    def scale(self, vector):
        self._model = glm.scale(
            self._model,
            glm.vec3(*vector)
        )
        return self

    def reset(self):
        self._model = glm.mat4(1.0)

    @property
    def mesh(self):
        return self._mesh

    def transform(self, time):
        raise NotImplementedError
    
    def render(self, time):
        self.transform(time)
        self._mesh.program["model"].write(self._model)
        self._mesh.render()
        self.reset()

class Mesh:
    """
    Contém informações sobre o programa de shaders e a geometria do objeto 3D a
    ser renderizado.
    """

    def __init__(self, program, vao):
        self._program = program
        self._vao = vao

    def render(self):
        self._vao.render(self._program)

    @property
    def program(self):
        return self._program
