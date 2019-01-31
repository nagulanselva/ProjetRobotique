class Robot(object):
	def __init__(self,x,y,angle):
		self.x=x
		self.y=y
		self.angle=angle
		self.couleur=0 #noir en binaire
		self.largeur=20
		self.longueur=50

	def get_position(self):
		return self.x, self.y


#jeu de test:
a=Robot(0,0,90)
print a.get_position()==(0,0)
a.x,a.y=a.x+1,a.y+1
print a.get_position()==(1,1)
print a.angle==90

