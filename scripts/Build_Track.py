from catmull_rom_splines import catmull_rom
import matplotlib.pyplot as plt
import numpy as np

# the resolution (number of interpolated points between each pair of
#   points, including the start point, but excluding the endpoint of each
#   interval)
RES = 50

def random_track(track_len:int, show=False):
    half_len = track_len // 2

    track_bottom_x = np.arange(1,half_len,dtype='float32')
    track_top_x = np.flip(np.arange(0,half_len-1,dtype='float32'))

    p_x = np.concatenate((track_bottom_x,track_top_x))
    p_y = np.zeros_like(p_x)

    for i in range((half_len-1)*2):
        p_y[i] = np.random.rand()*3
        p_y[i] += 2 if i >= half_len-1 else -2
    
    return custom_track(zip(p_x,p_y), show)

    
def custom_track(xy, show=False):
    x,y = list(zip(*xy)) # unzip

    # do the catmull-rom to compute center line
    center_x, center_y = catmull_rom(x, y, RES)
    
    # compute normal line for each interpolated point
    normal_lines = compute_normal(center_x,center_y)

    if show:
        print_track(x,y,center_x,center_y)

    return list(zip(center_x, center_y, normal_lines))


def compute_normal(center_x, center_y):
    normal_lines = []
    
    for i in range(len(center_x)):
        # calculate slope
        if i != len(center_x)-1:
            m = (center_y[i+1]-center_y[i])/(center_x[i+1]-center_x[i])
        else:
            m = (center_y[0]-center_y[i])/(center_x[0]-center_x[i])
        
        # negative reciprical of slope is normal line
        normal_lines.append(lambda x: (-1/m)*(x-center_x[i]) + center_y[i])

    return normal_lines 

def print_track(p_x,p_y,x_intpol,y_intpol):
    # append first point to end to close loop
    x_intpol = np.append(x_intpol,x_intpol[0])
    y_intpol = np.append(y_intpol,y_intpol[0])

    plt.figure()
    plt.scatter(p_x, p_y)
    plt.plot(x_intpol, y_intpol)
    plt.show()

if __name__ == "__main__":
    track = random_track(20, show=True)
    # custom_track([(0,2),(1,3),(2,2),(3,4),(2,5),(0.5,4)])
