from pyx import *

c = canvas.canvas()

circle = path.circle(0, 0, 2)
line = path.line(-1.5, 3, -1.5, -3)

c.stroke(circle, [style.linewidth.Thick])
c.stroke(line, [style.linewidth.Thick])
isects_circle, isects_line = circle.intersect(line)

isectx, isecty = circle.at(isects_circle[0])
isectxx, isectyy = circle.at(isects_circle[1])

tri=path.path(path.moveto(0,0), path.lineto(isectx, isecty), path.lineto(isectxx, isectyy), path.closepath())

for isect in isects_circle:
	isectx, isecty = circle.at(isect)
	c.stroke(path.line(0, 0, isectx, isecty))

c.fill(tri, [deco.filled([color.grey(0.5)])])
	
c.writePDFfile()