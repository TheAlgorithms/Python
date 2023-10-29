from turtle import *

dis = [100, 200, 150, 50, 120,100, 100]
ngl = [90, 72, 144, 36, -60, -90, 45,45]


for d, a in zip(dis, ngl):
    fd(d)
    if a < 0:
        lt(abs(a))
    else:
        rt(a)

mainloop()