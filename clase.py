class Silla:
    def __init__(self, material, color, patas=4):
        self.patas = patas
        self.material = material
        self.color = color
        self.ocupada = False

    def sentarse(self):
        if not self.ocupada:
            self.ocupada = True
            print("Te has sentado en la silla")
        else:
            print("La silla ya está ocupada")

    def levantarse(self):
        if self.ocupada:
            self.ocupada = False
            print("Te has levantado de la silla")
        else:
            print("La silla ya está libre")

x = Silla("madera", "negro")
print(x.levantarse)

x.levantarse()
x.sentarse()

silla_2 = Silla("plastico", "gris", 5)
print(silla_2.levantarse)