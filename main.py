#!/usr/local/env python3
import sys, logging, os, random, open_color, assets, arcade
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Constants
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 900
MARGIN = 50
SCREEN_TITLE = "Space Shooter Game"

SHIP_HP = 100
SHIP_SCALE = 1

NUM_ENEMIES = 5
ENEMY_SCALE = 0.5
ENEMY_MIN_Y = 400
ENEMY_MIN_HP = 10
ENEMY_MAX_HP = 50
ENEMY_MIN_MASS = 10
ENEMY_MAX_MASS = 100
ENEMY_ACCELERATION = 10


class Player(arcade.Sprite):
    def __init__(self, image, scale, x, y):
        super().__init__(image, scale)
        self.center_x = x
        self.center_y = y
        self.dx = 0
        self.dy = 0
        self.target_x = x
        self.target_y = y

class Enemy(arcade.Sprite):
    def __init__(self, x, y, mass, hp):
        sprites = ['enemy_01','enemy_02','enemy_03','enemy_04','enemy_05','enemy_06','enemy_07','enemy_08','enemy_09']
        sprite = random.choice(sprites)
        super().__init__("assets/{}.png".format(sprite), ENEMY_SCALE)
        self.center_x = x
        self.center_y = y
        self.hp = hp
        self.mass = mass
        self.dx = 0
        self.dy = 0
        self.target_x = x
        self.target_y = y
        self.acceleration = ENEMY_ACCELERATION / self.mass

class window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        self.set_mouse_visible(True)
        
        arcade.set_background_color(open_color.blue_4)

        elf.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()


    def setup(self):
        self.playing = True
        self.score = 0.0
        self.hp = SHIP_HP

        self.player = Player("assets/player.png",SHIP_SCALE<400,50)
        self.player_list.append(self.player)
        for e in range(NUM_ENEMIES):
            x = random.randint(MARGIN,SCREEN_WIDTH-MARGIN)
            y = random.randint(SCREEN_HEIGHT-ENEMY_MIN_Y,SCREEN_HEIGHT-MARGIN)
            hp = random.randing(ENEMY_MIN_HP,ENEMY_MAX_HP)
            mass = random.randint(ENEMY_MIN_MASS,ENEMY_MAX_MASS)
            enemy = Enemy(x, y, mass, hp)
            self.enemy_list.appent(enemy)

    def update(self, delta_time)
        pass

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.enemy_bullet_list.draw()


    def on_mouse_motion(self, x, y, dx, dy):
        pass


def main():
    window = window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    pass

if __name__ == "__main__":
    main()