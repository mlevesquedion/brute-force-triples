import time
import sys
from ctypes import cdll

lib = cdll.LoadLibrary("target/release/libtriples.so")

start = time.time()
lib.triples()
end = time.time()

sys.stderr.write(f"Using Rust: {end - start}\n")
