class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__ (self):
        return str(self.num)+"/"+str(self.den)
    def __repr__ (self):
        return str(self.num)+"/"+str(self.den)

if __name__ == '__main__':
    f = Fraction(3,5)
    print(f)