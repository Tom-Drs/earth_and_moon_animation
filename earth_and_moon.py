from tkinter import Canvas, Tk, ALL
from math import cos, sin, radians


class AnimationEarthMoon(Tk):

    def __init__(self, width=1000, height=1000, radius_earth_moon=350,
                 moon_radius=50, earth_radius=70):
        super().__init__()
        self.radius_earth_moon = radius_earth_moon
        self.earth_radius = earth_radius
        self.moon_radius = moon_radius
        self.width = width
        self.height = height
        self.degree = 0
        self.canvas = Canvas(self, width=width, height=height, bg='black')
        self.canvas.pack()
        self.animation_loop()

    def animation_loop(self):
        self.update_frame()
        self.degree += 1
        self.after(10, self.animation_loop)

    def update_frame(self):
        self.canvas.delete(ALL)
        self.draw_moon(self.degree)
        self.draw_earth()

    def draw_moon(self, degree):
        x_moon_point = cos(radians(degree)) * self.radius_earth_moon + self.width / 2
        y_moon_point = sin(radians(degree)) * self.radius_earth_moon + self.height / 2
        moon_coord = self.get_circle_coord(x_moon_point, y_moon_point, self.moon_radius)
        self.canvas.create_oval(moon_coord, fill="white")
        x_crater_point = cos(radians(180+self.degree)) * (self.moon_radius /2) + x_moon_point
        y_crater_point = sin(radians(180+self.degree)) * (self.moon_radius / 2) + y_moon_point
        crater_coord = self.get_circle_coord(x_crater_point, y_crater_point, 10)
        self.canvas.create_oval(crater_coord, fill="gray")

    def draw_earth(self):
        width_middle = self.width / 2
        height_middle = self.height / 2
        coord_circle = self.get_circle_coord(width_middle, height_middle,
                                             self.earth_radius)
        self.canvas.create_oval(coord_circle, fill="green")

    @staticmethod
    def get_circle_coord(x, y, radius):
        return x - radius, y + radius, x + radius, y - radius


if __name__ == "__main__":
    root = AnimationEarthMoon()
    root.resizable(width=False, height=False)
    root.title("Earth and Moon Animation")
    root.mainloop()
