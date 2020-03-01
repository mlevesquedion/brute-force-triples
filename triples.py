import time
import sys


start = time.time()
for i in range(1, 2000):
    for j in range(i + 1, 2000):
        k = (i*i + j*j)**0.5
        if k % 1 == 0:
                print(f"({i}, {j}, {int(k)})")
end = time.time()

sys.stderr.write(f"Pure python: {end - start}\n")
