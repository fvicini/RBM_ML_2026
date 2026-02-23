import numpy as np
import scipy.sparse
import matplotlib.pyplot as plt
import matplotlib.tri

def make_np_sparse(A_sparse_data):	
	return make_np_sparse_shift(A_sparse_data, 0, 0)

def make_np_sparse_shift(A_sparse_data, shiftRows, shiftCols):	
	return scipy.sparse.csc_array((A_sparse_data.values, 
                                   ([i + shiftRows for i in A_sparse_data.rows],
                                    [i + shiftCols for i in A_sparse_data.cols])), 
                                  shape=(A_sparse_data.size[0], A_sparse_data.size[1]))
                                  
def plot_mesh(mesh, export_folder = ""):
    fig = plt.figure(figsize=plt.figaspect(0.5))
    
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_aspect('equal')
    
    coordinates = mesh.cell0_ds_coordinates()
    ax1.triplot(matplotlib.tri.Triangulation(coordinates[0, :], coordinates[1, :]), 'ko-', lw=1)
    ax1.grid(True)

    if export_folder != "":
        current_directory_path = os.getcwd()
        subfolder_path = os.path.join(current_directory_path, export_folder)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
        file_name = 'Mesh.png'
        file_path = os.path.join(subfolder_path, file_name)
        plt.savefig(file_path)
        plt.show()
        plt.close(fig)
