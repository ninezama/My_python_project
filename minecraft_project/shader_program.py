import os
from settings import *
class ShaderProgram:
    def __init__(self,app):
        self.app = app
        self.ctx = app.ctx
        
        #-----------------------------Players-----------------------------#
        self.player = app.player
        
        #-----------------------------shaders-----------------------------#
        # for quad
        #self.quad = self.get_program(shader_name='quad' )
        self.chunk = self.get_program(shader_name='chunk' )
        #-----------------------------------------------------------------#
        self.set_uniform_on_init()
        
    def set_uniform_on_init(self):
        #for quad
        #self.quad['m_proj'].write(self.player.m_proj)
        #self.quad['m_model'].write(glm.mat4())
        self.chunk['m_proj'].write(self.player.m_proj)
        self.chunk['m_model'].write(glm.mat4())
    def update(self):
        #for quad
        #self.quad['m_view'].write(self.player.m_view)
        self.chunk['m_view'].write(self.player.m_view)
        
        
    def get_program(self,shader_name):
        path = os.path.dirname(os.path.abspath(__file__))
        with open(path + f'\\shaders\\{shader_name}.vert') as file:
            vertex_shader = file.read()
        with open(path + f'\\shaders\\{shader_name}.frag') as file:
            fragment_shader = file.read()
            
        program = self.ctx.program(vertex_shader=vertex_shader,fragment_shader=fragment_shader)
        return program
            