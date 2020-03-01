#!/bin/bash

cargo build --release

python3 triples_rs.py 1>rsout &
python3 triples_np.py 1>npout &
python3 triples.py 1>pyout

diff rsout npout
diff npout pyout

