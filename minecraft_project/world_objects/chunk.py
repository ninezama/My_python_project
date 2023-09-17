from settings import *
from meshes.chunk_mesh import ChunkMesh
class Chunk:
    def __init__(self,app):
        self.app = app
        self.voxels: np.array = self.build_voxels()
        self.mesh: ChunkMesh = None
        self.build_mesh()
    
    def build_mesh(self):
        self.mesh = ChunkMesh(self)
        
    def render(self):
        self.mesh.render()
    
        
        
        
    def build_voxels(self):
        #empty chunk
        voxels = np.zeros(CHUNK_VOL, dtype=np.uint8) # uint8 for 0-255
        
        #Fill chunk By draw end of chunk as 1
        for x in range(CHUNK_SIZE):
            for y in range(CHUNK_SIZE):
                for z in range(CHUNK_SIZE):
                    voxels[x+CHUNK_SIZE*z+CHUNK_AREA*y] = x+y+z
        
        return voxels
        