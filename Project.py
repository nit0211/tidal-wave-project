import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

raw_data = []
filename = 'ASTR19_F25_group_project_data.txt'

try:
    with open(filename, 'r') as f:
        print(f"Reading from {filename}...")
        for line in f:
            # Skip comments or empty lines
            if line.startswith('#') or not line.strip():
                continue
            
            parts = line.split()
            
            if len(parts) == 3:
                try:
                    day = int(parts[0])
                    time_str = parts[1]
                    height = float(parts[2])
                    raw_data.append((day, time_str, height))
                except ValueError:
                    continue 

    # This print statement is inside the 'try' block
    print(f"Successfully loaded {len(raw_data)} data points.")

# THIS PART IS CRITICAL - The 'try' block will crash without it!
except FileNotFoundError:
    print(f"ERROR: Could not find '{filename}'. Please make sure the file is in the same folder.")
    raw_data = [(1, "00:00", 0.0)]
