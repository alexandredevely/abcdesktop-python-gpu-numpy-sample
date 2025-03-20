#!/bin/bash
cd /src
source sample/bin/activate
echo "=== cpu time ==="
time python3 compute-cpu.py

echo "=== gpu time ==="
time python3 compute-gpu.py
