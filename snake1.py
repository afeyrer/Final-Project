from ggame import App, RectangleAsset, ImageAsset, SoundAsset, CircleAsset
from ggame import LineStyle, Color, Sprite, Sound
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
up=5
speed=3
blue=Color(0x87cefa, 1)
purple=Color(0x7b68ee, 1)
line=LineStyle(0,blue)
black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, line, black)
bg = Sprite(bg_asset, (0,0))
rond=lambda x: 2*(round(x/2,-1))
length=1
x=20
y=20
snk=[(20,20)]
dir=1

class tail(Sprite):
    asset=RectangleAsset(20,20,line, purple)
    def __init__(self, position):
        super().__init__(tail.asset, position)
class ntail(Sprite):
    asset=RectangleAsset(20,20,line, black)
    def __init__(self, position):
        super().__init__(ntail.asset, position)
class dots(Sprite):
    asset=RectangleAsset(20,20,line, blue)
    def __init__(self, position):
        super().__init__(dots.asset, position)

dot=[(20*randint(0,39), 20*randint(0,29))]
for (h,k) in dot:
    dots((h,k))
    
tail((x,y))

def leftKey(event):
    dir=0
def rightKey(event):
    dir=1
def downKey(event):
    dir=2
def upKey(event):
    dir=3
while x<SCREEN_WIDTH and x>=0 and y<SCREEN_HEIGHT and y>0:
    if dir ==0:
        print(left)

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
myapp.listenKeyEvent('keydown', 'j', leftKey)
myapp.listenKeyEvent('keydown', 'i', upKey)
myapp.listenKeyEvent('keydown', 'k', downKey)
myapp.listenKeyEvent('keydown', 'l', rightKey)