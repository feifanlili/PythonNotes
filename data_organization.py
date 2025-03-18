import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import Delaunay
from scipy.interpolate import interp2d

def read_DMA_data():
    # Read the file
    file_path = "your_file.txt"  # Change to your actual file path

    # Store parsed data
    data_dict = {}  
    current_point = None  

    with open(file_path, "r") as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            line = line.strip()
            
            # Detect "Point X"
            if line.startswith("Point"):
                current_point = line
                data_dict[current_point] = []
            
            # Ignore header, but store the actual data
            elif current_point and line and not line.startswith("Time"):
                data_dict[current_point].append(line.split("\t"))  # Assuming tab-separated values

    # Convert to DataFrame
    dfs = {}
    for point, data in data_dict.items():
        dfs[point] = pd.DataFrame(data, columns=["Time (s)", "Stress (MPa)", "Strain (%)"])
        dfs[point] = dfs[point].astype(float)  # Convert to numerical values

    # Plot the data
    plt.figure(figsize=(10, 5))

    for point, df in dfs.items():
        plt.plot(df["Time (s)"], df["Stress (MPa)"], label=f"{point} - Stress")
        plt.plot(df["Time (s)"], df["Strain (%)"], linestyle="dashed", label=f"{point} - Strain")

    plt.xlabel("Time (s)")
    plt.ylabel("Stress / Strain")
    plt.title("Stress and Strain Over Time")
    plt.legend()
    plt.grid()
    plt.show()


def delaunay_triangulation_3d_plot():
    # Sample scattered data (replace with your actual data)
    x = np.random.randint(1, 100, 50)  
    y = np.random.rand(50) * 10        
    z = np.random.rand(50) * 100       

    # Create a 2D mesh from (x, y)
    points2D = np.column_stack((x, y))
    tri = Delaunay(points2D)

    # Plot
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Plot surface using triangles
    ax.plot_trisurf(x, y, z, triangles=tri.simplices, cmap='viridis', alpha=0.8)

    # Labels
    ax.set_xlabel('Cycle')
    ax.set_ylabel('Strain')
    ax.set_zlabel('Stress')
    ax.set_title('3D Surface from Scattered Data')

    plt.show()

def data2d_intepolation():
    # Original grid
    x = np.linspace(0, 4, 5)  # 5 points
    y = np.linspace(0, 4, 5)  # 5 points
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.cos(Y)  # Sample function

    # Interpolation function
    interp_func = interp2d(x, y, Z, kind='cubic')

    # New finer grid
    x_new = np.linspace(0, 4, 50)  # 50 points
    y_new = np.linspace(0, 4, 50)  # 50 points
    Z_new = interp_func(x_new, y_new)

    # Plot original and interpolated data
    plt.subplot(1, 2, 1)
    plt.imshow(Z, extent=[0,4,0,4], origin='lower')
    plt.title("Original")

    plt.subplot(1, 2, 2)
    plt.imshow(Z_new, extent=[0,4,0,4], origin='lower')
    plt.title("Interpolated")

    plt.show()