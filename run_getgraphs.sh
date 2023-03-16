#!/bin/bash
for i in {0..99}
do
    echo "Starting ... job index $i"
    python sastvd/scripts/getgraphs.py "$i"
    echo "Finished index $i"
done