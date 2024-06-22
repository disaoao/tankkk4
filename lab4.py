import math
class Shape:
    def __init__(self, ellipse: int, ellipsee: int, square: int, trapezoid: int, trapezoide: int,trapezoidh: int,trapezoidc: int):
        self.ellipse = ellipse
        self.ellipsee = ellipsee
        self.square = square
        self.trapezoid = trapezoid
        self.trapezoide = trapezoide
        self.trapezoidh = trapezoidh
        self.trapezoidc = trapezoidc
        
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
class Ellip(Shape):
    def __init__(self, ellipse:int, ellipsee: int, square: int, trapezoid: int, trapezoide: int,trapezoidh: int, trapezoidc: int):
        super().__init__( ellipse, ellipsee, square, trapezoid, trapezoide, trapezoidh, trapezoidc)
    def area(self):
        return  3.14 *self.ellipse * self.ellipsee
    def perimeter(self):
        return 2 * 3.14 * math.sqrt((self.ellipse**2 + self.ellipsee**2) / 2)
        
class Squar(Shape):
    def __init__(self, ellipse:int, ellipsee: int, square: int, trapezoid: int, trapezoide: int,trapezoidh: int, trapezoidc: int):
        super().__init__( ellipse, ellipsee, square, trapezoid, trapezoide, trapezoidh, trapezoidc)      
    def area(self):
        return self.square * self.square
    def perimeter(self):
        return self.square *4
        
class Trapez(Shape):
    def __init__(self, ellipse: int, ellipsee: int, square: int, trapezoid: int, trapezoide: int,trapezoidh: int, trapezoidc: int):
        super().__init__( ellipse, ellipsee, square, trapezoid, trapezoide, trapezoidh, trapezoidc)      
    def area(self):
        # (a + b) * h / 2 
        return  (self.trapezoid + self.trapezoide) * self.trapezoidh / 2
    def perimeter(self):
        return 2*self.trapezoidc + self.trapezoid + self.trapezoide
        

ellip = Ellip(3,5,0,0,0,0,0)
squar = Squar(0,0,7,0,0,0,0)
trapez =Trapez(0,0,0,3,5,4,5)
print("Площадь элипса:", ellip.area())
print("Периметор элипса:", ellip.perimeter())
print("площадь квадрата:", squar.area())
print("Периметор квадрата:", squar.perimeter())
print("площадь трапеции:", trapez.area())
print("Периметор трапеции:", trapez.perimeter())