#!/bin/bash

python3 triples_rs.py 1>rsout &
python3 triples.py 1>pyout

diff pyout rsout

