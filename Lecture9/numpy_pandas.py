import numpy as np

class NumpyPandas:
    def test(self):

        #Transpose example1
        x = np.arange(12).reshape(3,4) #(samples =3, feature=4)
        xt = x.T #(4,3) #transposed

        #Indexing & Slicing
        a = np.arange(12).reshape(3, 4)
        a[0, 1]  # row 0, col 1
        a[0, :]  # first row
        a[:, 2]  # third column
        a[1:3, 1:4]  # submatrix

        #Masking -> core data selection technique
        z = np.array([0.1, 0.7, 0.2, 0.9])
        mask = z > 0.5
        z[mask]  # 0.7, 0.9
        z[a < 0.3] = 0.0  # modify selected values

        #Transpose example 2
        x_row = np.array([[1, 2, 3]])  # shape (1,3)
        x_col = x_row.T  # shape (3,1)
        print(x_row)
        print(x_col)

