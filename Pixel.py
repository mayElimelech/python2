class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        average = int((self._red + self._green + self._blue) / 3)
        self._red = average
        self._green = average
        self._blue = average

    def print_pixel_info(self):

        if self._red == 0 and self._green == 0 and self._blue > 50:
            color_name = "blue"
        elif self._red > 50 and self._green == 0 and self._blue == 0:
            color_name = "red"
        elif self._red == 0 and self._green > 50 and self._blue == 0:
            color_name = "green"

        else:
            color_name = ""
        info = f"({self._red}, {self._green}, {self._blue})"
        print(f"X: {self._x}, Y: {self._y}, Color: {info} {color_name}")

if __name__ == '__main__':
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()
