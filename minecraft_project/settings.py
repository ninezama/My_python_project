from numba import njit
import numpy as np 
import glm
import math

# resolution
WIN_RES = glm.vec2(1600,900)

#Chunk
CHUNK_SIZE = 32
H_CHUNK_SIZE = CHUNK_SIZE // 2
CHUNK_AREA = CHUNK_SIZE * CHUNK_SIZE
CHUNK_VOL = CHUNK_AREA * CHUNK_SIZE

# Camera 
ASPECT_RATIO = WIN_RES.x/WIN_RES.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG) # VERTICAL FOV
H_FOX = 2*math.atan(math.tan(V_FOV*0.5)*ASPECT_RATIO) # HORIZONTAL FOV
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89)

# Player
PLAYER_SPEED = 0.005
PLAYER_RUN_RATIO = 1.5
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(H_CHUNK_SIZE, CHUNK_SIZE, 1.5*CHUNK_SIZE)
MOUSE_SENSITIVITY = 0.002


 
# Background Color RGB scale 0.0 to 1.0
BG_Color = glm.vec3(0.1, 0.16, 0.25)