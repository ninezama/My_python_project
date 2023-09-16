import pygame as pg 
from OpenGL.GL import *

class App:
    def __init__(self,WIDTH=1200,HEIGHT=900):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT),pg.OPENGL|pg.DOUBLEBUF)
        #initialize the opengl 
        glClearColor(0.1,0.2,0.2,1)
        self.clock = pg.time.Clock()
        self.running = True
        self.FPS = 60
        self.mainloop()
    def mainloop(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False
            #refresh screen
            glClear(GL_COLOR_BUFFER_BIT)
            
            pg.display.flip()            
            self.clock.tick(self.FPS)
        self.quit()
    def quit(self):
        pg.quit()
        
if __name__ == "__main__":
    app = App()
    app.mainloop()

