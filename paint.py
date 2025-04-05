import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 10
    mode = 'blue'
    points = []

    while True:

        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                return


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_g:
                    mode = 'green'

            if event.type == pygame.MOUSEMOTION:

                position = event.pos
                points.append(position)
                points = points[-256:]

        screen.fill((0, 0, 0))


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


main()
