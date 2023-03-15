'''''
Draw line between two points through slope intercept algorithm and digital differential analyzer algorithm
'''''
from OpenGL.GL import * 
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def init():
  glClearColor(0.0,1.0,0.0,1.0)
  gluOrtho2D(-100.0, 100.0, -100.0, 100.0)
   
# Function for slope intercept algorithm
def slope(x1,y1,x2,y2):
  dx = x2 - x1
  dy = y2 - y1
  m = dy/dx
  x=x1
  y=y1
  b = y1 - m*x
  glBegin(GL_POINTS) 
  
  if m <= 1:
    steps = dx
    for x in range(x1+1, steps):
      y = m*x + b
      glVertex2f(x, y)
  else: 
    steps = dy
    for y in range(y1 + 1, steps):
      x = (y-b)/m 
  glEnd()
  glFlush()
  
def draw(): 
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(1.0,0.0,0.0)  #drawing color
  glPointSize(5)  #pointer size
  
  x1 = -50
  y1 = -50
  x2 = 15
  y2 = 12
  slope(x1,y1,x2,y2)
  
def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowPosition(50, 50)   #window starting point is 50,50
  glutInitWindowSize(700,700)
  glutCreateWindow("My First OpenGL")
  init()
  glutDisplayFunc(draw)
  glutMainLoop() 
main()