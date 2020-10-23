import math
def areaOfCircle(radius):
    return math.pi * radius**2

def diameterOfCircle(radius):
    return 2 * radius

def circumferenceOfCircle(radius):
    return 2 * math.pi * radius

radius = float(input())
print("%.2f" %areaOfCircle(radius))
print("%.2f"%diameterOfCircle(radius))
print("%.2f"%circumferenceOfCircle(radius))