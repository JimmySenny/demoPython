
import pygame

def main():
    pygame.init();
    screen = pygame.display.set_mode(800,600);
    pygame.display.set_caption('ball eat');
    running = True;
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;

if __name__ == '__main__':
    main();