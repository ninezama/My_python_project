from settings import *
from meshes.quad_mesh import QuadMesh
from world_objects.chunk import Chunk
class Scene:
    def __init__(self, app):
        self.app = app
        # scene of QuadMesh 
        #self.quad = QuadMesh(self.app) 
        self.chunk = Chunk(self.app)
    def update(self):
        pass
    def render(self):
        # scene of QuadMesh
        #self.quad.render()
        self.chunk.render()    