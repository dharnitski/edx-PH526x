import math
import random

print("2a", round(math.pi / 4, 6))

random.seed(1)  # Fixes the seed of the random number generator.


def rand():
    return random.uniform(-1, 1)


print("2b", rand())


def distance(x, y):
    (x1, y1) = x
    (x2, y2) = y
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


print("2c", distance((0, 0), (1, 1)))


def in_circle(x, origin=[0, 0]):
    d = distance(x, origin)
    return d < 1


print("2d", in_circle((1, 1)))


random.seed(1)  # Fixes the seed of the random number generator.
R = 10000
# Use the rand function from Exercise 2b to generate R randomly located points.
points = [(rand(), rand()) for i in range(R)]


# Use the function in_circle to test whether or not a given pint falls within the unit circle.
inside = [in_circle(p) for p in points]
# Find the proportion of points that fall within the circle by summing all True values in the inside list; then divide the answer by R to obtain a proportion.
total_inside = 0
for i in inside:
    if i:
        total_inside += 1

proportion = total_inside/R

print("2e", proportion)


# from exercise explanation
random.seed(1)

inside = []
for i in range(R):
    point = [rand(), rand()]
    inside.append(in_circle(point))

print("2e", sum(inside) / R)

print("2f", math.pi / 4 - proportion)

