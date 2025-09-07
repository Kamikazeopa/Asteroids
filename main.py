import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    
    player = Player(x= SCREEN_WIDTH / 2, y= SCREEN_HEIGHT / 2)
     
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000      #limit frames to 60

if __name__ == "__main__":
    main()
