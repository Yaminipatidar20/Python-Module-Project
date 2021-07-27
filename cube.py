import math
def volume(length,breadth,height):
    return length*breadth*height
def diagonal(length,breadth,height):
    return math.sqrt(length*length+breadth*breadth+height*height)
def perimeter(length,breadth,height):
    return 4*(length+breadth+height)