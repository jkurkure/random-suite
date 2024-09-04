# Check the randomness of simple-random.py

import os, sys
import matplotlib.pyplot as plt
import numpy as np

for seed in sys.argv[1:]:
    os.system(f"echo {seed}|python simple-random.py >> out.tmp")

f = open("out.tmp", "r")
s = f.read()

counts = []
for i in range(10):
    counts.append(s.count(f"{i}"))

x = np.array(range(10))
y = np.array(counts)
plt.bar(x, y)
plt.xlabel('Digit')
plt.ylabel('Frequency')
plt.savefig('results.png')
plt.show()

os.remove("out.tmp")