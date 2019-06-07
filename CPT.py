import arcade
import random


WIDTH = 1365
HEIGHT = 710

current_screen = "menu"

x = 0
y = 0
score = 0

#wall

WALLb_X = 0
WALLb_Y = 1
WALLb_WIDTH = 2
WALLb_HEIGHT = 3
WALLb_COLOR = 4


wallb1 = [692.5, 0, 25, random.randrange(0, HEIGHT-200), arcade.color.MAROON]
wallb2 = [1390, 0, 25, random.randrange(0, HEIGHT-200), arcade.color.MAROON]
bottom_walls = [wallb1, wallb2]

WALLt_X = 0
WALLt_Y = 1
WALLt_WIDTH = 2
WALLt_HEIGHT = 3
WALLt_COLOR = 4


wallt1 = [692.5, wallb1[WALLb_HEIGHT] + 200, 25, HEIGHT - wallb1[WALLb_HEIGHT], arcade.color.MAROON]
wallt2 = [1390, wallb2[WALLb_HEIGHT] + 200, 25, HEIGHT - wallb2[WALLb_HEIGHT], arcade.color.MAROON]
top_walls = [wallt1, wallt2]
up_pressed = False
down_pressed = False

HHB_X = 0
HHB_Y = 1
HHB_WIDTH = 2
HHB_HEIGHT = 3
HHB_COLOR = 4

helihitbox1 = [x + 200, y + 380, 100, -70, arcade.color.BLACK]
helihitbox2 = [x + 200, y + 365, -100, -25, arcade.color.BLACK]
all_hhb = [helihitbox1, helihitbox2]


def update(delta_time):
    global up_pressed, down_pressed, x, y, current_screen, top_walls, bottom_walls, score
    if current_screen == "play":
        if y <= 299.5:
            if up_pressed:
                y += 10
                helihitbox1[HHB_Y] += 10
                helihitbox2[HHB_Y] += 10
        if y >= -290:
            if down_pressed:
                y -= 10
                helihitbox1[HHB_Y] -= 10
                helihitbox2[HHB_Y] -= 10
        for wallb in bottom_walls:
            wallb[WALLb_X] -= 10
            if wallb[WALLb_X] <= -25:
                wallb[WALLb_X] = 1390
                wallb[WALLb_HEIGHT] = random.randrange(0, HEIGHT - 200)
        for wallt in top_walls:
            wallt[WALLt_X] -= 10
            if wallt1[WALLt_X] <= -25:
                wallt1[WALLt_X] = 1390
                wallt1[WALLt_Y] = wallb1[WALLb_HEIGHT] + 200
                wallt1[WALLt_HEIGHT] = HEIGHT - wallb1[WALLb_HEIGHT]
            if wallt2[WALLt_X] <= -25:
                wallt2[WALLt_X] = 1390
                wallt2[WALLt_Y] = wallb2[WALLb_HEIGHT] + 200
                wallt2[WALLt_HEIGHT] = HEIGHT - wallb2[WALLb_HEIGHT]
        if bwall1_is_hit1(wallb1, helihitbox1) == True:
            current_screen = "score"
        if bwall2_is_hit1(wallb2, helihitbox1) == True:
            current_screen = "score"
        if bwall1_is_hit2(wallb1, helihitbox2) == True:
            current_screen = "score"
        if bwall2_is_hit2(wallb2, helihitbox2) == True:
            current_screen = "score"
        if twall1_is_hit1(wallt1, helihitbox1) == True:
            current_screen = "score"
        if twall2_is_hit1(wallt2, helihitbox1) == True:
            current_screen = "score"
        if twall1_is_hit2(wallt1, helihitbox2) == True:
            current_screen = "score"
        if twall2_is_hit2(wallt2, helihitbox2) == True:
            current_screen = "score"
        if score_system(wallb, wallt) == True:
            score += 1
    if current_screen == "reset":
        x = 0
        y = 0
        wallb1[WALLb_X] = 692.5
        wallb2[WALLb_X] = 1390
        wallt1[WALLt_X] = 692.5
        wallt2[WALLt_X] = 1390
        helihitbox1[HHB_X] = x + 200
        helihitbox1[HHB_Y] = y + 380
        helihitbox2[HHB_X] = x + 200
        helihitbox2[HHB_Y] = y + 365
        score = 0
        current_screen = "play"


def score_system(wallb, wallt):
    if (helihitbox1[HHB_X] > wallb[WALLb_X] - 12.5 and helihitbox1[HHB_X] < wallb[WALLb_X] - 3.5 or helihitbox1[HHB_X]
            == wallb[WALLb_X] and helihitbox1[HHB_Y] > wallb[WALLb_Y] + wallb[WALLb_HEIGHT]
           and helihitbox1[HHB_Y] < wallt[WALLt_Y]):
        return True
    else:
        return False



def on_draw():
    global x, y, wall1, score, helihitbox1
    arcade.start_render()
    # Draw in here...
    if current_screen == "menu":
        arcade.draw_text("HOPPY HELICOPTER", HEIGHT/2 - 100, WIDTH/4, arcade.color.BLACK,font_size= 60, font_name= "garamond" )
        arcade.draw_text("Press space to play", HEIGHT/2 - 100, WIDTH/4.5, arcade.color.BLACK, font_name = "garamond")
        arcade.draw_text("Press I to read instructions" , HEIGHT/2 - 100, WIDTH/5, arcade.color.BLACK, font_name = "garamond")
    if current_screen == "play":
        draw_helicopter(x, y)
        draw_helihitbox(helihitbox1)
        draw_helihitbox(helihitbox2)
        for wallb in bottom_walls:
            draw_wallb(wallb)
        for wallt in top_walls:
            draw_wallt(wallt)
        arcade.draw_text("score", 20, 690, arcade.color.BLACK)
    if current_screen == "Instruction":
        arcade.draw_text("Welcome to Hoppy Helecopter! To move your helicopter use W for up and S for down.", HEIGHT/2, WIDTH/2 - 40, arcade.color.BLACK)
        arcade.draw_text("You can use the esc key to leave the game at any time", HEIGHT/2, WIDTH/2 - 60, arcade.color.BLACK)
        arcade.draw_text("Press ESC for main menu", HEIGHT / 10, WIDTH / 2 - 40, arcade.color.BLACK)
        arcade.draw_text("KEYBOARD DIAGRAM:", HEIGHT / 10, WIDTH / 2 - 120, arcade.color.BLACK)
        arcade.draw_xywh_rectangle_outline(450, 480, 100, 100, arcade.color.BLACK)
        arcade.draw_xywh_rectangle_outline(450, 360, 100, 100, arcade.color.BLACK)
        arcade.draw_xywh_rectangle_outline(300, 480, 100, 100, arcade.color.BLACK)
        arcade.draw_xywh_rectangle_outline(600, 360, 400, 100, arcade.color.BLACK)
        arcade.draw_text("SPACE", HEIGHT + 50, WIDTH / 2 - 280, arcade.color.BLACK)
        arcade.draw_text("S", HEIGHT - 220, WIDTH / 2 - 280, arcade.color.BLACK)
        arcade.draw_text("W", HEIGHT - 220, WIDTH / 2 - 160, arcade.color.BLACK)
        arcade.draw_text("ESC", HEIGHT / 2.14, WIDTH / 2 - 160, arcade.color.BLACK)
        arcade.draw_text("ESC = Escape To Menu", HEIGHT / 10, WIDTH / 3, arcade.color.BLACK)
        arcade.draw_text("W = Up:", HEIGHT / 10, WIDTH / 3 - 30, arcade.color.BLACK)
        arcade.draw_text("S = DOWN:", HEIGHT / 10, WIDTH / 3 - 60, arcade.color.BLACK)
        arcade.draw_text("SPACE = START:", HEIGHT / 10, WIDTH / 3 - 90, arcade.color.BLACK)
    if current_screen == "score":
        print(score)

def on_key_press(key, modifiers):
    global up_pressed, down_pressed, current_screen
    if current_screen == "menu":
        if key == arcade.key.SPACE:
            current_screen = "play"
        if key == arcade.key.I:
            current_screen = "Instruction"
    if current_screen == "Instruction":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"
    if current_screen == "play":
        if key == arcade.key.W:
            up_pressed = True
        if key == arcade.key.S:
            down_pressed = True
        if key == arcade.key.ESCAPE:
            current_screen = "menu"
    if current_screen == "score":
        if key == arcade.key.SPACE:
            current_screen = "reset"
        if key == arcade.key.ESCAPE:
            current_screen = "menu"


def on_key_release(key, modifiers):
    global up_pressed
    if key == arcade.key.W:
        up_pressed = False
    global down_pressed
    if key == arcade.key.S:
        down_pressed = False


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()

# BOTTOM WALL CODE

def draw_wallb(wallb):
    arcade.draw_xywh_rectangle_filled(wallb[WALLb_X],
                                      wallb[WALLb_Y],
                                      wallb[WALLb_WIDTH],
                                      wallb[WALLb_HEIGHT],
                                      wallb[WALLb_COLOR])

# TOP WALL CODE

def draw_wallt(wallt):
    arcade.draw_xywh_rectangle_filled(wallt[WALLt_X],
                                      wallt[WALLt_Y],
                                      wallt[WALLt_WIDTH],
                                      wallt[WALLt_HEIGHT],
                                      wallt[WALLt_COLOR])

# HELICOPTER SHAPES

def draw_helicopter(x, y):
    arcade.draw_xywh_rectangle_filled(x + 200, y + 380, 100, -70, arcade.color.GRAY)
    arcade.draw_xywh_rectangle_filled(x + 250, y + 380, 50, -35, arcade.color.WHITE)
    arcade.draw_xywh_rectangle_filled(x + 200, y + 365, -100, -25, arcade.color.GRAY)
    arcade.draw_triangle_filled(x + 200, y + 380, x + 235, y + 380, x + 200, y + 400, arcade.color.GRAY)
    arcade.draw_circle_filled(x + 200, y + 400, 10, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(x + 205, y + 405, 120, -10, arcade.color.GRAY)
    arcade.draw_xywh_rectangle_filled(x + 195, y + 405, -120, -10, arcade.color.GRAY)
    arcade.draw_triangle_filled(x + 100, y + 365, x + 110, y + 365, x + 100, y + 375, arcade.color.GRAY)
    arcade.draw_circle_filled(x + 100, y + 375, 5, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(x + 102.5, y + 377.5, 25, -5, arcade.color.GRAY)
    arcade.draw_xywh_rectangle_filled(x + 97.5, y + 377.5, -25, -5, arcade.color.GRAY)
    arcade.draw_xywh_rectangle_filled(x + 225, y + 310, 5, -10, arcade.color.GRAY)
    arcade.draw_xywh_rectangle_filled(x + 275, y + 310, -5, -10, arcade.color.GRAY)
    arcade.draw_xywh_rectangle_filled(x + 200, y + 300, 100, -5, arcade.color.GRAY)

# HELICOPTER HITBOX

def draw_helihitbox(helihitbox):
    arcade.draw_xywh_rectangle_outline(helihitbox[HHB_X],
                                      helihitbox[HHB_Y],
                                      helihitbox[HHB_WIDTH],
                                      helihitbox[HHB_HEIGHT],
                                      helihitbox[HHB_COLOR])

# BOTTOM WALL HIT DETECTION

def bwall1_is_hit1(wallb1, helihitbox1):
    if (helihitbox1[HHB_X] and helihitbox1[HHB_X] + helihitbox1[HHB_WIDTH] > wallb1[WALLb_X] and helihitbox1[HHB_X] and helihitbox1[HHB_X] +
            helihitbox1[HHB_WIDTH] < wallb1[WALLb_X] + wallb1[WALLb_WIDTH] and
            helihitbox1[HHB_Y] and helihitbox1[HHB_Y] + helihitbox1[HHB_HEIGHT] > wallb1[WALLb_Y] and helihitbox1[HHB_Y] and helihitbox1[HHB_Y] + helihitbox1[HHB_HEIGHT]
            < wallb1[WALLb_Y] + wallb1[WALLb_HEIGHT]):
        return True
    else:
        return False

def bwall2_is_hit1(wallb2, helihitbox1):
    if (helihitbox1[HHB_X] and helihitbox1[HHB_X] + helihitbox1[HHB_WIDTH] > wallb2[WALLb_X] and helihitbox1[HHB_X] and helihitbox1[HHB_X] +
            helihitbox1[HHB_WIDTH] < wallb2[WALLb_X] + wallb2[WALLb_WIDTH] and
            helihitbox1[HHB_Y] and helihitbox1[HHB_Y] + helihitbox1[HHB_HEIGHT] > wallb2[WALLb_Y] and helihitbox1[HHB_Y] and helihitbox1[HHB_Y] + helihitbox1[HHB_HEIGHT]
            < wallb2[WALLb_Y] + wallb2[WALLb_HEIGHT]):
        return True
    else:
        return False

def bwall1_is_hit2(wallb1, helihitbox2):
    if (helihitbox2[HHB_X] and helihitbox2[HHB_X] + helihitbox2[HHB_WIDTH] > wallb1[WALLb_X] and helihitbox2[HHB_X] and helihitbox2[HHB_X] +
            helihitbox2[HHB_WIDTH] < wallb1[WALLb_X] + wallb1[WALLb_WIDTH] and
            helihitbox2[HHB_Y] and helihitbox2[HHB_Y] + helihitbox2[HHB_HEIGHT] > wallb1[WALLb_Y] and helihitbox2[HHB_Y] and helihitbox2[HHB_Y] + helihitbox2[HHB_HEIGHT]
            < wallb1[WALLb_Y] + wallb1[WALLb_HEIGHT]):
        return True
    else:
        return False

def bwall2_is_hit2(wallb2, helihitbox2):
    if (helihitbox2[HHB_X] and helihitbox2[HHB_X] + helihitbox2[HHB_WIDTH] > wallb2[WALLb_X] and helihitbox2[HHB_X] and helihitbox2[HHB_X] +
            helihitbox2[HHB_WIDTH] < wallb2[WALLb_X] + wallb2[WALLb_WIDTH] and
            helihitbox2[HHB_Y] and helihitbox2[HHB_Y] + helihitbox2[HHB_HEIGHT] > wallb2[WALLb_Y] and helihitbox2[HHB_Y] and helihitbox2[HHB_Y] + helihitbox2[HHB_HEIGHT]
            < wallb2[WALLb_Y] + wallb2[WALLb_HEIGHT]):
        return True
    else:
        return False

# TOP WALLS HIT DETECTION

def twall1_is_hit1(wallt1, helihitbox1):
    if (helihitbox1[HHB_X] and helihitbox1[HHB_X] + helihitbox1[HHB_WIDTH] > wallt1[WALLt_X] and helihitbox1[HHB_X] and helihitbox1[HHB_X] +
            helihitbox1[HHB_WIDTH] < wallt1[WALLt_X] + wallt1[WALLt_WIDTH] and
            helihitbox1[HHB_Y] and helihitbox1[HHB_Y] + helihitbox1[HHB_HEIGHT] > wallt1[WALLt_Y] and helihitbox1[HHB_Y] and helihitbox1[HHB_Y] + helihitbox1[HHB_HEIGHT]
            < wallt1[WALLt_Y] + wallt1[WALLt_HEIGHT]):
        return True
    else:
        return False

def twall2_is_hit1(wallt2, helihitbox1):
    if (helihitbox1[HHB_X] and helihitbox1[HHB_X] + helihitbox1[HHB_WIDTH] > wallt2[WALLt_X] and helihitbox1[HHB_X] and helihitbox1[HHB_X] +
            helihitbox1[HHB_WIDTH] < wallt2[WALLt_X] + wallt2[WALLt_WIDTH] and
            helihitbox1[HHB_Y] and helihitbox1[HHB_Y] + helihitbox1[HHB_HEIGHT] > wallt2[WALLt_Y] and helihitbox1[HHB_Y] and helihitbox1[HHB_Y] + helihitbox1[HHB_HEIGHT]
            < wallt2[WALLt_Y] + wallt2[WALLt_HEIGHT]):
        return True
    else:
        return False

def twall1_is_hit2(wallt1, helihitbox2):
    if (helihitbox2[HHB_X] and helihitbox2[HHB_X] + helihitbox2[HHB_WIDTH] > wallt1[WALLt_X] and helihitbox2[HHB_X] and helihitbox2[HHB_X] +
            helihitbox2[HHB_WIDTH] < wallt1[WALLt_X] + wallt1[WALLt_WIDTH] and
            helihitbox2[HHB_Y] and helihitbox2[HHB_Y] + helihitbox2[HHB_HEIGHT] > wallt1[WALLt_Y] and helihitbox2[HHB_Y] and helihitbox2[HHB_Y] + helihitbox2[HHB_HEIGHT]
            < wallt1[WALLt_Y] + wallt1[WALLt_HEIGHT]):
        return True
    else:
        return False

def twall2_is_hit2(wallt2, helihitbox2):
    if (helihitbox2[HHB_X] and helihitbox2[HHB_X] + helihitbox2[HHB_WIDTH] > wallt2[WALLt_X] and helihitbox2[HHB_X] and helihitbox2[HHB_X] +
            helihitbox2[HHB_WIDTH] < wallt2[WALLt_X] + wallt2[WALLt_WIDTH] and
            helihitbox2[HHB_Y] and helihitbox2[HHB_Y] + helihitbox2[HHB_HEIGHT] > wallt2[WALLt_Y] and helihitbox2[HHB_Y] and helihitbox2[HHB_Y] + helihitbox2[HHB_HEIGHT]
            < wallt2[WALLt_Y] + wallt2[WALLt_HEIGHT]):
        return True
    else:
        return False



if __name__ == '__main__':
    setup()