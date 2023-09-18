import arcade 
from math import sqrt

class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)
        arcade.set_background_color(arcade.color.BLACK)
        self.green_x = 100
        self.green_y = 100
        self.blue_x = 200
        self.blue_y = 200
        self.yellow_x = 300
        self.yellow_y = 300
        self.vel_x = 0
        self.vel_y = 0
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.green_x, self.green_y, 50, arcade.color.GREEN, 20)
        arcade.draw_circle_filled(self.blue_x, self.blue_y, 50, arcade.color.BLUE, 20)
        arcade.draw_circle_filled(self.yellow_x, self.yellow_y, 50, arcade.color.YELLOW, 20)
    
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.green_x = x
            self.green_y = y
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.blue_x = x
            self.blue_y = y
        if button == arcade.MOUSE_BUTTON_MIDDLE:
            self.yellow_x = x
            self.yellow_y = y
    
    def on_mouse_motion(self, x, y, dx, dy):
        self.vel_x = x
        self.vel_y = y
    
    def on_update(self, delta_time):
        self.move_yellow_circle()
    
    def move_yellow_circle(self):
        x_dist = self.vel_x - self.yellow_x
        y_dist = self.vel_y - self.yellow_y
        
        distance = sqrt(x_dist * x_dist + y_dist * y_dist)
        if distance > 1:
            self.yellow_x += x_dist * 0.1
            self.yellow_y += y_dist * 0.1

            
Window(1280, 720, 'Window')
arcade.run()