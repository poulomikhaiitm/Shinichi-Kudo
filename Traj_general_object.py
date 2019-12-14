#%%
import matplotlib, math, random, shapely, timeit, pickle, csv, scipy.io
import matplotlib.pyplot as plt
import numpy as np
from itertools import zip_longest
from traj_func import new_circle, checkinside, speedpos, smax, myfrenet, hd, collect, bowl

#%% 
# -------------------------------------------------Initialization------------------------------------------------------
start = timeit.default_timer()

# Trajectory starting points
x = 0.0
y = 1.98

# designing the experiment area
outer_box = new_circle(1, False, (0,0))
objs = []

# centres for multiple objects (comment this part if there is no object)
obj_c = [(0.0, 0.8), (0.2,0.8), (-0.2, 0.8), (0.0, 1.0)]  
for i in obj_c:
    objs.append(new_circle(1, True, i)) 

# geometrical collection of the entire arena (env + object)
boxes = [outer_box, objs]
ll = collect(boxes)

# required variables
r1 = 1
r2 = 1
t = random.randint(0, 360)
theta = t/(2*math.pi)
T = 50000
ro = 0.05
dt = 0.01
xhist = np.array([])
yhist = np.array([])
a = 0
q = np.array([1, 0.9])
pm = 1
dist = np.zeros([4,1])
curv = np.zeros([1,T+2])
c_dist = 0

#%%
# ------------------------Trajectory_Generation---------------------------
for i in range(1, T+1):
    print(i)

    # direction flipping
    adot = -a + pm * smax(q,1/(1*r1))
    if (i % 1000) == 0:
        pm = -1*pm
    
    # position of agent and update
    xhist = np.append(xhist, x,)
    yhist = np.append(yhist, y,)
    xdot = r1 * np.cos(theta)
    ydot = r2 * np.sin(theta)

    # current and far position
    pos = np.array([x, y])
    pos_far = np.array([(x + 1000 * xdot), (y + 1000 * ydot)])
    
    # if i>10000:
        # pos = bowl(pos)
    
    # when far position isn't far enough
    if (i>2): 
        if (r1 == c_dist):
            pos_far = np.array([(x + 10000 * xdot), (y + 10000 * ydot)])

    # step updation rule
    temp_x1c, temp_y1c = checkinside(pos, ll, pos_far) # closest intersection point
    c_dist = np.linalg.norm(np.array([(x - temp_x1c), (y - temp_y1c)])) # dist from intersection points

    r1 = c_dist
    r2 = c_dist

    # variable update
    tdot = a/ro
    x = x + dt * xdot
    y = y + dt * ydot 
    theta = theta + 1 * dt * tdot
    a = a + 1 * dt * adot

    if (i > 23):
        if (xhist[i - 1] == xhist[i - 20]):
            break

# time taken to run the code
stop = timeit.default_timer()
print('Time: ', stop - start)
#%%
# ---------------------------plotting_the_trajectory------------------------
pos = np.column_stack((xhist,yhist))
plt.plot(xhist, yhist)
plt.show()

#%%
# --------------------------calculating_variables----------------
speed = speedpos(xhist, yhist)
theta_real_deg = hd(xhist, yhist)

#%%
#saving variables in pickle file
d = {'x':list(xhist), 'y':list(yhist), 'speed':list(speed), 'theta': list(theta_real_deg), 'env': outer_box, 'pos':pos , 'objs': objs}
with open('traj_0.2.pk1', 'wb') as f:
    pickle.dump(d, f)

#saving variable in csv file
csvfile = "traj_1.csv" 
with open(csvfile, "w") as f:
    w = csv.writer(f)
    w.writerow(["xhist", "yhist", "speed", "theta"])
    for a, b, c, d in zip_longest(xhist, yhist, speed, theta_real_deg): #outer_box):
        w.writerow([a, b, c, d])           

# extra
    # (importing mat file)
        # mat = scipy.io.loadmat('filename')
        # locals().update(mat) --------------makes all keys variables if it is a dictionary, which it always is-------------------

    # (importing from pickle file)
        # with open('filename', 'rb') as l:
            # j = pickle.dump(l)
