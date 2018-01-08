from numpy.linalg import norm
import math
'''define a magnitude do vetor para lim - mag = norma'''
def setMag(vector, lim):
    m = norm(vector)
    return lim*vector/m
'''limita a magnitude do vetor ao lim'''
def limit(vector, lim):
    if(norm(vector) > lim):
        return setMag(vector, lim)
    else:
        return vector
'''calcula angulo de rotacao do vetor'''
def heading(vector, add_radians=3*math.pi/2):
    return math.degrees(math.atan2(vector[1], vector[0]) + add_radians)