import pygame

pygame.init()
dimensions=(1200,800)
window = pygame.display.set_mode(dimensions)

done=False
x=60
y=60
speedx=5
speedy=5

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.circle(window,(255,255,255),(x,y),40)

    print("speedx: ",speedx)
    print("speedy: ",speedy)
    print("x: ",x)
    print("y: ",y)


    if(x+speedx>=1200-40 ):
        speedx*=-1
    if  x-speedx<0:
        speedx*=-1
    if y-speedy<0:
        speedy*=-1
    if(y+speedy>=800-40 ):
        speedy*=-1
    x+=speedx
    y+=speedy


    pygame.display.update()
    window.fill((0,0,0))

    #pygame.display.flip()
