# ma = F 
# mlθ'' = -mg Sinθ    UNDAMPED CASE, linear acceleration so *l 
# θ''(t) + (g/l)Sinθ = 0 

# convert to first order system (always needed for numerical difference scheme)
# θ' = x 
# x' = -(g/l)Sinθ

# [θ'; x'] = Y' = [x; -(g/l)Sinθ] = F

# naturally, in a finite difference form 
# Y_t+1 - Yt / Δt = F 
# where Y = [θ; x] = [θ; θ'] 

# Y_t+1 - Yt = F*Δt 

import numpy as np 
from math import sin, cos 
from scipy.integrate import odeint 
from matplotlib import pyplot as plt 

#define eqn 
def equations(y0, t):
    theta, x = y0 
    f = [x, -(g/l)*sin(theta)]
    return f 

def plot_results(time, theta_linear, theta_nonlinear):
    plt.plot(time, theta_linear)
    plt.plot(time, theta_nonlinear[:,0])

    plt.title('Pendulum motion for intial angle = ' + str(initial_angle))
    plt.xlabel('time')
    plt.ylabel('angle')
    plt.grid(True)
    plt.legend(['linear','nonlinear'], loc= 'lower right')
    plt.show()

# params 
g = 9.81 
l = 1.0 
time = np.arange(0,10.0,0.025) # similar to linspace, last arg is step

# initial conditions 
initial_angle = 45.0 # deg, <10 is around linear range   
theta0 = np.radians(initial_angle)
x0 = np.radians(0.0) # deg/s i.e. angular velocity 

theta_nonlinear = odeint(equations, [theta0, x0], time)

# analytic linear solution 
w = np.sqrt(g/l)
theta_linear = [theta0*cos(w*t) for t in time ]

# plot 
plot_results(time, theta_linear, theta_nonlinear)


