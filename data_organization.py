import pandas as pd
import matplotlib.pyplot as plt

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