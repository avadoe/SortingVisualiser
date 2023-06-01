import pygame
import numpy as np
import math

WIDTH = 800
SIZE = 50
pygame.display.set_caption('Sorting Visualiser')

def generate_array():
    return np.random.randint(1, 100, SIZE)

def draw_array(array, win, swapping_indices=None, border_width=1):
    win.fill((255, 255, 255))
    
    bar_width = WIDTH / len(array)
    
    for i, value in enumerate(array):
        bar_height = math.ceil((value / 100) * WIDTH) 
        x = i * bar_width
        y = WIDTH - bar_height
        color = (45, 45, 45)
        border_color = (0, 0, 0)
        
        if swapping_indices and i in swapping_indices:
            color = (0, 0, 128)
        
        pygame.draw.rect(win, border_color, (x, y, bar_width, bar_height), border_width)
        pygame.draw.rect(win, color, (x + border_width, y + border_width, bar_width - 2 * border_width, bar_height - 2 * border_width))

        
    pygame.display.update()

WIN = pygame.display.set_mode((WIDTH, WIDTH))

def bubble_sort(array):
    n = len(array)
    sorted_indices = []
    
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                sorted_indices.extend([j, j + 1])
                
                draw_array(array, WIN, swapping_indices=sorted_indices)
                
                pygame.time.wait(75) 
                
    return array

def main():
    ARRAY = generate_array()
    running = True
    
    print(ARRAY)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                break
        
        sorted_array = bubble_sort(ARRAY.copy())
        draw_array(sorted_array, WIN)
        
        pygame.display.update()
        
        pygame.event.pump()
        
    pygame.quit()

if __name__ == '__main__':
    pygame.init()
    main()
