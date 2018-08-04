# Build a House
# Part I, CodeCraft Setup
from codecraft import Game, Position
game = Game()
materials = game.materials

game.clear_console()
print('Hello, Buzz Coder!')
print(materials)

# Part II, useful functions
# block(x,y,z,m), m is material string
def block(x,y,z,m):
    game.set_block(Position(x,y,z), materials[m])

# column(x,z,h,m)
def column(x,z,h,m):   
    for j in range(1, h+1):
        block(x,j,z,m) 
# bar_x
def bar_x(x,y,z,length, m):
    for i in range(x,x+length):
        block(i, y, z, m)

# bar_y
def bar_y(x,y,z,length, m):
    for j in range(y,y+length):
        block(x, j, z, m)

# flat_xy
def flat_xy(x,y,z,h,w,m):
    for j in range(y, y+h):
        bar_x(x,j,z,w,m)                

# wall
def wall(x,z,h,w,m):
    for i in range(x,(x+w)):
        column(i,z,h,m)
game.on_click(put_block)

# Doors and windows: