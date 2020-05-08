'''pygame intro'''
'''making a block that moves based on arrow mvmt'''
import pygame
pygame.init()
win = pygame.display.set_mode((500,500)) #window size init
pygame.display.set_caption(" B l o c k ") #basically title

x=50
y=300
width=40
height=60
vel=5
isJump=False
jumpCount=10

run=True
while run: #main loop
    pygame.time.delay(100)

    for event in pygame.event.get(): #checking for any event, eg: mouse c lick
        if event.type == pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()  # to obtain the key that got pressed

    if keys[pygame.K_LEFT] and x>0:  #and condition so that it doesnt go off screen
        x-=vel
    if keys[pygame.K_RIGHT] and x<500-width:
        x+=vel
    if not (isJump): #these run only if ur not jumping
        if keys[pygame.K_UP] and y>0:
            y-=vel
        if keys[pygame.K_DOWN] and y<500-height:
            y+=vel
        if keys[pygame.K_SPACE]:
            isJump =True
    else:
        if jumpCount >= -10:
            neg=1
            if jumpCount<0:
                neg= -1
            y-= (jumpCount ** 2)*0.5*neg # jump is kinda parabolic, so we're squaring to get parabolic(y=x^2) path
            jumpCount-=1
        else:
            isJump=False
            jumpCount=10
    #in pygame the coordinates work like top left is (0,0) and bottom right is (500,500), or wtv the grid size is
    #so based on that moving command is defined
    win.fill((0,0,0)) #filling black so that when the block moves, its previous position becomes black
    #remove this line to see why its important
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))    #similarly circle,polygon ,check about that pygame website
    #check about that parameters, they are important
    pygame.display.update() #this is imp to display something

pygame.quit()


