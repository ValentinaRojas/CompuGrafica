import math, pygame

#t=[-20,-10]
#p=[100,0]
#e=5
#omega=90

def Tras(t,p):
	xp=t[0]+p[0]
	yp=t[1]-p[1]
	pp=[xp,yp]
	return pp

def Rot(omega,p):
	o=math.radians(omega)
	xp=round((math.cos(o)*p[0])-(math.sin(o)*p[1]))
	yp=round((math.sin(o)*p[0])+(math.cos(o)*p[1]))
	pp=[int(xp),int(yp)]
	return pp

def Esc(e,p):
    xp=e*p[0]
    yp=e*p[1]
    pp=[xp,yp]
    return pp
