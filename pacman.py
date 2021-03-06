from ggame import App, RectangleAsset, ImageAsset, SoundAsset, CircleAsset
from ggame import LineStyle, Color, Sprite, Sound
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
up=0
speed=20
blue=Color(0x87cefa, 1)
purple=Color(0x7b68ee, 1)
line=LineStyle(0,blue)
black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, line, black)
bg = Sprite(bg_asset, (0,0))
rond=lambda x: 2*(round(x/2,-1))

snake=Sprite(RectangleAsset(20,20,line,purple),(20,20))
snake.dir=0
snake.go = True    
class tail(Sprite):
    asset=RectangleAsset(20,20,line, purple)
    def __init__(self, position):
        super().__init__(tail.asset, position)

def leftKey(event):
    global up
    snake.dir=-speed
    up=0
    #tail((snake.x-20,snake.y))
def rightKey(event):
    global up
    snake.dir=speed
    up=0    
def upKey(event):
    global up
    snake.dir=-speed
    up=1
def downKey(event):
    global up
    snake.dir=speed
    up=1
def spaceKey(event):
    snake.dir=0
def step():
    global up
    if snake.go:
        if up==0:
            snake.x += snake.dir
            snake.y=rond(snake.y)
        if up==1:
            snake.y += snake.dir
            snake.x=rond(snake.x)
        if (snake.x+20)>SCREEN_WIDTH or (snake.y+20)>SCREEN_HEIGHT or snake.x<0 or snake.y<0:
            snake.go=False
            print("You lose.")
dot=[(20*randint(0,40), 20*randint(0,30))]
for (x,y) in dot:
    tail((x,y))
        



        

    

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run(step)
myapp.listenKeyEvent('keydown', 'j', leftKey)
myapp.listenKeyEvent('keydown', 'i', upKey)
myapp.listenKeyEvent('keydown', 'k', downKey)
myapp.listenKeyEvent('keydown', 'l', rightKey)
myapp.listenKeyEvent('keydown', 'space', spaceKey)
