# using any graphics library, draw the mandlebrot set
import pygame
import sys
import os

def clear():
    if os.name == "nt":
        os.system("cls")

def main():
    clear()
    pygame.init()
    pygame.display.set_caption("Mandlebrot Set")
    screen = pygame.display.set_mode((800, 800))
    screen.fill((255, 255, 255))
    pygame.display.update()
    for i in range(0, 800):
        for j in range(0, 800):
            x = -2 + (i / 200)
            y = -2 + (j / 200)
            z = complex(x, y)
            c = complex(0, 0)
            for k in range(0, 100):
                c = (c ** 2) + z
                if abs(c) > 2:
                    break
            if abs(c) > 2:
                screen.set_at((i, j), (0, 0, 0))
            else:
                screen.set_at((i, j), (255, 255, 255))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()