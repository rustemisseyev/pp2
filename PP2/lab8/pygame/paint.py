import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    tool = 'line'
    points = []
    
    current_color = (0, 0, 255)
    background_color = (0, 0, 0)
    
    drawing = False
    start_pos = None

    while True:
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_c:
                    tool = 'circle'
                elif event.key == pygame.K_l:
                    tool = 'line'
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_t:
                    tool = 'rectangle'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos
                    if tool == 'line':
                        points.append(event.pos)
                        points = points[-256:]
                elif event.button == 3:
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    end_pos = event.pos
                    if tool == 'rectangle':
                        drawRectangle(screen, start_pos, end_pos, radius, current_color)
                    elif tool == 'circle':
                        drawCircle(screen, start_pos, end_pos, current_color, radius)
                    drawing = False

            if event.type == pygame.MOUSEMOTION:
                if drawing and tool == 'line':
                    position = event.pos
                    points.append(position)
                    points = points[-256:]
                if drawing and tool == 'eraser':
                    pygame.draw.circle(screen, background_color, event.pos, radius)

        if mode == 'blue':
            current_color = (0, 0, 255)
        elif mode == 'red':
            current_color = (255, 0, 0)
        elif mode == 'green':
            current_color = (0, 255, 0)

        if tool == 'line':
            screen.fill(background_color)
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
                i += 1

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRectangle(screen, start, end, width, color):
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    w = abs(start[0] - end[0])
    h = abs(start[1] - end[1])
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, width)

def drawCircle(screen, start, end, color, width):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    radius = int((dx ** 2 + dy ** 2) ** 0.5)
    pygame.draw.circle(screen, color, start, radius, width)

main()