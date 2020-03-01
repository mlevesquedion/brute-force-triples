import time
import sys

import numpy as np


start = time.time()
i, j = np.ogrid[1:2000, 1:2000]
candidates = np.sqrt(i * i + j * j)
wheres = np.argwhere(np.mod(candidates, 1) == 0)

for a, b in sorted((np.unique(np.sort(wheres, axis=1), axis=0)).tolist()):
    print(f"({i[a, 0]}, {j[0, b]}, {int(candidates[a, b])})")
end = time.time()

sys.stderr.write(f"Using numpy: {end - start}\n")
