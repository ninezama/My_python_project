from settings import *
import moderngl as mgl
import pygame as pg
import sys
from shader_program import ShaderProgram
from scene import Scene
from player import Player
class VoxelEngine():
    def __init__(self):
        #----- app init --------------------------------#
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE,24)
        
        pg.display.set_mode(WIN_RES ,flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = 'auto'
        
        self.clock = pg.time.Clock()
        self.delta_time = 0.0 
        self.time = 0.0
        
        
        #---- pygame settings --------------------------------#
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        
        self.is_running = True
        #---- shader initialization --------------------------------#
        self.on_init()
        
    def on_init(self):
        self.player = Player(self)
        self.shader_program = ShaderProgram(self) 
        self.scene = Scene(self)
        
    def update(self):
        #------ player update --------------------------------#
        self.player.update()
        #------ shader update --------------------------------#
        self.shader_program.update()
        #------ scene update --------------------------------#
        self.scene.update()
        #-------app update --------------------------------#
        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks()*0.001
        pg.display.set_caption(f'{self.clock.get_fps() :.2f}')
        
        1
    def render(self):
        #----- app render --------------------------------#
        self.ctx.clear(color=BG_Color)
        #----- scene render --------------------------------#
        self.scene.render()
        #----- shader render --------------------------------#
        #self.shader_program.render()
        pg.display.flip()
        
    def handle_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or ( event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE ):
                self.is_running = False
    def run(self):
        while self.is_running:
            self.handle_event()
            self.update()
            self.render()
        pg.quit()
        sys.exit()
    
if __name__ == '__main__':
    app = VoxelEngine()
    app.run()