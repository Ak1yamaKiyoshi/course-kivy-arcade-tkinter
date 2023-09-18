import arcade 
from math import sqrt

class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)
        arcade.set_background_color(arcade.color.BLACK)

        self.player_x = 100
        self.player_y = 200
        self.player_speed = 250
        
        self.right = False
        self.left = False
        self.down = False
        self.up = False
        
        self.sprite1 = arcade.Sprite("idk.png", center_x = 100, center_y = 100)
        
        
        
    def on_draw(self):
        arcade.start_render()
        self.sprite1.draw()
        
    def on_update(self, delta_time):
        
        if self.right:
            self.sprite1.turn_right(2)
            #self.player_x += self.player_speed * delta_time
        if self.left:
            self.sprite1.turn_left(2)
            #self.player_x -= self.player_speed * delta_time
        if self.up:
            self.sprite1.strafe(0.1)
            #self.player_y += self.player_speed * delta_time
        if self.down:
            pass
            #self.player_y -= self.player_speed * delta_time

        self.sprite1.update()
        #self.sprite1.set_position(self.player_x, self.player_y)
        

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = True
        if symbol == arcade.key.LEFT:
            self.left = True
        if symbol == arcade.key.DOWN:
            self.down = True
        if symbol == arcade.key.UP:
            self.up = True
    
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = False
        if symbol == arcade.key.LEFT:
            self.left = False
        if symbol == arcade.key.DOWN:
            self.down = False
        if symbol == arcade.key.UP:
            self.up = False

Window(1280, 720, 'Window')
arcade.run()