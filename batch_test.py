#%%
import numpy as np
from Sudoku_render import draw_sudoku_simple, draw_sudoku_marginal
# reload the Sudoku_BPsolve.py
import importlib
import Sudoku_BPsolve
importlib.reload(Sudoku_BPsolve)
# from Sudoku_BPsolve import Sudoku_BP
import os 
# #%% Read the original data and save the first 1000 quizzes and solutions
# quizzes = np.zeros((1000000, 81), np.int32)
# solutions = np.zeros((1000000, 81), np.int32)
# for i, line in enumerate(open('sudoku.csv', 'r').read().splitlines()[1:]):
#     quiz, solution = line.split(",")
#     for j, q_s in enumerate(zip(quiz, solution)):
#         q, s = q_s
#         quizzes[i, j] = q
#         solutions[i, j] = s
# quizzes = quizzes.reshape((-1, 9, 9))
# solutions = solutions.reshape((-1, 9, 9))
# # save the fisrt 1000 quizzes and solutions
# np.save('quizzes_last1000.npy', quizzes[-1000:])
# np.save('solutions_last1000.npy', solutions[-1000:])
# %%
quizzes = np.load('quizzes1000.npy')
solutions = np.load('solutions1000.npy')
ind = 8
sudoku_one = quizzes[ind]
sudoku_one_sol = solutions[ind]
draw_sudoku_simple(sudoku_one.reshape(-1))
draw_sudoku_simple(sudoku_one_sol.reshape(-1))
# %%
def run_sudoku_BP(sudoku_one, ind,iters=20):
    # iters = 20
    plot_root = 'plots'
    plot_path = os.path.join(plot_root, 'sudoku_{}'.format(ind))
    if not os.path.exists(plot_path):
        os.makedirs(plot_path)
    solver = Sudoku_BPsolve.Sudoku_BP(sudoku_one)
    for i in range(iters):
        solver.iter = i
        solver.update_Q()
        solver.update_R()
        plot_name = os.path.join(plot_path, 'iter_{}.png'.format(i))
        draw_sudoku_marginal(solver.get_margin(),plot_name)
        if solver.if_complete():
            print('Solved')
            return True, solver
        if i == iters-1:
            print('Not solved')
            return False, solver

#%% solve the first 100 quizzes
solved = []
for i in range(10):
    print('Solving sudoku {}'.format(i))
    sol,_ = run_sudoku_BP(quizzes[i], i)
    solved.append(sol)
#%% solve the last 100 quizzes
quizzes = np.load('quizzes_last1000.npy')
solutions = np.load('solutions_last1000.npy')
solved = []
for i in range(100):
    print('Solving sudoku {}'.format(i))
    sol,_ = run_sudoku_BP(quizzes[i], 'last'+str(i))
    solved.append(sol)


# %%
# The world's hardest sudoku
sudoku_hard = np.array([[8,0,0,0,0,0,0,0,0],
                        [0,0,3,6,0,0,0,0,0],
                        [0,7,0,0,9,0,2,0,0],
                        [0,5,0,0,0,7,0,0,0],
                        [0,0,0,0,4,5,7,0,0],
                        [0,0,0,1,0,0,0,3,0],
                        [0,0,1,0,0,0,0,6,8],
                        [0,0,8,5,0,0,0,1,0],
                        [0,9,0,0,0,0,4,0,0]])
# solution to this sudoku
sudoku_hard_sol = np.array([[8,1,2,7,5,3,6,4,9],
                            [9,4,3,6,8,2,1,7,5],
                            [6,7,5,4,9,1,2,8,3],
                            [1,5,4,2,3,7,8,9,6],
                            [3,6,9,8,4,5,7,2,1],
                            [2,8,7,1,6,9,5,3,4],
                            [5,2,1,9,7,4,3,6,8],
                            [4,3,8,5,2,6,9,1,7],
                            [7,9,6,3,1,8,4,5,2]])
draw_sudoku_simple(sudoku_hard.reshape(-1))
# solved,solver = run_sudoku_BP(sudoku_hard, 'hard')
# %%
iters = 20
ind = 'hard'
marginal_lst = []
plot_root = 'plots'
plot_path = os.path.join(plot_root, 'sudoku_{}'.format(ind))
if not os.path.exists(plot_path):
    os.makedirs(plot_path)
solver = Sudoku_BPsolve.Sudoku_BP(sudoku_hard)
for i in range(iters):
    solver.iter = i
    solver.update_Q()
    solver.update_R()
    plot_name = os.path.join(plot_path, 'iter_{}.png'.format(i))
    draw_sudoku_marginal(solver.get_margin(),plot_name)
    marginal_lst.append(solver.get_margin())
    if solver.if_complete():
        print('Solved')
        break
    if i == iters-1:
        print('Not solved')
# %%
# sudoku_paper = np.array([[0,0,1,4,0,0,0,0,0],],
#                         0,9,0,0,0,0,3,0,0],])
