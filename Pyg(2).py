'''pygame 2(check intro for stepwise description)'''
'''making a character '''
import pygame
pygame.init()
win = pygame.display.set_mode((480,480))
pygame.display.set_caption(" M a n ")

#loading all the pics of the character we are making
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
clock=pygame.time.Clock() # used in line 47
x=50
y=400
width=64
height=64
vel=5
isJump=False
jumpCount=10
left = False
right = False
walkCount=0

def redrawGameWindow():
    global walkCount
    win.blit(bg,(0,0)) # to fill screen w pic
    if walkCount+1>=27: # each image is 3 pixels , total 9 so 3*9 =27
        walkCount=0
    if left:
        win.blit(walkLeft[walkCount//3],(x,y)) #div 3 because 3 pixels
        walkCount+=1
    elif right:
        win.blit(walkRight[walkCount//3],(x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))




    pygame.display.update()


run=True
while run:
    clock.tick(27) #setting 27 fps

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a] and x>0:
        x-=vel
        left=True
        right=False

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and x<500-width:
        x+=vel
        right = True
        left = False
    else:
        left=False
        right=False
        walkCount=0

    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump =True
            right=False
            left=False
            walkCount=0
    else:
        if jumpCount >= -10:
            neg=1
            if jumpCount<0:
                neg= -1
            y-= (jumpCount ** 2)*0.5*neg
            jumpCount-=1
        else:
            isJump=False
            jumpCount=10

    redrawGameWindow()

pygame.quit()


