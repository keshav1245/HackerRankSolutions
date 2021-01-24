import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real+no.real,self.imaginary+no.imaginary)

    def __sub__(self, no):
        return Complex(self.real-no.real,self.imaginary-no.imaginary)
    
    def __mul__(self, other):
        return Complex(self.real*other.real-self.imaginary*other.imaginary, self.real*other.imaginary+self.imaginary*other.real)
    def __truediv__(self, no):
        
        return self.__mul__(Complex(no.real, -1*no.imaginary)).__mul__(Complex(1.0/(no.mod().real)**2, 0))
        
        # d = (no.real**2 + no.imaginary**2)
        # real = (self.real*no.real + self.imaginary*no.imaginary ) // d
        
        # imag = (self.imaginary*no.real - self.real*no.imaginary) // d
        
        # return Complex(real,imag)
    
        
    def mod(self):
        return Complex((self.real**2 + self.imaginary**2)**0.5, 0 )
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
