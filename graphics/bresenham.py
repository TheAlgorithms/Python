# Bresenham's Line Algorithm to draw lines (https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm)

def altBresenham(x1,y1,x2,y2):
  dx=abs(x2-x1)
  dy=abs(y2-y1)
  d=2*dx-dy
  x=x1
  for y in range(y1,y2+1):
    print("(",x,",",y,")",sep='')
    if(d>0):
      x=x+1
      d=d+2*dx-2*dy
    else:
      d=d+2*dx

def bresenham(x1,y1,x2,y2):
  slope=(y2-y1)/(x2-x1)
  if(slope>1):
    altBresenham(x1,y1,x2,y2)
  else:
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    d=2*dy-dx
    y=y1
    for x in range(x1,x2+1):
      print("(",x,",",y,")",sep='')
      d=d+2*dy
      if(d>=0):
        y=y+1
        d=d-2*dx
    
#Driver Code
x1 = 0 
y1 = 0
x2 = 5
y2 = 8
bresenham(x1,y1,x2,y2)

