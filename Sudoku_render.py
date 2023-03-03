#%%
import numpy as np
import matplotlib.pyplot as plt

def draw_sudoku_simple(data):
    fig, ax = plt.subplots(dpi=300)
    ax.set_aspect('equal')
    ax.set_xticks(np.arange(0,10,1))
    ax.set_yticks(np.arange(0,10,1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.invert_yaxis()
    ax.grid(True)
    ax.vlines([3,6],0,9,'k')
    ax.hlines([3,6],0,9,'k')
    ax.set_xlim(0,9)
    ax.set_ylim(9,0)
    for i in range(9):
        for j in range(9):
            if data[i*9+j] != 0:
                ax.text(j+0.5,i+0.5,data[i*9+j],ha='center',va='center',fontsize=20)
    plt.show()

def draw_sudoku_marginal(data,plot_path=None):
    # data is an array of shape 81*9, every row is the marginal distribution of a cell
    # plot the marginal distribution of each cell as a 3*3 grid, with the value of the cell in the center, 
    # use gray to represent the probability of each value
    # organize the cells in a 9*9 grid
    fig, ax = plt.subplots(dpi=300)
    ax.set_aspect('equal')
    ax.set_xticks(np.arange(0,30,3))
    ax.set_yticks(np.arange(0,30,3))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    # ax.invert_xaxis()
    ax.invert_yaxis()
    ax.grid(True)
    ax.vlines([9,18],0,27,'k')
    ax.hlines([9,18],0,27,'k')
    ax.set_xlim(0,27)
    ax.set_ylim(27,0)
    for i in range(9):
        for j in range(9):
            ind = i*9+j
            if data[ind].max() > 0.9999:
                # the cell is determined
                # just plot the value in the center of the cell
                ax.text(j*3+1.5,i*3+1.5,data[ind].argmax()+1,ha='center',va='center',fontsize=20)
            else:
                # the cell is not determined
                # plot the marginal distribution in a 3*3 grid
                for k in range(9):
                    ax.text(j*3+k%3+0.5,i*3+k//3+0.5,k+1,ha='center',va='center',fontsize=8,color='blue',alpha=data[ind,k])
    if plot_path is not None:
        plt.savefig(plot_path)
        plt.close()
    else:
        plt.show()




#%%
# data = [5, 3, 0, 0, 7, 0, 0, 0, 0,
#         6, 0, 0, 1, 9, 5, 0, 0, 0,
#         0, 9, 8, 0, 0, 0, 0, 6, 0,
#         8, 0, 0, 0, 6, 0, 0, 0, 3,
#         4, 0, 0, 8, 0, 3, 0, 0, 1,
#         7, 0, 0, 0, 2, 0, 0, 0, 6,
#         0, 6, 0, 0, 0, 0, 2, 8, 0,
#         0, 0, 0, 4, 1, 9, 0, 0, 5,
#         0, 0, 0, 0, 8, 0, 0, 7, 9]
# draw_sudoku(data)


# %%
