import arcade


class Rectangle:
    pass

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title='анимация')
        self.background_color = (255, 255, 255)
        self.texture = arcade.load_texture("rabbit.jpg")

        self.x = 100
        self.y = 100
        self.radius = 30
        self.color = arcade.color.YELLOW
        self.change_x = 3
        self.change_y = 4
        self.change_x = 3


    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(
            center_x=400,
            center_y=300,
            width=800,
            height=600,
            texture=self.texture
        )
        arcade.draw_circle_outline(self.x, self.y, self.radius, self.color)


    def setup(self):
        pass

    def update(self, delta_time: float):
        self.x += self.change_x
        self.y += self.change_y
        if self.x + self.radius / 2 > 800 or self.x - self.radius / 2 < 0:
            self.change_x = - self.change_x
        if self.y + self.radius / 2 > 600 or self.y - self.radius / 2 < 0:
            self.change_y = - self.change_y



    def change_size(self):
        if self.x + self.w / 2 >= SCREEN_WIDTH or self.x - self.w / 2 <= 0:
            self.w += 2
            self.h += 2

if __name__=='__main__':
    game = Game()
    game.setup()
    arcade.run()










