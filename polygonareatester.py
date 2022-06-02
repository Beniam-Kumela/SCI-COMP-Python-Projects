class Rectangle:

    def __init__(self, width, height):
        self.set_width = int(width)
        self.set_height = int(height)
    
    def set_width(self, width):
        self.set_width = int(width)

    def set_height(self, height):
        self.set_height = int(height)
    
    def get_area(self):
        area = (self.set_width)*(self.set_height) 
        return area

    def get_perimeter(self):
        perimeter = ((2*self.set_width)+(2*self.set_height))
        return perimeter
    
    def get_diagonal(self):
        diagonal = ((self.set_width**2) + (self.set_height**2))
        return diagonal
    
    def get_picture(self):
        if self.set_width or self.set_height <= 50:
            row = ("*" * self.set_width) + "\n" 
            picture = row * self.set_height
        else:
            picture = "Too big for picture."
        return picture
    
    def get_amount_inside(self, width, height = ""):
        self.set_width2 = int(width)
        self.set_height2 = int(height)
        if height != "":
            area2 = (self.set_width2 * self.set_height2)
        if height == "":
            area2 = (self.set_width2 * self.set_width2)
        amount_inside = int(self.get_area()) // area2
        return amount_inside

class Square(Rectangle):

    def __init__(self, side):
        self.set_width = int(side)
        self.set_height = int(side)

    def set_side(self, side):
        self.set_width = int(side)
        self.set_height = int(side) 
