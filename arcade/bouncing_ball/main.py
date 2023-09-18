import arcade 

class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)
        
        arcade.set_background_color(arcade.color.BLACK)
        
        self.c_x = 100
        self.c_y = 100     
        
        self.x_speed = 500
        self.y_speed = 500
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.c_x,self.c_y, 50, arcade.color.GREEN, 10)
    
    def on_update(self, delta_time):
        self.c_y += self.y_speed*delta_time
        self.c_x += self.x_speed*delta_time
        
        if self.c_x > 1280 - 50 or self.c_x < 0 + 50:
            self.x_speed *=-0.98
        if self.c_y > 720 - 50 or self.c_y < 0 + 50:
            self.y_speed *=-1.1
    
Window(1280, 720, 'Window')
arcade.run()