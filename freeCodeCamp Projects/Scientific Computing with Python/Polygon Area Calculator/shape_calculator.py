class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            rectanglePicture = ""
            for i in range(0, self.height):
                for k in range (0, self.width):
                    rectanglePicture += "*"
                rectanglePicture += "\n"
            return rectanglePicture
    
    def get_amount_inside(self, shape):
        import math
        return math.floor(self.get_area() / shape.get_area())

    # Output Formatting #
    def __repr__(self):
        return self.get_picture()

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def set_side(self, length):
        self.width = length
        self.height = length

    # Output Formatting #
    def __str__(self):
        return "Square(side=" + str(self.width)+ ")"
