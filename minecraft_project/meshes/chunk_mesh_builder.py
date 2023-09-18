from settings import *

def is_void(voxels_pos, chunk_voxels):
    x,y,z = voxels_pos
    if 0 <= x < CHUNK_SIZE and 0 <= y < CHUNK_SIZE and 0 <= z < CHUNK_SIZE:
        if chunk_voxels[x+z*CHUNK_SIZE+y*CHUNK_AREA]:
            return False
    return True

def add_data(vertex_data,   index, *vertices):
    for vertex in vertices:
        for attr in vertex:
            vertex_data[index] = attr
            index += 1
    return index

def build_chunk_mesh(chunk_voxels, format_size):
    # main idea is build the chunk just visible surfaces
    # ARRAT_SIZE = CHUNK_VOLUME * NUM_VOXELS_VERTICLES * VERTEXS_ATTRS
    # NUM_VOXELS_VERTICLES is the number of possible to see voxels of rectangle and it's 18
    # VERTEXS_ATTRS the vertex attributes include of x,y,z,voxels_id and face_id 5 attrs of choose format_size
    vertex_data = np.empty(CHUNK_VOL*18*format_size, dtype='uint8')    
     
    
    index = 0
    for x in range(CHUNK_SIZE):
        for y in range(CHUNK_SIZE):
            for z in range(CHUNK_SIZE):
                voxel_id = chunk_voxels[x+z*CHUNK_SIZE+y*CHUNK_AREA]
                # ignore the border line
                if not voxel_id:
                    continue
                
                # Top face
                if is_void((x ,y+1, z),chunk_voxels):
                    # format: x, y, z, voxel_id, face_id
                    # 4 corners of top face
                    # face id is 0
                    v0 = (x     ,       y+1 ,    z      ,  voxel_id ,    0)
                    v1 = (x+1   ,       y+1 ,    z      ,  voxel_id ,    0)
                    v2 = (x+1   ,       y+1 ,    z+1    ,  voxel_id ,    0)
                    v3 = (x     ,       y+1 ,    z+1    ,  voxel_id ,    0)
                    
                    # relation ship by diagram below
        
                    # v0--------v1
                    #  |^ ->    /|
                    #  ||   |  / |
                    #  | <- V /  |
                    #  |     /   |
                    #  |    /    |
                    #  |   /     |
                    #  |  /^ ->  |
                    #  | / |   | |
                    #  |/   <- V |
                    # v3--------v2
                    #

                    index = add_data(vertex_data, index, v0, v3, v2, v0, v2, v1)
                    
                # Bottom face
                if is_void((x,y-1,z),chunk_voxels):
                    # face id is 1
                    v0 = (x     ,       y ,    z      ,  voxel_id ,    1)
                    v1 = (x+1   ,       y ,    z      ,  voxel_id ,    1)
                    v2 = (x+1   ,       y ,    z+1    ,  voxel_id ,    1)
                    v3 = (x     ,       y ,    z+1    ,  voxel_id ,    1)
                    
                    index = add_data(vertex_data, index, v0, v2, v3, v0, v1, v2)   
                     
                # Right face
                if is_void((x+1,y,z),chunk_voxels):
                    # face id is 2
                    v0 = (x+1   ,       y   ,    z      ,  voxel_id ,    2)
                    v1 = (x+1   ,       y+1 ,    z      ,  voxel_id ,    2)
                    v2 = (x+1   ,       y+1 ,    z+1    ,  voxel_id ,    2)
                    v3 = (x+1   ,       y   ,    z+1    ,  voxel_id ,    2)
                    
                    index = add_data(vertex_data, index, v0, v1, v2, v0, v2, v3)   
                      
                # Left face
                if is_void((x-1,y,z),chunk_voxels):
                    # face id is 3
                    v0 = (x   ,       y   ,    z      ,  voxel_id ,    3)
                    v1 = (x   ,       y+1 ,    z      ,  voxel_id ,    3)
                    v2 = (x   ,       y+1 ,    z+1    ,  voxel_id ,    3)
                    v3 = (x   ,       y   ,    z+1    ,  voxel_id ,    3)
                    
                    index = add_data(vertex_data, index, v0, v2, v1, v0, v3, v2)
                    
                # Back face
                if is_void((x,y,z-1),chunk_voxels):
                    # face id is 4
                    v0 = (x   ,       y   ,    z      ,  voxel_id ,    4)
                    v1 = (x   ,       y+1 ,    z      ,  voxel_id ,    4)
                    v2 = (x+1 ,       y+1 ,    z      ,  voxel_id ,    4)
                    v3 = (x+1 ,       y   ,    z      ,  voxel_id ,    4)
                    
                    index = add_data(vertex_data, index, v0, v1, v2, v0, v2, v3)
                    
                # Front face
                if is_void((x,y,z+1),chunk_voxels):
                    # face id is 5
                    v0 = (x   ,       y   ,    z+1      ,  voxel_id ,    5)
                    v1 = (x   ,       y+1 ,    z+1      ,  voxel_id ,    5)
                    v2 = (x+1 ,       y+1 ,    z+1      ,  voxel_id ,    5)
                    v3 = (x+1 ,       y   ,    z+1      ,  voxel_id ,    5)
                    
                    index = add_data(vertex_data, index, v0, v2, v1, v0, v3, v2)
                    
    return vertex_data[:index + 1]