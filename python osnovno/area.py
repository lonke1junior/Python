import math
def area(base, height):
    ''' (number, number) -> number

    Return the are of trangle with given base and height

    >>>area(10, 40)
    200.0
    >>>area(3.4, 7.5)
    12.75
    '''
    return base*height/2

def perimeter(side1, side2, side3):
    '''(number, number, number) -> number

    Return the perimeter of the triangle with sides or length side1, side2 and side3.

    >>>perimeter(3, 4, 5)
    12
    >>>perimeter(10.5, 6, 9.3)
    25.8
    '''
    return side1+side2+side3

def semiperimeter(side1, side2, side3):
    '''(number, number, number) -> float

    Return the semiperimeter od a triangle with sides od length side1, side2 and side3.

    >>>semiperimeter(3, 4, 5)
    6.5
    >>>semiperimeter(10.5, 6, 9.3)
    12.9
    '''
    return perimeter(side1,side2,side3)/2

def area_heron(side1, side2, side3):
    ''' (number, number, number)->float

    Return the area of a triangle with sides of length side1, side2 and side3.

    >>>area_heron(3, 4, 5)
    6.0
    >>>area_heron(10.5, 6, 9.3)
    27.731
    '''
    semi = semiperimeter(side1, side2, side3)
    area = math.sqrt(semi * (semi - side1) * (semi - side2) * (semi - side3))
    return area
