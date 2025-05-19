import pygame 

pygame.init()
kollane=[255,255,0]
punane=[255,0,0]
hall=[128,128,128]
sinine=[0,0,255]
pruun=[139,69,19]

ekraani_pind=pygame.display.set_mode((800,600))
pygame.display.set_caption("Pygame aken")
ekraani_pind.fill(hall)
pygame.draw.rect(ekraani_pind,kollane,(100,100,200,100))
pygame.draw.circle(ekraani_pind,punane,(400,300),50)
pygame.draw.polygon(ekraani_pind,sinine,[(600,100),(700,100),(650,50)])
pygame.draw.line(ekraani_pind,pruun,(100,500),(700,500),10)

pilt1=pygame.image.load("sigma.png")
pilt1=pygame.transform.scale(pilt1,(100,100))
ekraani_pind.blit(pilt1,(300,400))

pygame.display.flip()

while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()