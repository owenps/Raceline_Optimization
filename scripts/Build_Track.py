from Catmull_Rom_Splines import catmull_rom
import matplotlib.pyplot as plt
import numpy as np

# set the resolution (number of interpolated points between each pair of
#   points, including the start point, but excluding the endpoint of each
#   interval)
RES = 50

def random_track(width):

    track_bottom_x = np.arange(1,width,dtype='float32')
    track_top_x = np.flip(np.arange(0,width-1,dtype='float32'))

    p_x = np.concatenate((track_bottom_x,track_top_x))
    p_y = np.zeros_like(p_x)

    for i in range((width-1)*2):
        p_y[i] = np.random.rand()*3
        p_y[i] += 1.5 if i >= width else -1.5
        
    # do the catmull-rom
    x_intpol, y_intpol = catmull_rom(p_x, p_y, RES)
    
    # fancy plotting
    print_track(p_x,p_y,x_intpol,y_intpol)
    
def custom_track(P):
    pass 

def print_track(p_x,p_y,x_intpol,y_intpol):
    # append first point to end to close loop
    x_intpol = np.append(x_intpol,x_intpol[0])
    y_intpol = np.append(y_intpol,y_intpol[0])

    plt.figure()
    plt.scatter(p_x, p_y)
    plt.plot(x_intpol, y_intpol)
    plt.show()


if __name__ == "__main__":
    random_track(10)
