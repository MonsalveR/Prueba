class coche:
	def __init__(self):
		self.Color = "Blanco"
		self.Avanza = 0

	def Avanzar(self):
		self.Avanza += 1

	def Recorrido(self):
		print("Hemos Avanzado ",self.Avanza," Km")


c1 = coche()

while c1.Avanzar() != 4:
	c1.Avanzar()
	c1.Recorrido()
