import numpy as np
import scipy.sparse

def make_np_sparse(A_sparse_data):	
	return make_np_sparse_shift(A_sparse_data, 0, 0)

def make_np_sparse_shift(A_sparse_data, shiftRows, shiftCols):	
	return scipy.sparse.csc_array((A_sparse_data.values, 
                                   ([i + shiftRows for i in A_sparse_data.rows],
                                    [i + shiftCols for i in A_sparse_data.cols])), 
                                  shape=(A_sparse_data.size[0], A_sparse_data.size[1]))