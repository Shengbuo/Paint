from pygame import *
from random import *
from tkinter import *
from tkinter import filedialog
from math import *
from time import *

mixer.init()
display.init()
wid = 1066
hei = 800
screen = display.set_mode((wid,hei))
screen.fill((17,114,189))
running = True

#tk stuff
root = Tk()
root.withdraw()
filetype = [("png",'*.png'),("jpg",'*.jpg')]

cols = [((0,0,0)),((255,255,255)),((0,0,0))]
prisec = 0

#music variables
#wav files are more stable than mp3 files when using mixer
songs = ["music/Chief - stay.wav","music/Door - Minecraft.wav","music/Sweden - Minecraft.wav","music/Gate of Time - The Legend of Zelda.wav","music/The Legend of Zelda Medley.wav",
         "music/Tetris Main Theme.wav","music/Kana Boon - Silhouette.wav","music/Experience - Ludovico Einaudi.wav"]
playing = 0
playbefore = Rect(180,10,50,50)
playnext = Rect(250,10,50,50)
loop = Rect(150,40,20,20)
pause = Rect(150,10,20,20)

pausesurface = screen.subsurface(pause).copy()

looping = False
paused = False

#drawing music
draw.rect(screen,(0,0,0),playnext,1)
draw.rect(screen,(0,0,0),playbefore,1)
draw.rect(screen,(0,0,0),pause,1)
draw.rect(screen,(0,0,0),loop,1)

mixer.music.load(songs[playing])
mixer.music.play()

#brushsize and shape width
sz = 10
shapewid = 1

pointonex,pointoney = -1,-1
drawshape = False

logo = image.load("images/Edsby.png")
logo = transform.scale(logo,(100,100))

spectrumpic = image.load("images/color spectrum.png")
spectrumshades = image.load("images/spectrumshades.png")
spectrumpic = transform.scale(spectrumpic,(120,140))
shadepic = transform.scale(spectrumshades,(20,140))

save = Rect(20,600,40,40)

stampone = image.load("images/Edsbyoriginal.png")
stampone = transform.scale(stampone,(130,130))
stamptwo = image.load("images/edsbymagnify.png")
stamptwo = transform.scale(stamptwo,(100,100))
stampthree = image.load("images/edsbystudent.png")
stampthree = transform.scale(stampthree,(90,90))
stampfour = image.load("images/Edsbycool.png")
stampfour = transform.scale(stampfour,(80,80))
stampfive = image.load("images/edsbyteacher.png")
stampfive = transform.scale(stampfive,(100,100))
stampsix = image.load("images/edsbyheadphones.png")
stampsix = transform.scale(stampsix,(100,100))
stamp = 0
stamps = [stampone,stamptwo,stampthree,stampfour,stampfive,stampsix]

pencil = Rect(20,140,50,50)
eraser = Rect(90,140,50,50)
brush = Rect(20,210,50,50)
colpicker = Rect(90,210,50,50)
rectan = Rect(20,280,50,50)
circl = Rect(90,280,50,50)
lin = Rect(20,350,50,50)
elips = Rect(90,350,50,50)
polyg = Rect(20,420,50,50)
sprayp = Rect(90,420,50,50)
stamponerect = Rect(170,700,130,130)
stamptworect = Rect(310,700,130,130)
stampthreerect = Rect(450,700,130,130)
stampfourrect = Rect(590,700,130,130)
stampfiverect = Rect(730,700,130,130)
stampsixrect = Rect(870,700,130,130)

canvas = Rect(int(0.15*wid),int(0.1*hei),int(0.75*wid),int(0.75*hei))

spectrum = Rect(0,660,140,140)

#color selector
colorcordx = 1
colorcordy = 799
colorselect = Rect(colorcordx-2,colorcordy-2,4,4)
pricol = Rect(80,580,40,40)
seccol = Rect(100,600,40,40)

#loading/resizing images
looppic = image.load("images/loop.png")
looppic = transform.scale(looppic,(20,20))
redlooppic = image.load("images/loopred.png")
redlooppic = transform.scale(redlooppic,(20,20))
playmuspic = image.load("images/playmusic.png")
playmuspic = transform.scale(playmuspic,(17,17))
pausemuspic = image.load("images/pausemusic.png")
pausemuspic = transform.scale(pausemuspic,(17,17))
beforepic = image.load("images/beforenext.png")
beforepic = transform.scale(beforepic,(50,50))
nextpic = transform.flip(beforepic,True,False)
pencilpic = image.load("images/pencil.png")
pencilpic = transform.scale(pencilpic,(40,40))
pencilpiccurs = transform.scale(pencilpic,(27,27))
eraserpic = image.load("images/eraser.png")
eraserpic = transform.scale(eraserpic,(40,40))
eraserpiccurs = transform.scale(eraserpic,(24,24))
brushpic = image.load("images/paintbroosh.png")
brushpic = transform.scale(brushpic,(40,45))
brushpiccurs = transform.flip(brushpic,True,False)
brushpiccurs = transform.scale(brushpiccurs,(24,27))
colpic = image.load("images/colpik.png")
colpic = transform.scale(colpic,(40,40))
colpiccurs = transform.scale(colpic,(30,30))
spraypaintpic = image.load("images/spraypaint.png")
spraypaintpic = transform.scale(spraypaintpic,(40,40))
spraycurs = transform.scale(spraypaintpic,(24,24))
spraycurs = transform.rotate(spraycurs,30)


tools = [pencil,eraser,brush,colpicker,rectan,0,0,0,0,0,sprayp]
tool = 0
#0's for shape tools
cursorpics = [pencilpiccurs,eraserpiccurs,brushpiccurs,colpiccurs,0,0,0,0,0,spraycurs]

canvasurface = Surface((int(0.75*wid),int(0.75*hei)))
screen.blit(canvasurface,(int(0.15*wid),int(0.1*hei)))
canvasurface.fill((255,255,255))

draw.rect(screen,(255,255,255),canvas,0)
draw.rect(screen,(0,0,0),pencil,3)
draw.rect(screen,(0,0,0),eraser,3)
draw.rect(screen,(0,0,0),brush,3)
draw.rect(screen,(0,0,0),colpicker,3)
draw.rect(screen,(0,0,0),sprayp,3)
draw.rect(screen,(255,255,255),rectan,0)
draw.rect(screen,(0,0,0),rectan,3)
draw.rect(screen,(255,255,255),circl,0)
draw.rect(screen,(0,0,0),circl,3)
draw.rect(screen,(255,255,255),lin,0)
draw.rect(screen,(0,0,0),lin,3)
draw.rect(screen,(255,255,255),elips,0)
draw.rect(screen,(0,0,0),elips,3)
draw.rect(screen,cols[0],pricol,0)
draw.rect(screen,cols[1],seccol,0)
draw.rect(screen,(255,255,255),save,0)
    
screen.blit(pencilpic,(25,145))
screen.blit(eraserpic,(95,145))
screen.blit(brushpic,(25,215))
screen.blit(colpic,(93,215))
draw.rect(screen,(0,0,0),(25,285,40,40),2)
draw.circle(screen,(0,0,0),(115,305),20,2)
draw.line(screen,(0,0,0),(25,355),(65,395),2)
draw.ellipse(screen,(0,0,0),(93,360,45,30),2)
screen.blit(spraypaintpic,(93,425))
screen.blit(spectrumpic,(0,660))
screen.blit(shadepic,(120,660))
screen.blit(looppic,(150,40))
screen.blit(pausemuspic,(151,11))
screen.blit(nextpic,(250,10))
screen.blit(beforepic,(180,10))
for i in range(6):
    screen.blit(stamps[i],(170+i*150,700))


#Pure black for color spectrum
draw.line(screen,(0,0,0),(0,799),(139,799))

spectrumsurface = screen.subsurface(spectrum).copy()
spectrumsurcopy = spectrumsurface.copy()
draw.circle(spectrumsurface,(255,255,255),(colorcordx,colorcordy-660),4)
draw.circle(spectrumsurface,(60,60,60),(colorcordx,colorcordy-660),4,1)
screen.blit(spectrumsurface,(0,660))

draw.rect(screen,(255,255,255),(20,10,120,120))
screen.blit(logo,(30,20))


copee = canvasurface.copy()

display.flip()

while running:
    click = False
    fclick = False
    for e in event.get():
        if e.type == QUIT:
            running = False
#_______________________________________________________________________________


        kebo = key.get_pressed()

        #checks if f is pressed (for filled shape tools)
        if kebo[K_f]:
            fclick = True

        if e.type == MOUSEBUTTONDOWN:
            
            if e.button == 1:
                click = True
            #changing brush size, shape thickness    
            if tool == 2 or tool == 1 or tool == 9:    
                if e.button == 4:
                    if kebo[K_LSHIFT]:
                        sz += 4
                    else:
                        sz += 1
                elif e.button == 5:
                    if kebo[K_LSHIFT]:
                        sz -= 4
                    else:
                        sz -= 1
                    if sz < 1:
                        sz = 1
            if 8 > tool > 3:
                if e.button == 4:
                    if kebo[K_LSHIFT]:
                        shapewid += 3
                    else:
                        shapewid += 1
                if e.button == 5:
                    if kebo[K_LSHIFT]:
                        shapewid -= 3
                    else:
                        shapewid -= 1
                    if shapewid < 1:
                        shapewid = 1
            
                        
                
                        
    mx,my = mouse.get_pos()
    mpos = mouse.get_pos()
    mb = mouse.get_pressed()

    
    #music stuff
    if click:
        if loop.collidepoint(mx,my):
            if not looping:
                looping = True
                screen.blit(redlooppic,(150,40))
                
            else:
                looping = False
                screen.blit(looppic,(150,40))
   
        if pause.collidepoint(mx,my):
            if not paused:
                mixer.music.pause()
                paused = True
                screen.blit(pausesurface,(150,10))
                screen.blit(playmuspic,(151,11))
            else:
                mixer.music.unpause()
                paused = False
                screen.blit(pausesurface,(150,10))
                screen.blit(pausemuspic,(151,11))

        if playnext.collidepoint(mx,my):
            mixer.music.stop()
            if playing < len(songs) - 1:
                playing += 1
            else:
                playing = 0
            mixer.music.load(songs[playing])
            mixer.music.play()

        if playbefore.collidepoint(mx,my):
            mixer.music.stop()
            if abs(playing) < len(songs) - 1 or playing == len(songs)-1:
                playing -= 1
            else:
                playing = 0
            mixer.music.load(songs[playing])
            mixer.music.play()

    if not mixer.music.get_busy():
        if not looping:
            if playing < len(songs) - 1:
                playing += 1
            else:
                playing = 0
        mixer.music.stop()
        mixer.music.load(songs[playing])
        mixer.music.play()

    
    #needed for updating the color spectrum when using the color picker
    colchange = cols[prisec]

    
    #color, second color, and saved colour (for temporary changes, like eraser usage)
    #Draws first color over second color if first color is selected, and vice versa
    if prisec == 0: 
        draw.rect(screen,cols[1],seccol,0)
        draw.rect(screen,cols[0],pricol,0)
        if seccol.collidepoint(mx,my) and mb[0] == 1 and not pricol.collidepoint(mx,my):
            prisec = 1
    if prisec == 1:
        draw.rect(screen,cols[0],pricol,0)
        draw.rect(screen,cols[1],seccol,0)
        if pricol.collidepoint(mx,my) and mb[0] == 1 and not seccol.collidepoint(mx,my):
            prisec = 0
        
    #picking color using spectrum
    spectrumsurface.blit(spectrumsurcopy,(0,0))
    if spectrum.collidepoint(mx,my) and mb[0] == 1:
        colorcordx = mx
        colorcordy = my
        cols[prisec] = spectrumsurcopy.get_at((mx,my-660))
    draw.circle(spectrumsurface,(255,255,255),(colorcordx,colorcordy-660),3)
    draw.circle(spectrumsurface,(60,60,60),(colorcordx,colorcordy-660),4,1)
    

    #matches up cursor with canvas surface co-ords
    drawx = mx - int(0.15*wid)
    drawy = my - int(0.1*hei)


    if click:
        if pencil.collidepoint(mx,my):
            tool = 0
        if eraser.collidepoint(mx,my):
            tool = 1
        if brush.collidepoint(mx,my):
            tool = 2
        if colpicker.collidepoint(mx,my):
            tool = 3
        if rectan.collidepoint(mx,my):
            tool = 4
        if circl.collidepoint(mx,my):
            tool = 5
        if lin.collidepoint(mx,my):
            tool = 6
        if elips.collidepoint(mx,my):
            tool = 7
        if sprayp.collidepoint(mx,my):
            tool = 9
        if stamponerect.collidepoint(mx,my) or stamptworect.collidepoint(mx,my) or stampthreerect.collidepoint(mx,my) or stampfourrect.collidepoint(mx,my) or stampfiverect.collidepoint(mx,my) or stampsixrect.collidepoint(mx,my):
            tool = 10
            if stamponerect.collidepoint(mx,my):
                stamp = 0
            elif stamptworect.collidepoint(mx,my):
                stamp = 1
            elif stampthreerect.collidepoint(mx,my):
                stamp = 2
            elif stampfourrect.collidepoint(mx,my):
                stamp = 3
            elif stampfiverect.collidepoint(mx,my):
                stamp = 4
            elif stampsixrect.collidepoint(mx,my):
                stamp = 5
        if save.collidepoint(mx,my):
            filename = (filedialog.asksaveasfilename(parent=root,filetypes = filetype,title="Save as:"))
            

    

    if canvas.collidepoint(mx,my):
        screen.set_clip(canvas)
        if mb[0] == 1:
            if not drawshape:
                screen.blit(copee,(int(0.15*wid),int(0.1*hei)))
        
#pencil
            if tool == 0:
                draw.line(canvasurface,cols[prisec],(ox,oy),(drawx,drawy),2)

#brush and eraser
#eraser is just a white brush tool
            if tool == 2 or tool == 1:
                if tool == 1:
                    cols[2] = (cols[prisec])
                    cols[prisec] = ((255,255,255))
                dist = ((my - oy)**2+(drawx - ox)**2)**0.5
                xdist = (drawx - ox)/max(dist,0.1)
                ydist = (drawy - oy)/max(dist,0.1)
                if xdist == 0 and ydist == 0:
                    draw.circle(canvasurface,cols[prisec],(drawx,drawy),sz)
                else:
                    xcord = ox + xdist
                    ycord = oy + ydist
                    while min(oy,drawy) <= ycord <= max(oy,drawy) and min(ox,drawx) <= xcord <= max(ox,drawx):
                        draw.circle(canvasurface,cols[prisec],(int(xcord),int((ycord))),sz)
                        xcord += xdist
                        ycord += ydist
                ox,oy = drawx,drawy
#resets color if tool was eraser

                if tool == 1:
                    cols[prisec] = cols[2]

            #picking color using tool
            if tool == 3:
                    cols[prisec] = canvasurface.get_at((drawx,drawy))

            if tool == 9:
                #loop for speed
                for i in range(7):
                    rad = randint(0,1)
                    ax = randint(-sz,sz)
                    ay = randint(-sz,sz)
                    if sqrt((ax)**2+(ay)**2)<=sz:
                        draw.circle(canvasurface,cols[prisec],(ax+drawx,drawy+ay),rad)
        
            copee = canvasurface.copy()



        #for drawing shapes
        #
        #
        if click:
            if tool == 10:
                canvasurface.blit(stamps[stamp],(drawx-40,drawy-40))
            if 4 <= tool <= 6:
                if pointonex and pointoney != -1:
                    drawshape = False
                    if fclick and shapewid != 0:
                        shapewid = 0
                    elif fclick and shapewid == 0:
                        shapewid = 1
                    if tool == 4:
                        draw.rect(canvasurface,cols[prisec],(pointonex,pointoney,drawx-pointonex,drawy-pointoney),shapewid)
                    if tool == 5:
                        draw.circle(canvasurface,cols[prisec],(pointonex,pointoney),int(hypot(drawx-pointonex,drawy-pointoney)),min(shapewid,int(hypot(drawx-pointonex,drawy-pointoney))))
                    if tool == 6:
                        draw.line(canvasurface,cols[prisec],(pointonex,pointoney),(drawx,drawy),shapewid)
                    if tool == 7:
                        draw.ellipse(canvasurface,cols[prisec],(pointonex,pointoney,drawx-pointonex,drawy-pointoney),shapewid)
                    pointonex = -1
                    pointoney = -1
                    copee = canvasurface.copy()
                else:
                    pointonex = drawx
                    pointoney = drawy
                    drawshape = True
                    
        if drawshape:
            if fclick and shapewid != 0:
                shapewid = 0
            elif fclick and shapewid == 0:
                shapewid = 1
                    
            if tool < 4 or tool > 7:
                drawshape = False
                pointonex = -1
                pointoney = -1
            else:
                screen.blit(copee,(int(0.15*wid),int(0.1*hei)))
                if tool == 4:
                    draw.rect(screen,cols[prisec],(pointonex+int(0.15*wid),pointoney+int(0.1*hei),drawx-pointonex,drawy-pointoney),shapewid)
                if tool == 5:
                    draw.circle(screen,cols[prisec],(pointonex+int(0.15*wid),pointoney+int(0.1*hei)),int(hypot(drawx-pointonex,drawy-pointoney)),min(shapewid,int(hypot(drawx-pointonex,drawy-pointoney))))
                if tool == 6:
                    draw.line(screen,cols[prisec],(pointonex+int(0.15*wid),pointoney+int(0.1*hei)),(mx,my),shapewid)
                if tool == 7:
                    draw.ellipse(screen,cols[prisec],(pointonex+int(0.15*wid),pointoney+int(0.1*hei),drawx-pointonex,drawy-pointoney),shapewid)
#different cursors when on canvas
    if mb[0] != 1 and canvas.collidepoint(mx,my) and tool < 4 or tool >= 9:
        mouse.set_visible(False)
        screen.blit(copee,(int(0.15*wid),int(0.1*hei)))
        screen.set_clip(canvas)
        if tool == 10:
            screen.blit(stamps[stamp],(mx-40,my-40))
        else:
            screen.blit(cursorpics[tool],(mx-1,my - 26))
    else:
        mouse.set_visible(True)
    ox,oy = drawx,drawy

#updates the spectrum color if color picker is used
    if cols[prisec] != colchange:
        specx = 0
        specy = 660
        while True:
            if spectrumsurcopy.get_at((specx,specy-660)) == cols[prisec]:
                colorcordx = specx
                colorcordy = specy
                break
            else:
                specx += 1
                if specx == 140:
                    specy += 1
                    specx = 0
            

    screen.blit(spectrumsurface,(0,660))

    screen.set_clip(None)
    
    display.flip()
quit()
