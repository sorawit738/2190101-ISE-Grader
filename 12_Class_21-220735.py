class Complex:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __str__(self):
        if self.__b == 1:
            if self.__a != 0:
                s = str(self.__a) + '+' + 'i'
            else:
                s = 'i'
        elif self.__b == -1:
            if self.__a != 0:
                s = str(self.__a) + '-' + 'i'
            else:
                s = '-i'
        elif self.__b == 0 and self.__a == 0:
            s = '0'
        else:
            sign = ''
            real = ''
            imaginary = ''
            if self.__b > 0 and self.__a != 0:
                sign = '+'
            if self.__a != 0:
                real = str(self.__a)
            if self.__b != 0:
                imaginary = str(self.__b) + 'i'
            s = real + sign + imaginary
        return s

    def __add__(self, rhs):
        re = self.__a + rhs.__a
        im = self.__b + rhs.__b
        if im == 1:
            if re != 0:
                s = str(re) + '+i'
            else:
                s = 'i'
        elif im == -1:
            if re != 0:
                s = str(re) + '-i'
            else:
                s = '-i'
        elif im == 0 and re == 0:
            s = '0'
        else: 
            sign = ''
            real = ''
            imaginary = ''
            if im > 0 and re != 0:
                sign = '+'
            if re != 0:
                real = str(re)
            if im != 0:
                imaginary = str(im) + 'i'
            s = real + sign + imaginary
        return s

    def __mul__(self, rhs):
        re = (self.__a * rhs.__a) - (self.__b * rhs.__b)
        im = (self.__a * rhs.__b) + (self.__b * rhs.__a)
        if im == 1:
            if re != 0:
                s = str(re) + '+i'
            else:
                s = 'i'
        elif im == -1:
            if re != 0:
                s = str(re) + '-i'
            else:
                s = '-i'
        elif im == 0 and re == 0:
            s = '0'
        else:
            sign = ''
            real = ''
            imaginary = ''
            if im > 0 and re != 0:
                sign = '+'
            if re != 0:
                real = str(re)
            if im != 0:
                imaginary = str(im) + 'i'
            s = real + sign + imaginary
        return s

    def __truediv__(self,rhs):
        re = ((self.__a * rhs.__a) + (self.__b * rhs.__b)) / ((rhs.__a ** 2) + (rhs.__b ** 2))
        im = (-(self.__a * rhs.__b) + (self.__b * rhs.__a)) / ((rhs.__a ** 2) + (rhs.__b ** 2))
        if im == 1:
            if re != 0:
                s = str(re) + '+i'
            else:
                s = 'i'
        elif im == -1 and re != 0:
            if re != 0:
                s = str(re) + '-i'
            else:
                s = '-i'
        elif im == 0 and re == 0:
            s = '0'
        else: 
            sign = ''
            real = ''
            imaginary = ''
            if im > 0:
                sign = '+'
            if re != 0:
                real = str(re)
            if im != 0:
                imaginary = str(im) + 'i'
            s = real + sign + imaginary
        return s

t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a, b)
c2 = Complex(c, d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1 + c2)
elif t == 4 : print(c1 * c2)
else : print(c1 / c2)
