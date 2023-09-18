import arcade 
import random

class Circle():
    def __init__(self, x, y, dx, dy, color):
        self.pos = [x, y]
        self.speed = [dx, dy]
        self.color = color
    
    def update(self, delta_time):
        self.pos[0] += self.speed[0]*delta_time
        self.pos[1] += self.speed[1]*delta_time
        
        if self.pos[0] > 1280 - 50 or self.pos[0] < 0 + 50:
            self.speed[0]*=-1
        if self.pos[1] > 720 - 50 or self.pos[1] < 0 + 50:
            self.speed[1]*=-1
            
    def draw(self):
        arcade.draw_circle_filled(self.pos[0],self.pos[1], 50, arcade.color.RED, 10)

class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(0, 0)
        
        arcade.set_background_color(arcade.color.BLACK)

        self.balls = []
        for i in range(7):
            self.balls.append(Circle(50+(100*i), 50+(100*i), random.randint(200, 800), random.randint(200, 800), "RED"))

    def check_collisions(self):
        for index1, i in enumerate(self.balls):
            for index2, j in enumerate(self.balls):
                if index1 != index2:
                    if j.pos[0] >= i.pos[0] - 50 and j.pos[0] <= i.pos[0] + 50:
                        if j.pos[1] >= i.pos[1] - 50 and j.pos[1] <= i.pos[1] + 50:
                            j.speed[0] *=-1
                            j.speed[1] *=-1

    def on_draw(self):
        arcade.start_render()
        for i in self.balls:
            i.draw()

    def on_update(self, delta_time):
        for i in self.balls:
            i.update(delta_time)
        self.check_collisions()
    
Window(1280, 720, 'Window')
arcade.run()