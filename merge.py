import pygame
import numpy as np
import math

WIDTH = 800
SIZE = 25
pygame.display.set_caption('Merge Sort Visualiser')

def generate_array():
    return np.random.randint(1, 100, SIZE)

def draw_array(array, win, active_index=None, swapping_indices=None, border_width=1):
    win.fill((255, 255, 255))
    
    bar_width = WIDTH / len(array)
    
    for i, value in enumerate(array):
        bar_height = math.ceil((value / 100) * WIDTH) 
        x = i * bar_width
        y = WIDTH - bar_height
        color = (45, 45, 45)
        border_color = (0, 0, 0)
        
        if active_index is not None and i == active_index:
            color = (0, 255, 0)
        elif swapping_indices and i in swapping_indices:
            color = (0, 0, 128)
        
        
        pygame.draw.rect(win, border_color, (x, y, bar_width, bar_height), border_width)
        pygame.draw.rect(win, color, (x + border_width, y + border_width, bar_width - 2 * border_width, bar_height - 2 * border_width))

        
    pygame.display.update()

WIN = pygame.display.set_mode((WIDTH, WIDTH))

def merge(left, right):
    merged = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
            
        else:
            merged.append(right[j])
            j += 1
            
    while i < len(left):
        merged.append(left[i])
        i += 1
        
    while j < len(right):
        merged.append(right[j])
        j += 1
        
    draw_array(merged, WIN)
    pygame.time.delay(600)
        
    return merged

def merge_sort(array):
    n = len(array)
    if n <= 1: return array
    
    mid = n // 2
    
    left = array[:mid]
    draw_array(left, WIN)
    pygame.time.delay(600)
    right = array[mid:]
    draw_array(right, WIN)
    pygame.time.delay(600)
    
    left = merge_sort(left)
    right = merge_sort(right)
    merged = merge(left, right)
    
    return merged

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
        
        sorted_array = merge_sort(ARRAY.copy())
        draw_array(sorted_array, WIN)
        
        pygame.display.update()
        
        pygame.event.pump()
        
        if sorted_array == sorted(ARRAY):
            pygame.time.delay(5000)
            running = False
            
    pygame.time.delay(5000)
        
    pygame.quit()

if __name__ == '__main__':
    pygame.init()
    main()
