import pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Airplane Game")
airplane_img = pygame.image.load("airplane.png")
airplane_img = pygame.transform.scale(airplane_img, (airplane_img.get_width() // 4, airplane_img.get_height() // 4))
dimensionX = 20
dimensionY = 20
# bullet_img = pygame.iVmage.load("bullet.png")


class Airplane: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        screen.blit(airplane_img, (self.x, self.y))
    def move(self):
        keys = pygame.key.get_pressed() 
        vel = 1
        if keys[pygame.K_LEFT] and self.x>0: 
            self.x -= vel 
        if keys[pygame.K_RIGHT] and self.x< width - dimensionX: 
            self.x += vel 
        # if left arrow key is pressed    
        if keys[pygame.K_UP] and self.y>0: 
            self.y -= vel 
            
        # if left arrow key is pressed    
        if keys[pygame.K_DOWN] and self.y< height - dimensionY: 
            self.y += vel 

class AirPlaneBullet():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        screen.blit(airplane_img, (self.x, self.y))
    def move(self):
        while (self.y):
            self.y += 10
            self.draw()
        
        

airplane = Airplane(screen.get_width() // 2.5, screen.get_height() - 100)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    airplane.draw() 
    airplanebullet = AirPlaneBullet(airplane.x, airplane.y + 10)
    airplanebullet.draw()
    pygame.display.flip()
    airplane.move()
    airplanebullet.move()
    screen.fill((0, 0, 0))

pygame.display.update()
pygame.quit()
        
