import numpy as np
from scipy.optimize import least_squares

def calc_R(x, y, xc, yc):
    return np.sqrt((x-xc)**2 + (y-yc)**2)

def f(c, x, y):
    Ri = calc_R(x, y, *c)
    return Ri - Ri.mean()

def least_squares_circle(coords):
    x, y = np.transpose(coords)
    x_m, y_m = x.mean(), y.mean()
    center_estimate = x_m, y_m
    center_ = least_squares(f, center_estimate, args=(x, y))
    xc, yc = center_.x
    Ri = calc_R(x, y, *center_.x)
    R = Ri.mean()
    return R



#coords= np.array([x_n,y_n]).T


