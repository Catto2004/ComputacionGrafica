# ######### Actividad PyGame en Clase by Juan Diego Ruiz Benjumea
# DDA, Bresenham y draw.line
import pygame

# ######### Configuración Inicial
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
running = True



def dda(screen, x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    pasos = int(max(abs(dx), abs(dy)))
    mx = dx / pasos
    my = dy / pasos
    x, y = x1, y1
    for _ in range(pasos):
        pygame.draw.circle(screen, color, (round(x), round(y)), 1)
        x += mx
        y += my
        

        
def bresenham(screen, x1, y1, x2, y2, color):
    dx = abs (x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    if dx > dy:
        err = dx / 2.0
        while x != x2:
            pygame.draw.circle(screen, color, (x, y), 1)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
        else:
            pygame.draw.circle(screen, color, (x, y), 1)
            err -= dx
            if err < 0:
                y += sy
                err += dx
            y += sy
        pygame.draw.circle(screen, color, (x, y), 1)
                
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")
    pygame.draw.line(screen, "red", (70,70), (100,100), 5)
    dda(screen, 50, 50, 200, 150, "blue")
    bresenham(screen, 75, 50, 200, 150, "blue")
    pygame.display.flip()
    
pygame.quit()