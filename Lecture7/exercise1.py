import numpy as np
import pandas as pd

class Exercise1:
    def vector(self):
        u = np.array([1, 2, 3, 4])
        col_u = u.reshape(-1, 1)
        v = np.array([10, 20, 30, 40])
        col_v = v.reshape(-1, 1)

        res_adding = col_u + col_v
        res_subtract = col_u - col_v
        res_multip = 2 * col_u
        res_square = col_u * col_u









