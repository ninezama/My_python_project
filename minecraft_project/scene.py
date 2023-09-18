from settings import *
from meshes.quad_mesh import QuadMesh
from world import World
class Scene:
    def __init__(self, app):
        self.app = app
        # scene of QuadMesh 
        #self.quad = QuadMesh(self.app) 
        self.world = World(self.app)
    def update(self):
        self.world.update()
    def render(self):
        # scene of QuadMesh
        #self.quad.render()
        self.world.render()    