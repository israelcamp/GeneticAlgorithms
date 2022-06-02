from numpy.linalg import norm
import math

def setMag(vector, lim):
    '''define a magnitude do vetor para lim - mag = norma'''
    m = norm(vector)
    return lim*vector/m

def limit(vector, lim):
    '''limita a magnitude do vetor ao lim'''
    if(norm(vector) > lim):
        return setMag(vector, lim)
    else:
        return vector

def heading(vector, add_radians=3*math.pi/2):
    '''calcula angulo de rotacao do vetor'''
    return math.degrees(math.atan2(vector[1], vector[0]) + add_radians)