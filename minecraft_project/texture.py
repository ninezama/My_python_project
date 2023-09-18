import pygame as pg 
import moderngl as mgl
import os
class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
    
        # loaf texture
        self.texture_0 = self.load('frame.png')

        # assign texture unit
        self.texture_0.use(location=0)

    def load(self, filename):
        path = os.path.dirname(os.path.abspath(__file__))
        texture = pg.image.load(f'{path}\\assets\\{filename}')
        texture = pg.transform.flip(texture,flip_x=True,flip_y=False)

        texture = self.ctx.texture(
            size= texture.get_size(),
            components = 4,
            data= pg.image.tostring(texture,'RGBA',False)
            )
        texture.anisotropy = 32.0
        texture.build_mipmaps()
        # Before implement use filter (mgl.LINEAR_MIPMAP_LINEAR,mgl.LINEAR)
        texture.filter = (mgl.NEAREST,mgl.NEAREST)
        return texture
