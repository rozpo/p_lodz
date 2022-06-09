from pyx import*
import sys

c = canvas.canvas()
j = int(sys.stdin.readline())
z = 1

for j in range(0, j, 1):
    i = j*4
	
    p1 = path.curve(i+0.2,0, i+2.2,-4, i+2.2,4, i+4.2,0)
    p2 = path.curve(i+1.1,0, i+3.1,-4, i+3.1,4, i+5.1,0)
    p3 = path.curve(i+2,0, i+4,-4, i+4,4, i+6,0)
    
    if z == 1:
        c.stroke(p3, [color.rgb.blue, style.linewidth(0.1)])
        c.stroke(p2, [color.rgb.red, style.linewidth(0.1)])
        c.stroke(p1, [color.rgb.green, style.linewidth(0.1)])
    elif z == 2:
        c.stroke(p3, [color.rgb.blue, style.linewidth(0.1)])
        c.stroke(p1, [color.rgb.green, style.linewidth(0.1)])
        c.stroke(p2, [color.rgb.red, style.linewidth(0.1)])#
    elif z == 3:
        c.stroke(p1, [color.rgb.green, style.linewidth(0.1)])
        c.stroke(p3, [color.rgb.blue, style.linewidth(0.1)])
        c.stroke(p2, [color.rgb.red, style.linewidth(0.1)])
    elif z == 4:
        c.stroke(p1, [color.rgb.green, style.linewidth(0.1)])
        c.stroke(p2, [color.rgb.red, style.linewidth(0.1)])
        c.stroke(p3, [color.rgb.blue, style.linewidth(0.1)])
    elif z == 5:
        c.stroke(p2, [color.rgb.red, style.linewidth(0.1)])
        c.stroke(p1, [color.rgb.green, style.linewidth(0.1)])
        c.stroke(p3, [color.rgb.blue, style.linewidth(0.1)])
    elif z == 6:
        c.stroke(p2, [color.rgb.red, style.linewidth(0.1)])
        c.stroke(p3, [color.rgb.blue, style.linewidth(0.1)])
        c.stroke(p1, [color.rgb.green, style.linewidth(0.1)])
        z = 0
    z = z + 1
    
c.writePDFfile("lines")