from pygame import *
from math import *
from random import *
from time import *

width,height = 1066,800

init()
mixer.init()
screen = display.set_mode((width, height))

songs = ["mosak/1.mp3","mosak/2.mp3","mosak/3.mp3"]
wavsongs = [song.replace(".mp3","wav")+".wav" for song in songs]
print(wavsongs)

playing = 0
newmuspos = 0

mixer.music.load(songs[playing])
mixer.music.play()
playnext = Rect(400,300,50,50)
playbefore = Rect(600,300,50,50)
scrubber = Rect(30,15,200,30)
usingscrub = False
loop = Rect(600,500,30,30)
looping = False
playnewpos = False

muspos = mixer.music.get_pos()/1000

pause = Rect(400,500,30,30)
paused = False

screen.fill((255,255,255))

draw.rect(screen,(0,0,0),playnext,0)
draw.rect(screen,(0,0,0),playbefore,0)
draw.rect(screen,(0,0,0),pause,0)
draw.line(screen,(0,0,0),(30,30),(230,30),3)
draw.rect(screen,(0,0,0),loop,0)
copye = screen.copy()

running = True
while running:
    clicked = False
    for evt in event.get():
        if evt.type == MOUSEBUTTONDOWN:
            clicked = True
        if evt.type == QUIT:
            running = False
            break

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    songlen = mixer.Sound(wavsongs[playing]).get_length()

    muspos = mixer.music.get_pos()/1000 + newmuspos
    
    scrubpos = muspos*200//songlen + 30

    

    screen.blit(copye,(0,0))
    
    
    if clicked and pause.collidepoint(mx,my):
        if not paused:
            mixer.music.pause()
            paused = True
        else:
            mixer.music.unpause()
            paused = False

    if clicked and playnext.collidepoint(mx,my):
        mixer.music.stop()
        if playing < len(songs) - 1:
            playing += 1
        else:
            playing = 0
        newmuspos = 0
        mixer.music.load(songs[playing])
        mixer.music.play()

    if clicked and playbefore.collidepoint(mx,my):
        mixer.music.stop()
        if abs(playing) < len(songs) - 1 or playing == len(songs)-1:
            playing -= 1
        else:
            playing = 0
        newmuspos = 0
        mixer.music.load(songs[playing])
        mixer.music.play()

    if clicked and loop.collidepoint(mx,my):
        if not looping:
            looping = True
            draw.rect(screen,(255,0,0),loop,0)
        else:
            looping = False
            draw.rect(screen,(0,0,0),loop,0)
        copye = screen.copy()


    if muspos >= songlen-1:
        if not looping:
            if playing < len(songs) - 1:
                playing += 1
            else:
                playing = 0
        newmuspos = 0
        mixer.music.stop()
        mixer.music.load(songs[playing])
        mixer.music.play()

    if clicked and scrubber.collidepoint(mx,my):
        usingscrub = True
        
    if mb[0] == 1 and usingscrub:
        screen.set_clip(scrubber)
        mixer.music.stop()
        if 30 < mx < 230:
            scrubpos = mx
            newmuspos = (mx-30)*songlen/200
        elif mx < 30:
            newmuspos = 0
            scrubpos = 30
        elif mx > 230:
            newmuspos = 0
            scrubpos = 230
        playnewpos = True

    if playnewpos and mb[0] != 1:
        playnewpos = False
        usingscrub = False
        mixer.music.play(start = newmuspos)
        screen.set_clip(None)

    draw.rect(screen,(0,0,0),(scrubpos-3,15,6,30),0)
    display.flip()

quit()
