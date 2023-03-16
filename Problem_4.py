import math

# Define the equation in terms of x
def f(x):
    return x ** 3 - 2 * x + 1

# Define the initial guess for the root
y = 1

# Define the tolerance for convergence
tolerance = 1e-6

# Apply the Newton-Raphson method to find the root
while abs(f(y)) > tolerance:
    y = (y ** 3 + 1) / 2

# Print the root
print(f"The solutions to the equation are:")
print(f"y = {y:.6f}")
print(f"y = {(-1 + math.sqrt(5)) / 2:.6f} or y = {(-1 - math.sqrt(5)) / 2:.6f}")
