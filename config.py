from pygame import Color

game_title = "Flying strawberry"
screen_size = (800, 500)
lock_fps = 60
background = Color("black")
pipes_color = Color("Orange")
font_color = Color("White")

gravity_vector = (0, 0.17)
jump_vector = (0, -8)
init_pos = (70, 300)
player_size = (25,25)
speed = 1
score = 0
