def homothety():
    M0 = (3, 4)
    C = (0, 0)
    B = (6, 0)
    A = (0, 8)
    L = (4, 4/3)

    x_diff = B[0] - C[0]
    y_diff = B[1] - C[1]
    M = (M0[0] + x_diff, M0[1] + y_diff)

    K0 = (L[0] + M0[0] - M[0], L[1] + M0[1] - M[1])

    line1 = ((L[0], L[1]), (K0[0] + x_diff, K0[1] + y_diff))
    line2 = ((K0[0], K0[1]), (A[0], A[1]))

    _, B0 = intersect(line1, line2)

    polygon = [A, B0, C]
    homothety_center = (C[0], C[1]) # fix here
    scale_factor = 2

    new_polygon = homothety_transform(polygon, homothety_center, scale_factor)

    return new_polygon


def intersect(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]
    det = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if det == 0:
        return False, None

    t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / det
    u = -((x1-x2)*(y1-y3) - (y1-y2)*(x1-x3)) / det

    if 0 <= t <= 1 and 0 <= u <= 1:
        x = x1 + t*(x2-x1)
        y = y1 + t*(y2-y1)
        return True, (x, y)
    else:
        return False, None

def homothety_transform(polygon, center, scale_factor):
    new_polygon = []
    for point in polygon:
        if point is not None:
            x = center[0] + scale_factor*(point[0] - center[0])
            y = center[1] + scale_factor*(point[1] - center[1])
            new_point = (x, y)
            new_polygon.append(new_point)
        else:
            new_polygon.append(None)
    return new_polygon


print(homothety())
