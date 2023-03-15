import math

def inequality(x):
    if x <= 1:
        y = math.sqrt((1-x)/(1+x))
        lhs = x * (8*math.sqrt(1-x) + math.sqrt(1+x))
        rhs = (11*math.sqrt(1+x) - 16*math.sqrt(1-x)) * ((8*y + 1)/(1-y**2))
        return lhs <= rhs
    else:
        return False

lower_bound = 3/5
upper_bound = 1

for x in [lower_bound, (lower_bound+upper_bound)/2, upper_bound]:
    if inequality(x):
        print(f"The solution is {x}")
        break

