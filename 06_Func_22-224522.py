import math


def distance1(x1, y1, x2, y2):
    delta_x = x2 - x1
    delta_y = y2 - y1
    magnitude = math.sqrt(delta_x**2 + delta_y**2)
    return magnitude


def distance2(p1, p2):
    return distance1(p1[0], p1[1], p2[0], p2[1])


def distance3(c1, c2):
    d = distance2(c1, c2)
    radiuses = c2[2] + c1[2]
    if d <= radiuses:
        return d, True
    return d, False


def perimeter(points):
    sum = 0
    i = len(points) - 1
    while i >= 0:
        sum += distance2(points[i - 1], points[i])
        i -= 1
    return sum


exec(input().strip())
