from numba import njit
import numpy as np 
import glm
import math

# resolution
WIN_RES = glm.vec2(1600,900)

# Background Color RGB scale 0.0 to 1.0
BG_Color = glm.vec3(0.1, 0.16, 0.25)