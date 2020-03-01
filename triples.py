import time
import sys


start = time.time()
for i in range(1000):
    for j in range(i + 1, 1000):
        for k in range(j + 1, 1000):
            if i*i + j*j == k*k:
                print(f"({i}, {j}, {k})")
end = time.time()

sys.stderr.write(f"Pure python: {end - start}\n")
