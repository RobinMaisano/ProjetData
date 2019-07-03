import os
import sys
import subprocess


map_directory = str(os.path.dirname(os.path.abspath(__file__))) + '\\maps'
n_trucks = 10

if len(sys.argv) == 3:
    map_directory = sys.argv[1]
    n_trucks = sys.argv[2]


for files in os.listdir(map_directory):
    print("Currently: " + str(files))
    subprocess.run(["python", "script_cluster_greedy.py", str(map_directory) + "\\" + str(files), n_trucks])
