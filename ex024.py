import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("ex024.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass

pygame.quit()
