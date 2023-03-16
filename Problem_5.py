import math

# Define the equation in terms of x
def f(x):
    return 1 / math.sin(x) ** 3 - 1 / math.cos(x) ** 3 - math.sin(x) ** 7 + math.cos(x) ** 7

# Define the tolerance for convergence
tolerance = 1e-6

# Define the solutions for case 1
solution1 = [math.pi/4, math.pi + math.pi/4]

# Apply the Newton-Raphson method to find the solutions for case 2
solutions2 = []
for x in range(-90, 90):
    x_rad = math.radians(x)
    if abs(math.cos(x_rad) - math.sin(x_rad)) < tolerance:
        continue
    t = math.cos(x_rad) * math.sin(x_rad)
    g = lambda y: (1 + y) / (y ** 3) - 1 / (1 - 3 * y ** 2 + y ** 3) - t
    y = -1
    while abs(g(y)) > tolerance:
        y -= g(y) / ((y ** 2) * (y - 3 * y ** 2 + 1))
    if abs(y) <= 1:
        solutions2.append(math.asin(y))

# Print the solutions
print("The solutions to the equation are:")
for s in solution1 + solutions2:
    print(f"x = {s:.6f} (in radians) or {math.degrees(s):.6f} (in degrees)")
