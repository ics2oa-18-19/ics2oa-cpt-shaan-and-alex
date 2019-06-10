import arcade
import random

#Screen Dimensions
WIDTH = 1365
HEIGHT = 710

#Variables
current_screen = "menu"
x = 0
y = 0
score = 0


    #Bottom Wall Code

WALLb_X = 0
WALLb_Y = 1
WALLb_WIDTH = 2
WALLb_HEIGHT = 3
WALLb_COLOR = 4

wallb1 = [690, 0, 25, random.randrange(0, HEIGHT - 200), arcade.color.MAROON]
wallb2 = [1390, 0, 25, random.randrange(0, HEIGHT - 200), arcade.color.MAROON]
bottom_walls = [wallb1, wallb2]


    #Top Wall Code

WALLt_X = 0
WALLt_Y = 1
WALLt_WIDTH = 2
WALLt_HEIGHT = 3
WALLt_COLOR = 4

wallt1 = [690, wallb1[WALLb_HEIGHT] + 200, 25, HEIGHT - wallb1[WALLb_HEIGHT], arcade.color.MAROON]
wallt2 = [1390, wallb2[WALLb_HEIGHT] + 200, 25, HEIGHT - wallb2[WALLb_HEIGHT], arcade.color.MAROON]
top_walls = [wallt1, wallt2]
up_pressed = False
down_pressed = False


    #Helicopter Hit Box Code

HHB_X = 0
HHB_Y = 1
HHB_WIDTH = 2
HHB_HEIGHT = 3

helihitbox1 = [x + 200, y + 295, 100, 5]
helihitbox2 = [x + 100, y + 340, 100, 25]
helihitbox3 = [x + 75, y + 395, 250, 10]
all_hhb = [helihitbox1, helihitbox2, helihitbox3]

    #Update Function

def update(delta_time):
    global up_pressed, down_pressed, x, y, current_screen, top_walls, bottom_walls, score, all_hhb
    if current_screen == "play":
        if y <= 290:
            if up_pressed:
                y += 10
                for helihitbox in all_hhb:
                    helihitbox[HHB_Y] += 10
        if y >= -280:
            if down_pressed:
                y -= 10
                for helihitbox in all_hhb:
                    helihitbox[HHB_Y] -= 10
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
        if score_system() == True:
            score += 1
        if hit_detection() == True:
            current_screen = "score"
    if current_screen == "reset":
        x = 0
        y = 0
        wallb1[WALLb_X] = 690
        wallb2[WALLb_X] = 1390
        wallt1[WALLt_X] = 690
        wallt2[WALLt_X] = 1390
        helihitbox1[HHB_X] = x + 200
        helihitbox1[HHB_Y] = y + 295
        helihitbox2[HHB_X] = x + 100
        helihitbox2[HHB_Y] = y + 340
        helihitbox3[HHB_X] = x + 75
        helihitbox3[HHB_Y] = y + 395
        score = 0
        current_screen = "play"



def on_draw():
    global x, y, wall1, score, helihitbox1
    arcade.start_render()
    # Draw in here...
    if current_screen == "menu":
        arcade.draw_text("HOPPY HELICOPTER", HEIGHT / 2 - 100, WIDTH / 4, arcade.color.BLACK, font_size=60,
                         font_name="garamond")
        arcade.draw_text("Press space to play", HEIGHT / 2 - 100, WIDTH / 4.5, arcade.color.BLACK,
                         font_name="garamond")
        arcade.draw_text("Press I to read instructions", HEIGHT / 2 - 100, WIDTH / 5, arcade.color.BLACK,
                         font_name="garamond")
        arcade.draw_text("Press ESC to Quit", HEIGHT / 2 - 100, WIDTH / 5.5 , arcade.color.BLACK,
                         font_name="garamond")
    if current_screen == "play":
        draw_helicopter(x, y)
        for wallb in bottom_walls:
            draw_wallb(wallb)
        for wallt in top_walls:
            draw_wallt(wallt)
        arcade.draw_text(f"{score}", 20, 690, arcade.color.BLACK)
    if current_screen == "pause":
        draw_helicopter(x, y)
        for wallb in bottom_walls:
            draw_wallb(wallb)
        for wallt in top_walls:
            draw_wallt(wallt)
        arcade.draw_text(f"{score}", 20, 690, arcade.color.BLACK)
        arcade.draw_text("PAUSE", HEIGHT / 2 + 150, WIDTH / 4, arcade.color.BLACK, font_size=60,
                         font_name="garamond")
        arcade.draw_text("Press Space to Resume", HEIGHT / 2 + 80, WIDTH / 4 - 50, arcade.color.BLACK, font_size=30,
                         font_name="garamond")
    if current_screen == "Instruction":
        arcade.draw_text("Welcome to Hoppy Helecopter! To move your helicopter use W for up and S for down.",
                         HEIGHT / 2, WIDTH / 2 - 40, arcade.color.BLACK)
        arcade.draw_text("You can use the esc key to leave the game at any time", HEIGHT / 2, WIDTH / 2 - 60,
                         arcade.color.BLACK)
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
        arcade.draw_text(f"Score: {score}", HEIGHT / 10, WIDTH / 2 - 20, arcade.color.BLACK)
        arcade.draw_text("To return to menu, press ESC", HEIGHT / 10, WIDTH / 2 - 60, arcade.color.BLACK)
        arcade.draw_text("To replay, press SPACE", HEIGHT / 10, WIDTH / 2 - 100, arcade.color.BLACK)


    #Score Code

def score_system():
    for wallb in bottom_walls:
        for wallt in top_walls:
            if (helihitbox1[HHB_X] == wallb[WALLb_X] and helihitbox1[HHB_Y] > wallb[WALLb_Y]
                    + wallb[WALLb_HEIGHT] and helihitbox1[HHB_Y] < wallt[WALLt_Y]):
                return True
    else:
        return False


def on_key_press(key, modifiers):
    global up_pressed, down_pressed, current_screen
    if current_screen == "menu":
        if key == arcade.key.SPACE:
            current_screen = "reset"
        if key == arcade.key.I:
            current_screen = "Instruction"
        if key == arcade.key.ESCAPE:
            quit()
    if current_screen == "Instruction":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"
    if current_screen == "play":
        if key == arcade.key.W:
            up_pressed = True
        if key == arcade.key.S:
            down_pressed = True
        if key == arcade.key.ESCAPE:
            current_screen = "pause"
    if current_screen == "pause":
        if key == arcade.key.SPACE:
            current_screen = "play"
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


    #WALL HIT DETECTION

def hit_detection():
    for wallt in top_walls:
        for wallb in bottom_walls:
            for helihitbox in all_hhb:
                if (helihitbox[HHB_Y] <= wallb[WALLb_HEIGHT] and helihitbox[HHB_X] < wallb[WALLb_X] and helihitbox[HHB_X]
                        + helihitbox[HHB_WIDTH] > wallb[WALLb_X] + wallb[WALLb_WIDTH] or helihitbox[HHB_X] +
                        helihitbox[HHB_WIDTH] >= wallb[WALLb_X] and helihitbox[HHB_X] + helihitbox[HHB_WIDTH]
                        <= wallb[WALLb_X] + wallb[WALLb_WIDTH] and helihitbox[HHB_Y] < wallb[WALLb_HEIGHT]):
                    return True
                elif (helihitbox3[HHB_Y] >= wallt[WALLt_Y] and helihitbox3[HHB_X] < wallt[WALLt_X] and helihitbox3[HHB_X]
                        + helihitbox3[HHB_WIDTH] > wallt[WALLt_X] + wallt[WALLt_WIDTH] or helihitbox3[HHB_X] +
                        helihitbox3[HHB_WIDTH] >= wallt[WALLt_X] and helihitbox3[HHB_X] + helihitbox3[HHB_WIDTH]
                        <= wallt[WALLt_X] + wallt[WALLt_WIDTH] and helihitbox3[HHB_Y] > wallt[WALLt_Y]):
                    return True
    else:
        return False


if __name__ == '__main__':
    setup()                                                                                                                                                                   
