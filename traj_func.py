import matplotlib, math, random, shapely, csaps, scipy.interpolate 
import matplotlib.pyplot as plt
import numpy as np
from itertools import zip_longest
from scipy.spatial.distance import cdist
from shapely.geometry import LineString, LinearRing, box, Point, Polygon
from shapely.ops import nearest_points, unary_union

def new_circle(flag, obj, c):
    if obj == False:
        # creating the circle
        if flag == 1:
            r = 2
            p = Point(c)
            sq = p.buffer(r)

        # creating a plus
        if flag == 2: 
            sq = Polygon([(-0.5,-0.5), (-0.5, -2.0), (0.5, -2.0), (0.5, -0.5), (2.0, -0.5), (2.0, 0.5), (0.5, 0.5), (0.5, 2.0), (-0.5, 2.0), (-0.5, 0.5), (-2.0, 0.5), (-2.0, -0.5)])

        # creating a radial arm maze
        if flag == 3:
            sq = Polygon([(-0.39, 0.88), (-0.88, 0.82), (-0.88, 0.22), (-0.31, 0.57), (-0.66,0), (-0.06,0), (0,0.49), (0.06, 0), (0.66, 0), (0.31, 0.57), (0.88, 0.22), (0.88, 0.82), (0.39, 0.88), (0.88, 0.94), (0.88, 1.54), (0.31, 1.19), (0.66, 1.76), (0.06, 1.76), (0, 1.27), (-0.06, 1.76), (-0.66, 1.76), (-0.31, 1.19), (-0.88, 1.54), (-0.88, 0.94)])

        #creating a rectangular box
        if flag == 4:
            sq = box(-2,-2,2,2)

    elif obj == True: # if there is an object in the environment
        # creating a circular object
        if flag == 1:
            r = 0.1
            p = Point(c)
            sq = p.buffer(r)
        
    # seperating cords    
    k = list(sq.exterior.coords)
    xi = [m[0] for m in k ]
    yi = [m[1] for m in k ]

    #plotting both the boundaries
    plt.plot(xi, yi)
    return k



def collect(boxes):
    # creating a collection of given entities in the arena (objs + env)
    ll_o = [LinearRing(boxes[0])]
    
    if boxes[1]:
        ll_s = [LinearRing(j) for j in boxes[1]]
        ll = ll_o + ll_s
    else:
        ll = ll_o

    return ll



def checkinside(x, ll, pos_far):
    # find the closest intersection point from current position in the arena 
    pos = x

    pp = unary_union(ll)
    line_cords = LineString([tuple(pos), tuple(pos_far)])

    temp = pp.intersection(line_cords)
    if temp.is_empty: 
        temp_x1 = pos_far[0]
        temp_y1 = pos_far[1]
    else:
        J = np.array(temp)
        if (np.ndim(J) == 1):
            temp_x1 = J[0]
            temp_y1 = J[1]
        else:
            K = np.matlib.repmat(x, len(J), 1)
            L = cdist(J, K)
            M = np.diag(L)
            ind = list(M).index(min(M))
            temp_x1 = J[ind][0]
            temp_y1 = J[ind][1]
    return temp_x1, temp_y1




def smax(q,beta): 
    # generating random probability to flip the direction
    sprob = 0
    q = np.array([1, 0.9])
    beta = 1.0
    for i in q:
        sprob = sprob + np.exp(beta*i)
    
    Prob = np.exp(beta*q[0])/sprob
    if random.random() <= Prob :
        Act = 1
    else:
        Act = -1
    return Act



def speedpos(x, y):
    # finding speed of given coords
    speed = []
    for i in range(1, len(x)):
        dist = np.sqrt((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2)
        speed.append(dist)

    return speed



def hd(x2, y2):
    # calculating theta for given coords
    tgn = myfrenet(x2, y2) # tangent vectors at all the points
    ang = [] 
    p = tgn.shape
   
    # adjusting angle according to different quadrants
    for i in range(p[0]):
        temp = math.degrees(math.atan(tgn[i, 1]/tgn[i, 0]))
        if tgn[i, 0] >= 0:
            if tgn[i,1] >= 0:
                # quadrant 1
                ang.insert(i, temp)
            else:
                #quadrant 4
                ang.insert(i, (temp+360))
        else:
            if (tgn[i, 1] >= 0) or (tgn[i, 1] <= 0):
                # quadrant 2, 3
                ang.insert(i, (temp+180))
    return ang



def myfrenet(x1, y1):
    sz = x1.shape
    
    # calculate derivatives of the curve using spline method
    X = csaps.UnivariateCubicSmoothingSpline(range(sz[0]), x1, smooth = 1.021)
    Y = csaps.UnivariateCubicSmoothingSpline(range(sz[0]), y1, smooth = 1.021)
    p = np.asarray(range(sz[0]))
    mx = scipy.misc.derivative(X, p)
    my = scipy.misc.derivative(Y, p)
    A = [mx, my] # list of all derivative vectors at given points of curve
    
    # discard bad points
    j1 = np.sqrt(np.sum(np.multiply(A,A),axis=0))
    ind = np.nonzero(j1)
    data_x =[mx[i]for i in ind[0]]
    data_y =[my[i]for i in ind[0]]
    data = np.transpose(np.array([data_x, data_y])) # array with non-zero derivative values
    
    # Normalize Tangents
    T_1 = np.sqrt(np.sum(np.multiply(data,data),axis=1))
    T = np.divide(data,np.column_stack((T_1, T_1)))
    
    # finding derivatives at given trajectory inputs
    fx = scipy.interpolate.interp1d(ind[0], np.transpose(T), axis=1)
    T = np.transpose(fx(p))
    
    # Normalize all the tangent vectors
    Tang_1 = np.sqrt(np.sum(np.multiply(T,T),axis=1))
    Tang = np.divide(T,np.column_stack((Tang_1,Tang_1)))
    
    return Tang



def reward(pos, rew_cen):
    R = [0]*len(pos)
    b_rad = 0.40
    p1, p2, p3, p4 = Point(rew_cen[0]), Point(rew_cen[1]), Point(rew_cen[2]), Point(rew_cen[3])
    c1, c2, c3, c4 = p1.buffer(b_rad), p2.buffer(b_rad), p3.buffer(b_rad), p4.buffer(b_rad)
    for i,j in zip(pos,range(len(pos))):
        plc = Point(i)
        if c1.contains(plc) or c3.contains(plc):
            R[j] = -1
        elif c2.contains(plc) or c4.contains(plc):
            R[j] = 1
    return R



def bowl(pos):
    d = math.sqrt(pos[0]**2 + pos[1]**2)
    p = Point(tuple(pos))
    p_c = Point(0,0)
    c1 = p_c.buffer(0.68)
    if 0.7 <= d < 0.72:
        jj = nearest_points(c1, p)
        k_x, k_y = jj[0].x, jj[0].y
        kk = np.array([k_x, k_y])
        return kk
    else:
        return pos
