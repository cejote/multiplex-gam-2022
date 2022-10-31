import itertools
from matplotlib import pyplot as plt
import numpy as np

def dotplot(values, bounds=(-0.15,0.15), label=None,
            median=True, x_pos=None, horizontal=False, **kwargs):
    
    if x_pos is None:
        x = list(itertools.chain(*[[i]*len(v) for i,v in enumerate(values)]))
        x_ix = range(np.max(x)+1)

    else:
        x = list(itertools.chain(*[[x_pos[i]]*len(v) for i,v in enumerate(values)]))
        x_ix = x_pos
    
    x = np.array(x) + np.random.uniform(bounds[0], bounds[1], len(x))

    y = np.concatenate(values)
    
    if horizontal:
        x, y = y, x
 
    plt.scatter(x, y, label=label, **kwargs)
    
    if median:
        mean_expr = [np.median(y[(x == i).nonzero()[0]]) for i in x_ix]
        plt.plot(x_ix, mean_expr)
        
def simpleaxis():
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()