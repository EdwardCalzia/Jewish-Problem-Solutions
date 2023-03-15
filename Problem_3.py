import math

def construct_point_KM(triangle):
    # extract the coordinates of the vertices A, B, and C from the triangle list
    A = triangle[0]
    B = triangle[1]
    C = triangle[2]
    
    # pick a point M0 anywhere on BC
    M0 = ((B[0]+C[0])/2, (B[1]+C[1])/2)
    
    # construct L on AB such that AL = CM0
    AL_length = math.sqrt((M0[0]-C[0])**2 + (M0[1]-C[1])**2)
    L = ((AL_length/(B[0]-A[0]))*A[0]+(1-AL_length/(B[0]-A[0]))*B[0], 
         (AL_length/(B[0]-A[0]))*A[1]+(1-AL_length/(B[0]-A[0]))*B[1])
    
    # construct K0 such that K0M0 = CM0
    slope_AC = (C[1]-A[1])/(C[0]-A[0])
    K0_x = (L[1]-M0[1]+slope_AC*M0[0]-slope_AC*L[0])/(slope_AC**2+1)
    K0_y = slope_AC*(K0_x-M0[0])+M0[1]
    K0 = (K0_x, K0_y)
    
    # construct A0 and B0 such that A0K0 || AB and B0K0 || BC
    A0 = ((B[1]-L[1]+K0[1])/slope_AC+L[0], B[1])
    B0 = (B[0], B[1]+(K0[0]-B[0])/(B[0]-C[0])*(C[1]-B[1]))
    
    # perform homothety about C to get A0B0C and the points K and M
    K = ((B0[0]-C[0])/2+C[0], (B0[1]-C[1])/2+C[1])
    M = ((A0[0]-C[0])/2+C[0], (A0[1]-C[1])/2+C[1])
    
    return K, M

triangle = [(0,0), (4,0), (2,3)]

result = construct_point_KM(triangle)
print(result)
