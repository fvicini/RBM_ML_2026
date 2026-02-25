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
        if not os.path.exists(export_folder):
            os.makedirs(export_folder)
        file_name = 'Mesh.png'
        file_path = os.path.join(export_folder, file_name)
        plt.savefig(file_path)
        plt.show()
        plt.close(fig)
        
def plot_solution(mesh, solution_cell0Ds, title = "Solution", export_folder = ""):
    coordinates = mesh.cell0_ds_coordinates()
    x = coordinates[0,:]
    y = coordinates[1,:]
    z = solution_cell0Ds
    triang = matplotlib.tri.Triangulation(x, y)
    
    fig = plt.figure(figsize = plt.figaspect(0.5))
    fig.suptitle(title)
    
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_aspect('equal')
    tpc = ax1.tripcolor(triang, z, shading='flat')
    ax1.triplot(matplotlib.tri.Triangulation(coordinates[0, :], coordinates[1, :]), 'k--', lw=1)
    fig.colorbar(tpc)
    
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    ax2.plot_trisurf(x, y, z, triangles=triang.triangles, cmap=plt.cm.Spectral)
    
    if export_folder != "": 
        if not os.path.exists(export_folder):
            os.makedirs(export_folder)
        file_name = title + '.png'
        file_path = os.path.join(export_folder, file_name)
        plt.savefig(file_path)
        plt.show()
        plt.close(fig)
