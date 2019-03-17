def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
     def __init__(self,top,bottom):
         """Modify the constructor for the fraction class so that it
         checks to make sure that the numerator and denominator
         are both integers.If either is not an integer the constructor
         should raise an exception."""
         if (type(top) != int) or (type(bottom) != int):
            raise RuntimeError("The numerator and the denominator must both be integers")
         else:
             """Using a negative denominator would cause some
             of the relational operators to give incorrect results.
             In general, this is an unnecessary constraint. Modify
             the constructor to allow the user to pass a negative
             denominator so that all of the operators continue
             to work properly."""
             self.num = top
             self.den = bottom
             # simplify fraction
             common = gcd(self.num,self.den)
             self.num = self.num//common
             self.den = self.den//common
             # the gcd flips the num/den signs if den is negative, fixing this here
             if (self.den > 0) and (bottom < 0):
                 self.den = self.den*(-1)
                 self.num = self.num*(-1)

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

    # __repr__ is what is returned when you type the name of a variable and push enter in the python terminal
     def __repr__(self):
         return '{self.__class__.__name__}({self.num}, {self.den})'.format(self=self)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         return Fraction(newnum,newden)

     """Research the __radd__ method. How does it differ
     from __add__? When is it used? Implement __radd__
     DOESN'T MAKE SENSE TO DO THIS IN FRACTION CLASS, SO SKIPPING"""
     """def __radd__(self, otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         return Fraction(newnum,newden)"""

     #consider the __iadd__ (+=) method.
     def __iadd__(self, otherFrac):
         selfFrac = Fraction(self.num,self.den)
         return(selfFrac.__add__(otherFrac))

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den
         return firstnum == secondnum

     # write some methods to implement *, /, and - . Also implement comparison operators > and <
     def __mul__(self,otherFrac):
         prod_num = self.num*otherFrac.num
         prod_den = self.den*otherFrac.den
         return Fraction(prod_num,prod_den)

     def __truediv__(self,otherFrac):
         flipFrac = Fraction(otherFrac.den,otherFrac.num)
         return self.__mul__(flipFrac)

     def __sub__(self,otherFrac):
         newnum = self.num*otherFrac.den - self.den*otherFrac.num
         newden = self.den*otherFrac.den
         return Fraction(newnum,newden)

     def __gt__(self,otherFrac):
         newnum_self = self.num*otherFrac.den
         newnum_other = self.den*otherFrac.num
         return newnum_self > newnum_other

     def __lt__(self,otherFrac):
         newnum_self = self.num*otherFrac.den
         newnum_other = self.den*otherFrac.num
         return newnum_self < newnum_other

     def __ge__(self,otherFrac):
         newnum_self = self.num*otherFrac.den
         newnum_other = self.den*otherFrac.num
         return newnum_self >= newnum_other


     def __le__(self,otherFrac):
         newnum_self = self.num*otherFrac.den
         newnum_other = self.den*otherFrac.num
         return newnum_self <= newnum_other

     def __ne__(self,otherFrac):
         newnum_self = self.num*otherFrac.den
         newnum_other = self.den*otherFrac.num
         return newnum_self != newnum_other

     def getNum(self):
         return self.num

     def getDen(self):
         return self.den


x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)
print(x*y)
print(x/y)
print(x-y)
print(x>y)
print(x<y)
print(x<=y)
print(x>=y)
print(x!=y)
print(x.getNum())
print(x.getDen())
print(y.getNum())
print(y.getDen())

print('Now onto negative fractions. X & Y are the same fractions but Y has the negative in the denominator')
x = Fraction(-1,2)
y = Fraction(1,-2)
print(x+y)
print(x == y)
print(x*y)
print(x/y)
print(x-y)
print(x>y)
print(x<y)
print(x<=y)
print(x>=y)
print(x!=y)
print(x.getNum())
print(x.getDen())
print(y.getNum())
print(y.getDen())
x += y
print(x)
print(repr(y))
