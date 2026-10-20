import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

VERTICES = [
    (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1),
    (-1, 1, 1), (-1, -1, -1), (-1, -1, 1), (-1, 1, -1),
]
TRIANGLES = [
    (0, 3, 6), (0, 6, 4),
    (1, 2, 5), (1, 5, 7),
    (0, 1, 7), (0, 7, 4),
    (3, 2, 5), (3, 5, 6),
    (0, 1, 2), (0, 2, 3),
    (4, 7, 5), (4, 5, 6),
]

def draw_cube():
    glBegin(GL_TRIANGLES)
    for tri in TRIANGLES:
        for i in tri:
            glVertex3fv(VERTICES[i])
    glEnd()

def draw_object():

    cubes = [
        (1.0, (0.4, 0.4, 0)),
        (0.8, (0.6, 0.6, 0)),
        (0.6, (0.8, 0.8, 0)),
        (0.4, (1.0, 1.0, 0)),
    ]
    for size, color in cubes:
        glPushMatrix()
        glScalef(size, size, size)
        glColor3f(*color)
        draw_cube()
        glPopMatrix()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("05 Lab 1")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    pos_x, pos_y = 0.0, 0.0
    angle = 0.0
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pos_x -= 1
                elif event.key == pygame.K_d:
                    pos_x += 1
                elif event.key == pygame.K_w:
                    pos_y += 1
                elif event.key == pygame.K_s:
                    pos_y -= 1

        angle += 1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        glTranslatef(pos_x * 0.6, pos_y * 0.6, 0)
        glRotatef(angle, 1, 1, 1)
        glScalef(0.6, 0.6, 0.6)
        draw_object()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
